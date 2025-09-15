import streamlit as st

st.markdown("""
    <style>
    /* Full App Background */
    .stApp {
        background: linear-gradient(135deg, #74ebd5, #ACB6E5);
        font-family: 'Arial', sans-serif;
    }

    /* Title */
    .title {
        text-align: center;
        font-size: 45px;
        font-weight: bold;
        color: white;
        margin-bottom: 30px;
        text-shadow: 2px 2px 6px rgba(0,0,0,0.3);
    }

    /* Input Labels */
    label {
        font-size: 50px !important;
        font-weight: 800 !important;
        color: #222 !important;
    }

    /* Result Box */
    .result-box {
        background: rgba(255,255,255,0.95);
        padding: 30px;
        border-radius: 18px;
        text-align: center;
        margin-top: 25px;
        box-shadow: 0px 6px 18px rgba(0,0,0,0.25);
    }

    /* BMI Value */
    .bmi-value {
        font-size: 50px;
        font-weight: bold;
        color: #2E8B57;
    }

    /* Category */
    .category {
        font-size: 50px;
        font-weight: 600;
        margin-top: 12px;
    }

    /* Button */
    div.stButton > button {
        background: #2E86C1;
        color: white;
        font-size: 40px;
        font-weight: bold;
        border-radius: 10px;
        padding: 10px 24px;
        transition: 0.3s;
    }
    div.stButton > button:hover {
        background: #1B4F72;
        transform: scale(1.05);
    }
    </style>
""", unsafe_allow_html=True)

st.markdown('<div class="title"> Body Mass Index (BMI) Calculator </div>', unsafe_allow_html=True)

weight = st.number_input("Enter Your Weight in Kilograms (KG):", min_value=0.0, format="%.2f")
height = st.number_input("Enter Your Height in Centi Meters (CM):", min_value=0.0, format="%.2f")

if st.button("Calculate BMI"):
    if height > 0:
        bmi = weight / ((height / 100) ** 2)

        st.markdown(f"""
            <div class="result-box">
                <div class="bmi-value">Your BMI is: {bmi:.2f}</div>
        """, unsafe_allow_html=True)

        if bmi < 18.5:
            st.markdown('<div class="category" style="color:#E67E22;">Underweight</div></div>', unsafe_allow_html=True)
        elif 18.5 <= bmi < 24.9:
            st.markdown('<div class="category" style="color:#28B463;">Normal Weight</div></div>', unsafe_allow_html=True)
        elif 25 <= bmi < 29.9:
            st.markdown('<div class="category" style="color:#D4AC0D;">Overweight</div></div>', unsafe_allow_html=True)
        else:
            st.markdown('<div class="category" style="color:#C0392B;">Obese</div></div>', unsafe_allow_html=True)
    else:
        st.error("Height must be Greater Than Zero.")
