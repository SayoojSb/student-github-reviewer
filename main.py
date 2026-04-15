from fastapi import FastAPI
from agent.graph import github_reviewer_app

app = FastAPI()

@app.get("/")
def home():
    return {"message": "GitHub Reviewer backend is running perfectly!"}


@app.post("/review")
def review_portfolio(username: str):
    initial_state = {"username": username}

    result = github_reviewer_app.invoke(initial_state)

    return {
        "username": result["username"],
        "extracted_data": result.get("github_data"),
        "mentor_feedback": result.get("feedback")
    }