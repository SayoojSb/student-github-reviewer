from typing import TypedDict, Optional

# Shared state between all agents
class ReviewState(TypedDict):
    username: str
    github_data: Optional[dict]
    feedback: Optional[str]