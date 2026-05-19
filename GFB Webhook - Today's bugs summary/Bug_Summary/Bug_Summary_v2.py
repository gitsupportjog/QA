# -*- coding: utf-8 -*-
import os
import requests
from pathlib import Path
from collections import Counter
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
# FETCH BUG DATA (UPDATED API)
# =========================
def fetch_bugs(jql):
    url = f"{JIRA_BASE}/rest/api/3/search/jql"

    headers = {
        "Accept": "application/json"
    }

    params = {
        "jql": jql,
        "fields": ["priority", "status", "reporter"],
        "maxResults": 100
    }

    r = requests.get(url, headers=headers, params=params, auth=auth, timeout=15)

    if r.status_code == 401:
        print("[ERROR] Unauthorized → cek EMAIL/API TOKEN")
        return []

    r.raise_for_status()

    return r.json().get("issues", [])

# =========================
# SEND MESSAGE
# =========================
def send_message(text):
    try:
        r = requests.post(MATTERMOST_WEBHOOK, json={"text": text}, timeout=10)
        print("STATUS:", r.status_code)
    except Exception as e:
        print("[ERROR] Send failed:", e)

# =========================
# MAIN
# =========================
def main():

    print("== QA BUG DASHBOARD (ATLASSIAN) ==")

    # 🔥 pakai JQL dari .env sebagai base
    BASE_JQL = os.getenv("JQL")

    # BUG dibuat hari ini
    new_bug_jql = f"{BASE_JQL} AND issuetype = Bug AND created >= startOfDay()"
    new_bugs = fetch_bugs(new_bug_jql)

    # BUG masih open
    open_bug_jql = f"{BASE_JQL} AND issuetype = Bug AND statusCategory != Done"
    open_bugs = fetch_bugs(open_bug_jql)

    print(f"New bugs: {len(new_bugs)} | Open bugs: {len(open_bugs)}")

    # =========================
    # PRIORITY COUNT
    # =========================
    priority_counter = Counter()

    for bug in open_bugs:
        priority = bug["fields"].get("priority", {}).get("name", "None")
        priority_counter[priority] += 1

    # =========================
    # REPORTER COUNT
    # =========================
    reporter_counter = Counter()

    for bug in new_bugs:
        reporter = bug["fields"].get("reporter", {}).get("displayName", "Unknown")
        reporter_counter[reporter] += 1

    top_reporters = reporter_counter.most_common(3)

    reporter_text = ""
    if top_reporters:
        for name, count in top_reporters:
            reporter_text += f"- {name} ({count})\n"
    else:
        reporter_text = "- No bug reported today"

    # =========================
    # MESSAGE FORMAT
    # =========================
    message = f"""
📊 **QA BUG DASHBOARD**

| Metric | Count |
|------|------|
| 🐞 New Bugs Today | {len(new_bugs)} |
| 📂 Open Bugs | {len(open_bugs)} |

**Priority Breakdown**

🔴 Critical: {priority_counter.get("Critical",0)}  
🟠 High: {priority_counter.get("High",0)}  
🟡 Medium: {priority_counter.get("Medium",0)}  
🟢 Low: {priority_counter.get("Low",0)}

**Top Reporters Today**

{reporter_text}

🔎 Jira Dashboard  
{JIRA_BASE}/issues/?jql=issuetype=Bug
"""

    send_message(message)

# =========================
if __name__ == "__main__":
    main()