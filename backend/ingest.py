import requests, os

GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
REPO = "username/repo-name"

headers = {"Authorization": f"token {GITHUB_TOKEN}"}

def fetch_runs():
    url = f"https://api.github.com/repos/{REPO}/actions/runs"
    r = requests.get(url, headers=headers)
    data = r.json()
    return data["workflow_runs"]
