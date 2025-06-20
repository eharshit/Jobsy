import base64
import requests

def push_to_github(token, repo, branch, filepath, commit_message):
    api_url = f"https://api.github.com/repos/{repo}/contents/{filepath}"
    
    # Read local file content
    with open(filepath, "rb") as f:
        content = f.read()
        encoded_content = base64.b64encode(content).decode("utf-8")

    # Check if file already exists
    headers = {"Authorization": f"token {token}"}
    response = requests.get(api_url, headers=headers)
    
    sha = response.json().get("sha") if response.status_code == 200 else None

    # Payload
    payload = {
        "message": commit_message,
        "content": encoded_content,
        "branch": branch,
    }
    if sha:
        payload["sha"] = sha

    response = requests.put(api_url, headers=headers, json=payload)

    if response.status_code in [200, 201]:
        print("✅ Markdown pushed to GitHub!")
    else:
        print("❌ GitHub push failed:", response.status_code, response.text)
