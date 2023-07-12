import streamlit as st
from send_email import send_email
import pandas as pd


st.header("Contact Us")

df = pd.read_csv("topics.csv")

with st.form(key="email_form"):
    user_email = st.text_input("Enter your email address")
    topic = st.selectbox("What topic do you want to discuss?",
                         df['topic'])
    raw_message = st.text_area("Your message")
    message = f"""\
    Subject: New email from {user_email}
    
    From: {user_email}
    Topic {topic}
    {raw_message}
    """
    button = st.form_submit_button("Submit")
    if button:
        send_email(message)
        st.info("Your email was sent successfully.")
