# 🐙 AI-Powered GitHub Portfolio Reviewer

An AI-powered system that analyzes GitHub profiles and generates structured feedback using real-time data and Large Language Models.

## Website link
https://student-github-reviewer-ui-04ew.onrender.com/

## 🚀 Overview

This project is a full-stack AI application that:
- Fetches real-time GitHub data
- Analyzes repositories and programming languages
- Generates personalized feedback using an LLM
- Provides a clean web interface for interaction

---

## 🧠 Architecture


User → Streamlit UI → FastAPI Backend → LangGraph Agents
→ GitHub API → LLM (Groq / Llama 3) → Response → UI


---

## ⚙️ Tech Stack

- **Backend:** FastAPI  
- **Frontend:** Streamlit  
- **AI Framework:** LangGraph, LangChain  
- **LLM:** Groq (Llama 3.1)  
- **API Integration:** GitHub REST API  
- **Deployment:** Render  

---

## 🔁 How It Works

1. User enters a GitHub username  
2. Frontend sends request to FastAPI backend  
3. LangGraph orchestrates two agents:
   - **Data Extractor** → Fetches GitHub data  
   - **Code Mentor** → Generates feedback using LLM  
4. Results are returned and displayed in UI  

---

## 📊 Features

- 🔍 Real-time GitHub data extraction  
- 🤖 AI-generated portfolio feedback  
- ⚡ Fast API response using FastAPI  
- 🌐 Deployed microservices architecture  
- 🎯 Clean and interactive UI  

---

## 🛠️ Setup (Local)

```bash
git clone https://github.com/SayoojSb/student-github-reviewer.git
cd student-github-reviewer
2. Create Virtual Environment
python -m venv venv
source venv/bin/activate
3. Install Dependencies
pip install -r requirements.txt
4. Add Environment Variables

Create a .env file:
(api key and tokenid will expire in 30 days)
GROQ_API_KEY=your_groq_key
GITHUB_TOKEN=your_github_token
5. Run Backend
uvicorn main:app --reload
6. Run Frontend
streamlit run ui/app.py
```

### ☁️ Deployment

The project is deployed using Render:
Backend → FastAPI service
Frontend → Streamlit service

⚠️ Limitations
- Uses only recent repositories (limited analysis)
- Feedback may be generic for highly experienced developers
- No scoring or ranking system yet

🚀 Future Improvements
- Add portfolio scoring system
- Analyze README quality and repo metrics
- Improve LLM prompt engineering
- Introduce true agent decision-making
- Enhance UI/UX


## 👨‍💻 Author
Sayooj S B

## ⭐ Acknowledgements
- GitHub API
- Groq (Llama 3)
- LangGraph & LangChain

