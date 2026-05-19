# -*- coding: utf-8 -*-
import os
import json
import requests
from pathlib import Path
from datetime import datetime
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
    raise ValueError("Missing JIRA_BASE / JIRA_TOKEN / MATTERMOST_WEBHOOK in .env")

# =========================
# CONFIG
# =========================
CACHE_FILE = BASE_DIR / "sent_bug_cache.json"

# Mapping mention (opsional)
JIRA_TO_MM = {
    "Yordan Ridhanto": "@yordan.ridhanto",
    "Yahya Hardiyanto": "@Yahya.Hardiyanto",
    "Catur Putranto": "@catur.putranto",
    "Andri Bagastomo": "@andri.bagastomo",
}

# Reporter whitelist (HANYA ini yang dikirim)
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
# FETCH BUGS
# =========================
def fetch_new_bugs():
    url = f"{JIRA_BASE}/rest/api/2/search"

    headers = {
        "Accept": "application/json",
        "Authorization": f"Bearer {JIRA_TOKEN}"
    }

    # Bug yang dibuat 10 menit terakhir
    jql = "issuetype = Bug AND created >= -10m ORDER BY created DESC"

    params = {
        "jql": jql,
        "fields": "summary,reporter,priority,status,created",
        "maxResults": 50
    }

    r = requests.get(url, headers=headers, params=params, timeout=15)
    r.raise_for_status()
    return r.json().get("issues", [])

# =========================
# SEND TO MATTERMOST
# =========================
def send_message(text):
    payload = {"text": text}
    r = requests.post(MATTERMOST_WEBHOOK, json=payload, timeout=10)
    print("STATUS:", r.status_code)

# =========================
# FORMAT MESSAGE
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
        f"Reporter: {reporter_mm}"
    )

# =========================
# MAIN
# =========================
def main():
    cache = load_cache()
    new_bugs = fetch_new_bugs()
    messages = []

    for issue in new_bugs:
        key = issue["key"]
        fields = issue["fields"]

        reporter = fields.get("reporter", {}).get("displayName", "Unknown")

        # FILTER REPORTER
        if reporter not in ALLOWED_REPORTERS:
            print(f"Skip reporter: {reporter}")
            continue

        # Skip jika sudah pernah dikirim
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
        # send_message("No new bugs added")
        print("No new bugs")

if __name__ == "__main__":
    main()