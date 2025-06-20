from internshala_scraper import scrape_internshala
from formatter import format_to_markdown
from github_uploader import push_to_github
from dotenv import load_dotenv
import os

# 🔓 Load secrets from .env file
load_dotenv()

if __name__ == "__main__":
    data = scrape_internshala(keyword="python", max_results=5)
    format_to_markdown(data)

    push_to_github(
        token=os.getenv("GITHUB_TOKEN"),            # ✅ Secure token access
        repo="eharshit/opdrop",
        branch="main",
        filepath="output/job_dump.md",
        commit_message="🚀 Auto-update from Opdrop"
    )
