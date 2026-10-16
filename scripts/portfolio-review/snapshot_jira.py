#!/usr/bin/env python3
"""Snapshot QYJI's Jira tickets (assignee or reporter) into CSV + JSON.

Usage:
    python3 scripts/portfolio-review/snapshot_jira.py reports/portfolio-review/YYYY-MM-DD

Network leg uses curl (system CA bundle) because Python urllib fails on the
corporate root CA. Token is read from ~/.config/jira/token and never printed.
"""
import csv
import json
import os
import subprocess
import sys
from datetime import date

JIRA = "https://jira.novonordisk.com/rest/api/2/search"
CA = "/etc/pki/tls/certs/ca-bundle.crt"
JQL = "(assignee = currentUser() OR reporter = currentUser()) ORDER BY updated DESC"
FIELDS = "summary,status,components,created,updated"


def main(out_dir: str) -> None:
    os.makedirs(out_dir, exist_ok=True)
    tok = open(os.path.expanduser("~/.config/jira/token")).read().strip()
    r = subprocess.run(
        ["curl", "-sS", "--cacert", CA, "-H", f"Authorization: Bearer {tok}", "-G",
         "--data-urlencode", f"jql={JQL}", "--data-urlencode", f"fields={FIELDS}",
         "--data-urlencode", "maxResults=200", JIRA],
        capture_output=True, text=True, check=True)
    data = json.loads(r.stdout)
    today = date.today()
    rows = []
    for i in data["issues"]:
        f = i["fields"]
        upd = f["updated"][:10]
        rows.append({
            "key": i["key"],
            "status": f["status"]["name"],
            "component": ",".join(c["name"] for c in f["components"]),
            "created": f["created"][:10],
            "updated": upd,
            "days_since_update": (today - date.fromisoformat(upd)).days,
            "summary": f["summary"].strip(),
        })
    with open(os.path.join(out_dir, "jira_snapshot.json"), "w") as fh:
        json.dump(rows, fh, indent=1, ensure_ascii=False)
    with open(os.path.join(out_dir, "jira_snapshot.csv"), "w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=list(rows[0]))
        w.writeheader()
        w.writerows(rows)
    print(f"{len(rows)} tickets (Jira total={data.get('total')}) -> {out_dir}")


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else f"reports/portfolio-review/{date.today()}")
