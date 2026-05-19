# -*- coding: utf-8 -*-
import os
import json
import requests
from pathlib import Path
from datetime import datetime
from dotenv import load_dotenv
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

if not all([JIRA_BASE, JIRA_EMAIL, JIRA_API_TOKEN, MATTERMOST_WEBHOOK]):
    raise ValueError("Missing env config")

# =========================
# AUTH (ATLASIAN CLOUD)
# =========================
auth = HTTPBasicAuth(JIRA_EMAIL, JIRA_API_TOKEN)

# =========================
# CONFIG
# =========================
CACHE_FILE = BASE_DIR / "sent_bug_cache.json"

JIRA_TO_MM = {
    "Yordan Ridhanto": "@yordan.ridhanto",
    "Yahya Hardiyanto": "@yahya.hardiyanto",
    "Catur Putranto": "@catur.putranto",
    "Andri Bagastomo": "@andri.bagastomo",
}

ALLOWED_REPORTERS = {
    "Yordan Ridhanto",
    "Yahya Hardiyanto",
    "Amri Arfian",
    "Catur Putranto",
    "Andri Bagastomo",
}

# =========================
# CACHE
# =========================
def load_cache():
    if CACHE_FILE.exists():
        return json.loads(CACHE_FILE.read_text())
    return {}

def save_cache(data):
    CACHE_FILE.write_text(json.dumps(data))

# =========================
# FETCH BUGS (UPDATED API)
# =========================
def fetch_new_bugs():
    url = f"{JIRA_BASE}/rest/api/3/search/jql"

    headers = {
        "Accept": "application/json"
    }

    # 🔥 pakai relative time (real-time-ish)
    jql = "issuetype = Bug AND created >= -10m ORDER BY created DESC"

    params = {
        "jql": jql,
        "fields": ["summary", "reporter", "priority", "status", "created"],
        "maxResults": 50
    }

    r = requests.get(url, headers=headers, params=params, auth=auth, timeout=15)

    if r.status_code == 401:
        print("[ERROR] Unauthorized → cek EMAIL/API TOKEN")
        return []

    r.raise_for_status()

    return r.json().get("issues", [])

# =========================
# SEND
# =========================
def send_message(text):
    try:
        r = requests.post(MATTERMOST_WEBHOOK, json={"text": text}, timeout=10)
        print("STATUS:", r.status_code)
    except Exception as e:
        print("[ERROR] Send failed:", e)

# =========================
# FORMAT
# =========================
def format_bug_message(issue):
    key = issue["key"]
    fields = issue["fields"]

    summary = fields.get("summary", "No summary")
    reporter = fields.get("reporter", {}).get("displayName", "Unknown")
    priority = fields.get("priority", {}).get("name", "None")
    status = fields.get("status", {}).get("name", "Unknown")

    reporter_mm = JIRA_TO_MM.get(reporter, reporter)
    link = f"{JIRA_BASE}/browse/{key}"

    return (
        f"🐞 NEW BUG\n"
        f"[{key}]({link})\n"
        f"Summary: {summary}\n"
        f"Priority: {priority}\n"
        f"Status: {status}\n"
        f"👤 Reporter: {reporter_mm}"
    )

# =========================
# MAIN
# =========================
def main():
    print("== NEW BUG WATCHER (ATLASSIAN) ==")

    cache = load_cache()
    new_bugs = fetch_new_bugs()

    print(f"Fetched bugs: {len(new_bugs)}")

    messages = []

    for issue in new_bugs:
        key = issue["key"]
        fields = issue["fields"]

        reporter = fields.get("reporter", {}).get("displayName", "Unknown")

        # FILTER REPORTER
        if reporter not in ALLOWED_REPORTERS:
            print(f"Skip reporter: {reporter}")
            continue

        # skip jika sudah pernah dikirim
        if cache.get(key):
            continue

        messages.append(format_bug_message(issue))
        cache[key] = True

    if messages:
        final_message = "\n\n".join(messages)
        send_message(final_message)
        save_cache(cache)
        print(f"Sent {len(messages)} new bug(s)")
    else:
        now = datetime.now().strftime("%Y-%m-%d %H:%M")
        send_message(f"ℹ️ No new bugs added ({now})")
        print("No new bugs")

# =========================
# ENTRY
# =========================
if __name__ == "__main__":
    main()