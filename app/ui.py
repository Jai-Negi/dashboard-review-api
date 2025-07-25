# app/ui.py

import streamlit as st
import requests

st.title("Dashboard Review Submission")

with st.form("review_form"):
    reviewer_name = st.text_input("Your Name", max_chars=50)
    dashboard_link = st.text_input("Dashboard URL")
    review_text = st.text_area("Review Text (optional)")
    uploaded_file = st.file_uploader("Upload a file (optional)")

    submitted = st.form_submit_button("Submit Review")

if submitted:
    if not reviewer_name or not dashboard_link:
        st.error("Please provide your name and dashboard URL.")
    else:
        url = "http://localhost:8000/submit-review"  # Your FastAPI backend URL

        # Prepare data for form submission
        data = {
            "reviewer_name": reviewer_name,
            "dashboard_link": dashboard_link,
            "review_text": review_text
        }

        files = None
        if uploaded_file:
            files = {"file": (uploaded_file.name, uploaded_file, uploaded_file.type)}

        try:
            response = requests.post(url, data=data, files=files)
            if response.status_code == 200:
                review_id = response.json().get("review_id")
                st.success(f"Review submitted successfully! Review ID: {review_id}")
            else:
                st.error(f"Failed to submit review: {response.text}")
        except Exception as e:
            st.error(f"Error connecting to backend: {e}")
