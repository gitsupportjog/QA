# -*- coding: utf-8 -*-
import os
import requests
import json
from datetime import datetime
from pathlib import Path
from dotenv import load_dotenv
from dateutil import parser
from requests.auth import HTTPBasicAuth

# =========================
# LOAD ENV
# =========================
BASE_DIR = Path(__file__).resolve().parent
load_dotenv(BASE_DIR / ".env")

JIRA_BASE = os.getenv("JIRA_BASE")
JIRA_EMAIL = os.getenv("JIRA_EMAIL")
JIRA_API_TOKEN = os.getenv("JIRA_API_TOKEN")
MATTERMOST_WEBHOOK = os.getenv("MATTERMOST_WEBHOOK")
JQL = os.getenv("JQL")

if not all([JIRA_BASE, JIRA_EMAIL, JIRA_API_TOKEN, MATTERMOST_WEBHOOK, JQL]):
    raise ValueError("Missing env config")

# =========================
# AUTH
# =========================
auth = HTTPBasicAuth(JIRA_EMAIL, JIRA_API_TOKEN)

# =========================
# MAPPING (EDIT SESUAI TIM KAMU)
# =========================
JIRA_TO_MM = {
    "Edi S. Putra": "@edi.putra",
    "Alba Alfath Millentry": "@alba.millentry"
}

# =========================
# CACHE
# =========================
CACHE_FILE = BASE_DIR / "sent_issues.json"

def load_cache():
    if CACHE_FILE.exists():
        return json.loads(CACHE_FILE.read_text())
    return {}

def save_cache(data):
    CACHE_FILE.write_text(json.dumps(data))

# =========================
# FETCH (UPDATED API)
# =========================
def fetch_issues():
    url = f"{JIRA_BASE}/rest/api/3/search/jql"

    headers = {
        "Accept": "application/json"
    }

    params = {
        "jql": JQL,
        "fields": ["comment", "reporter", "status"],
        "maxResults": 50
    }

    r = requests.get(url, headers=headers, params=params, auth=auth, timeout=15)

    if r.status_code == 401:
        print("[ERROR] Unauthorized → cek EMAIL / API TOKEN")
        return []

    if r.status_code == 410:
        print("[ERROR] Endpoint deprecated")
        return []

    r.raise_for_status()

    return r.json().get("issues", [])

# =========================
# SEND
# =========================
def send_mattermost(message: str):
    try:
        requests.post(MATTERMOST_WEBHOOK, json={"text": message}, timeout=10)
    except Exception as e:
        print("[ERROR] Failed to send:", e)

# =========================
# MAIN
# =========================
def main():
    print("== Atlassian Comment Watcher ==")

    cache = load_cache()
    issues = fetch_issues()

    print(f"Fetched issues: {len(issues)}")

    messages = []

    for issue in issues:
        key = issue["key"]
        fields = issue["fields"]

        reporter_name = fields.get("reporter", {}).get("displayName", "Unknown")
        reporter_mm = JIRA_TO_MM.get(reporter_name, reporter_name)

        comments = fields.get("comment", {}).get("comments", [])
        if not comments:
            continue

        latest = comments[-1]
        author_name = latest.get("author", {}).get("displayName", "Unknown")

        # skip kalau reporter sendiri yang komen
        if author_name == reporter_name:
            continue

        author_mm = JIRA_TO_MM.get(author_name, author_name)

        timestamp_str = latest.get("updated")
        timestamp = parser.parse(timestamp_str)

        # skip kalau sudah pernah dikirim
        if cache.get(key) == timestamp_str:
            continue

        cache[key] = timestamp_str

        link = f"{JIRA_BASE}/browse/{key}"

        messages.append(
            f"💬 NEW COMMENT\n"
            f"[{key}]({link})\n"
            f"👤 {author_mm} commented\n"
            f"🔔 {reporter_mm} please check"
        )

    # fallback message
    if not messages:
        now = datetime.now().strftime("%Y-%m-%d %H:%M")
        messages.append(f"ℹ️ No new comment ({now})")

    final_message = "\n\n".join(messages)

    send_mattermost(final_message)
    save_cache(cache)

    print("Done")
    print(final_message)

# =========================
# ENTRY POINT
# =========================
if __name__ == "__main__":
    main()