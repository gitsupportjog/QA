# -*- coding: utf-8 -*-
import os
import requests
import json
from datetime import datetime
from pathlib import Path
from dotenv import load_dotenv

# =========================
# LOAD ENV
# =========================
BASE_DIR = Path(__file__).resolve().parent
load_dotenv(BASE_DIR / ".env")

JIRA_BASE = os.getenv("JIRA_BASE")
JIRA_TOKEN = os.getenv("JIRA_TOKEN")
MATTERMOST_WEBHOOK = os.getenv("MATTERMOST_WEBHOOK")

if not all([JIRA_BASE, JIRA_TOKEN, MATTERMOST_WEBHOOK]):
    raise ValueError("Missing env variables")

# =========================
# CONFIG
# =========================
JQL = "project = G4BQADB AND resolution IS NOT EMPTY AND updated >= -24h ORDER BY updated DESC"

CACHE_FILE = BASE_DIR / "status_cache.json"

JIRA_TO_MM = {
    "Yordan Ridhanto": "@yordan.ridhanto",
    "Yahya Hardiyanto": "@yahya.hardiyanto",
    "Catur Putranto": "@catur.putranto",
}

RESOLUTION_LABEL = {
    "Fixed": "✅ BUG FIXED",
    "NAB": "❌ NOT A BUG",
    "WNF": "🚫 WILL NOT FIX",
    "Duplicate": "🔁 DUPLICATE",
    "Cannot Reproduce": "❓ CANNOT REPRODUCE"
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
# FETCH
# =========================
def fetch_issues():
    url = f"{JIRA_BASE}/rest/api/2/search"

    headers = {
        "Authorization": f"Bearer {JIRA_TOKEN}",
        "Accept": "application/json"
    }

    params = {
        "jql": JQL,
        "fields": "summary,status,resolution,reporter",
        "maxResults": 50
    }

    r = requests.get(url, headers=headers, params=params, timeout=15)
    r.raise_for_status()

    return r.json().get("issues", [])

# =========================
# SEND
# =========================
def send_message(text):
    requests.post(MATTERMOST_WEBHOOK, json={"text": text})

# =========================
# MAIN
# =========================
def main():
    print("== STATUS WATCHER STARTED ==")

    cache = load_cache()
    issues = fetch_issues()

    print(f"Fetched issues: {len(issues)}")

    messages = []

    for issue in issues:
        key = issue["key"]
        fields = issue["fields"]

        resolution = fields.get("resolution", {}).get("name")
        status = fields.get("status", {}).get("name")
        summary = fields.get("summary", "No summary")

        reporter = fields.get("reporter", {}).get("displayName", "Unknown")
        reporter_mm = JIRA_TO_MM.get(reporter, reporter)

        print(f"{key} | status={status} | resolution={resolution}")

        # skip kalau belum resolved
        if not resolution:
            continue

        # skip kalau sudah pernah dikirim
        if cache.get(key):
            continue

        label = RESOLUTION_LABEL.get(resolution, f"📌 {resolution}")
        link = f"{JIRA_BASE}/browse/{key}"

        messages.append(
            f"{label}\n"
            f"[{key}]({link})\n"
            f"{summary}\n"
            f"Reporter: {reporter_mm}"
        )

        cache[key] = True

    if messages:
        send_message("\n\n".join(messages))
        save_cache(cache)
        print(f"Sent {len(messages)} updates")
    else:
        print("No new updates")

# =========================
# ENTRY POINT
# =========================
if __name__ == "__main__":
    main()