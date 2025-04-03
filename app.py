'''
import streamlit as st
from PIL import Image

# ---- CONFIG ----
st.set_page_config(page_title="My Interactive CV", page_icon="📄", layout="wide")

# ---- SIDEBAR ----
st.sidebar.title("📌 Navigation")
menu = st.sidebar.radio("Go to", ["About Me", "Experience", "Projects", "Contact"])

# ---- ABOUT ME ----
if menu == "About Me":
    st.title("👤 About Me")
    col1, col2 = st.columns([1, 3])

    with col1:
        profile_pic = Image.open("profile.jpg")  # Replace with your image
        st.image(profile_pic, width=150)

    with col2:
        st.subheader("Your Name")
        st.write("""
        A brief introduction about yourself:
        - 🎓 Your background
        - 💼 Current focus or position
        - 🛠 Technologies you love
        """)

# ---- EXPERIENCE ----
elif menu == "Experience":
    st.title("💼 Experience")

    st.subheader("Job Title @ Company")
    st.write("Dates | Location")
    st.write("""
    - What you did
    - Skills or technologies used
    """)

    st.subheader("Another Job Title @ Company")
    st.write("Dates | Location")
    st.write("""
    - Your responsibilities
    - Any highlights or achievements
    """)

# ---- PROJECTS ----
elif menu == "Projects":
    st.title("🚀 Projects")

    st.markdown("### 🤖 OpenAI ChatBot")
    st.write("A chatbot using OpenAI's GPT API to answer questions.")
    st.markdown("[View Code](https://github.com/yourrepo/openai-chatbot)")

    st.markdown("### 🖼️ DALL·E Image Generator")
    st.write("An app that generates images from text prompts.")
    st.markdown("[View Code](https://github.com/yourrepo/dalle-app)")

    st.markdown("### 📄 PDF Summarizer")
    st.write("Summarizes uploaded PDFs using GPT-4.")
    st.markdown("[View Code](https://github.com/yourrepo/pdf-summarizer)")

# ---- CONTACT ----
elif menu == "Contact":
    st.title("📬 Contact")
    st.write("Feel free to reach out via:")

    st.markdown("- [LinkedIn](https://www.linkedin.com/in/yourprofile)")
    st.markdown("- [GitHub](https://github.com/yourprofile)")
    st.markdown("- 📧 your.email@example.com")

    st.download_button("📄 Download CV", data=open("cv.pdf", "rb"), file_name="CV.pdf")
'''
import openai
from chatbot import run_chatbot
import os

import streamlit as st

st.set_page_config(page_title="My CV", page_icon="📄", layout="wide")

# ---- Sidebar Navigation ----
st.sidebar.title("📌 Menu")
menu = st.sidebar.radio("Go to", ["About Me", "Experience", "Projects","Chatbot", "Contact"])

# ---- Page content ----

if menu == "About Me":
    st.title("👤 About Me")
    st.write("This is where you’ll introduce yourself.")

elif menu == "Experience":
    st.title("💼 Experience")
    st.write("Add your work experience here.")

elif menu == "Projects":
    st.title("🚀 Projects")
    st.write("Here you’ll showcase your projects.")
    
elif menu == "ChatBot":
    run_chatbot()

elif menu == "Contact":
    st.title("📬 Contact")
    st.write("Add links to your GitHub, LinkedIn, or email.")