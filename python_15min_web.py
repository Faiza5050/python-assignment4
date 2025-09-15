import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(
    page_title="Hello, World! This is a Streamlit Website.",
    page_icon="✨",
    layout="centered"
)

st.markdown("""
    <style>
        /* Background */
        .stApp {
            background: linear-gradient(135deg, #e0f7fa, #f1f8e9);
            font-family: 'Segoe UI', sans-serif;
        }

        /* Title */
        .css-10trblm {
            text-align: center;
            color: #2e7d32;
            font-size: 40px !important;
            font-weight: 700 !important;
        }

        /* Sidebar */
        .css-1d391kg {
            background-color: #f1f8e9 !important;
            padding: 15px;
            border-radius: 10px;
        }

        /* Headers */
        h2, h3 {
            color: #1565c0;
            font-weight: 600;
        }

        /* Inputs */
        .stTextInput>div>div>input {
            border: 2px solid #90caf9;
            border-radius: 10px;
            padding: 8px;
        }

        .stTextArea textarea {
            border: 2px solid #90caf9;
            border-radius: 10px;
        }

        /* Buttons */
        .stButton>button {
            background: linear-gradient(135deg, #42a5f5, #478ed1);
            color: white;
            border: none;
            padding: 10px 24px;
            border-radius: 12px;
            font-weight: 600;
            cursor: pointer;
            transition: all 0.3s ease-in-out;
        }
        .stButton>button:hover {
            background: linear-gradient(135deg, #1e88e5, #1565c0);
            transform: scale(1.05);
        }

        /* Success & Error messages */
        .stAlert {
            border-radius: 12px;
            font-weight: 500;
        }
    </style>
""", unsafe_allow_html=True)

st.title("Welcome To My Streamlit App")

st.sidebar.title("📌 MENU")
page = st.sidebar.selectbox("Select Page", ["Home", "About", "Contact"])

if page == "Home":
    st.header("🏠 Home Page")
    st.write("This is the Home Page of the Streamlit App.")
    name = st.text_input("Enter Your Name ", "Type Here ...")
    if name and name != "Type Here ...":
        st.success(f"Hello, {name}! Thanks For Using the Streamlit App. 🌟")

elif page == "About":
    st.header("ℹ️ About Page")
    st.write("This is the About Page of the Streamlit App.")
    st.write("""
        ✨ This App is Created to Demonstrate the Capabilities of Streamlit.  
        📊 You Can Upload a CSV File, View its Contents, and Generate Simple Plots.
    """)

elif page == "Contact":
    st.header("📧 Contact Page")
    st.write("You Can Reach Me at: ")
    email = st.text_input("Email", "Type Here ...")
    message = st.text_area("Message", "Type Here ...")

    if st.button("Submit"):
        if email and message and email != "Type Here ..." and message != "Type Here ...":
            st.success("✅ Thank You for Reaching Out! I Will Get Back to You Soon.")
        else:
            st.error("⚠️ Please Fill in All the Fields.")
