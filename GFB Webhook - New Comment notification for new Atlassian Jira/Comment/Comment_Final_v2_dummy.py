# -*- coding: utf-8 -*-
import os
import requests
import json
from datetime import datetime, timedelta
from pathlib import Path
from dotenv import load_dotenv
from dateutil import parser

# === LOAD CONFIG FROM .ENV ===
project_root = Path(__file__).resolve().parent
env_path = project_root / ".env"
load_dotenv(dotenv_path=env_path)

JIRA_BASE = os.getenv("JIRA_BASE")
JIRA_TOKEN = os.getenv("JIRA_TOKEN")
MATTERMOST_WEBHOOK = os.getenv("MATTERMOST_WEBHOOK")
JQL = os.getenv("JQL")

if not JIRA_BASE or not JIRA_TOKEN or not MATTERMOST_WEBHOOK or not JQL:
    print("[ERROR] Please set JIRA_BASE, JIRA_TOKEN, MATTERMOST_WEBHOOK, and JQL in your .env file")
    input("Press ENTER to exit...")
    exit(1)

jira_to_mattermost = {
    "Edi S. Putra": "@edi.putra",
    "Alba Alfath Millentry": "@alba.millentry"

}


CACHE_FILE = project_root / "sent_issues.json"
last_comment_time = {}

def load_cache():
    if CACHE_FILE.exists():
        with open(CACHE_FILE, "r") as f:
            return json.load(f)
    return {}

def save_cache():
    with open(CACHE_FILE, "w") as f:
        json.dump(last_comment_time, f)

def send_mattermost(message: str):
    try:
        response = requests.post(MATTERMOST_WEBHOOK, json={"text": message}, timeout=10)
        if response.status_code != 200:
            print(f"[WARNING] Mattermost webhook failed: {response.status_code}")
    except Exception as e:
        print(f"[ERROR] Failed to send Mattermost notification: {e}")

def fetch_issues():
    url = f"{JIRA_BASE}/rest/api/2/search"
    headers = {
        "Accept": "application/json",
        "Authorization": f"Bearer {JIRA_TOKEN}"
    }
    
    params = {"jql": JQL, "fields": "comment,reporter,status"}

    try:
        r = requests.get(url, headers=headers, params=params, timeout=10)
        if r.status_code == 401:
            print("[ERROR] Unauthorized: Check your JIRA_TOKEN")
            return []
        r.raise_for_status()
        return r.json().get("issues", [])
    except Exception as e:
        print("[ERROR] Failed to fetch issues:", e)
        return []

def main():
    global last_comment_time
    last_comment_time = load_cache()

    print("== Jira Comment Watcher Started ==")
    today = datetime.now().date()
    yesterday = today - timedelta(days=1)

    issues = fetch_issues()
    messages = []

    for issue in issues:
        key = issue["key"]

        
        status_name = issue["fields"].get("status", {}).get("name", "").lower()
        if status_name == "fix confirmed":
            continue

        reporter_name = issue["fields"]["reporter"]["displayName"]
        reporter_mm = jira_to_mattermost.get(reporter_name, reporter_name)

        comments = issue["fields"]["comment"]["comments"]
        if not comments:
            continue

        latest = comments[-1]
        author_name = latest["author"]["displayName"]

        
        if author_name == reporter_name:
            continue

        author_mm = jira_to_mattermost.get(author_name, author_name)
        timestamp_str = latest["updated"]
        timestamp = parser.parse(timestamp_str)
        
        if last_comment_time.get(key) == timestamp_str:
            continue

        last_comment_time[key] = timestamp_str

        issue_link = f"{JIRA_BASE}/browse/{key}"
        messages.append(f"- [{key}]({issue_link}) has new comment by {author_mm}. Please check {reporter_mm}")

    
    # if not messages:
        now = datetime.now().strftime("%Y-%m-%d %H:%M")
        messages.append(f"- No new comment added ({now})")

    final_message = "\n".join(messages)

    send_mattermost(final_message)
    save_cache()

    print(f"[{datetime.now()}] Message sent:\n{final_message}")
    # input("\n=== Script finished. Press ENTER to exit ===")

if __name__ == "__main__":
    main()