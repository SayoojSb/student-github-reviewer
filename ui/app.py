import streamlit as st
import requests

st.set_page_config(page_title="GitHub Code Mentor", page_icon="🐙")

st.title("🐙 The Student GitHub & Portfolio Reviewer")

# Input field
username = st.text_input("GitHub Username:", placeholder="e.g., torvalds")

# Button click
if st.button("Analyze Portfolio"):
    if username:
        with st.spinner(f"Analyzing {username}'s repositories..."):
            try:
                # Backend API URL (local for now)
                url = f"https://student-github-reviewer-mvkc.onrender.com/review?username={username}"

                response = requests.post(url)

                if response.status_code == 200:
                    data = response.json()

                    st.success("Analysis Complete!")

                    # Show extracted data
                    st.subheader("📊 Extracted GitHub Data")
                    st.json(data["extracted_data"])

                    # Show feedback
                    st.subheader("🤖 Mentor Feedback")
                    st.write(data["mentor_feedback"])

                else:
                    st.error(f"Backend Error: {response.status_code}")

            except Exception as e:
                st.error("❌ Could not connect to backend.")
                st.write(str(e))

    else:
        st.warning("⚠️ Please enter a GitHub username.")