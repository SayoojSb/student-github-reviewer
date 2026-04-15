import os
import requests
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage
from .state import ReviewState

load_dotenv()

# Initialize LLM
llm = ChatGroq(
    model="llama-3.1-8b-instant",
    temperature=0.7
)

# -------------------------------
# Node 1: Extract GitHub Data
# -------------------------------
def extract_github_data(state: ReviewState):
    username = state["username"]
    github_token = os.getenv("GITHUB_TOKEN")

    headers = {
        "Authorization": f"Bearer {github_token}"
    } if github_token else {}

    try:
        user_url = f"https://api.github.com/users/{username}"
        repos_url = f"https://api.github.com/users/{username}/repos?sort=updated&per_page=5"

        user_resp = requests.get(user_url, headers=headers, timeout=5)
        repos_resp = requests.get(repos_url, headers=headers, timeout=5)

        if user_resp.status_code == 200 and repos_resp.status_code == 200:
            repos_data = repos_resp.json()

            repo_names = [repo["name"] for repo in repos_data]

            languages = list(set([
                repo["language"]
                for repo in repos_data
                if repo["language"]
            ]))

            real_data = {
                "recent_repos": repo_names,
                "primary_languages": languages,
                "public_repos_count": user_resp.json().get("public_repos", 0)
            }

            return {"github_data": real_data}

        else:
            return {
                "github_data": {
                    "error": f"API Error: User '{username}' not found or rate-limited."
                }
            }

    except Exception as e:
        return {"github_data": {"error": str(e)}}


# -------------------------------
# Node 2: Generate AI Feedback
# -------------------------------
def code_mentor_review(state: ReviewState):
    username = state["username"]
    data = state.get("github_data", {})

    try:
        prompt = f"""
You are an encouraging Code Mentor.

Review this GitHub portfolio for user: {username}

Data:
{data}

Give:
1. Strengths based on languages and activity
2. 1-2 actionable improvements

Keep it short, clear, and professional.
"""

        response = llm.invoke([
            HumanMessage(content=prompt)
        ])

        return {"feedback": response.content}

    except Exception as e:
        return {"feedback": f"LLM Error: {str(e)}"}