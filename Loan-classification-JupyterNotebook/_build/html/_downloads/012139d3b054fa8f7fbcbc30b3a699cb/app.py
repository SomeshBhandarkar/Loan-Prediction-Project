import streamlit as st
import requests
import numpy as np

API_URL = "https://loan-classification-backend-280303833155.us-central1.run.app/predict"

st.set_page_config(
    page_title="Loan Approval Classifier",
    page_icon="💰",
    layout="centered"
)

st.markdown("""
    <style>
    .main {
        padding: 2rem;
    }
    .stButton>button {
        width: 100%;
        margin-top: 2rem;
    }
    .result-box {
        padding: 1.5rem;
        border-radius: 0.5rem;
        margin: 1rem 0;
    }
    .success {
        background-color: #90EE90;
        color: #006400;
    }
    .failure {
        background-color: #FFB6C1;
        color: #8B0000;
    }
    </style>
    """, unsafe_allow_html=True)

st.title("💰 Loan Approval Classifier")
st.markdown("---")

col1, col2 = st.columns(2)

with col1:
    cd_account = st.number_input("CD Account (0 or 1)", min_value=0, max_value=1, step=1)
    education = st.number_input("Education Level (1-3)", min_value=1, max_value=3, step=1)
    ccavg = st.number_input("Credit Card Average", min_value=0.0, format="%.2f")

with col2:
    mortgage = st.number_input("Mortgage Value", min_value=0.0, format="%.2f")
    age = st.number_input("Age", min_value=18, max_value=100, step=1)
    income = st.number_input("Income", min_value=0.0, format="%.2f")

if st.button("Predict Loan Approval"):
    try:
        input_data = {
            "CD_Account": int(cd_account),
            "Education": int(education),
            "CCAvg": float(ccavg),
            "Mortgage": float(mortgage),
            "Age": int(age),
            "Income": float(income)
        }

        response = requests.post(API_URL, json=input_data)
        
        if response.status_code == 200:
            prediction = response.json().get("loan_prediction")

            st.markdown("### Result")
            if prediction == 1:
                st.markdown("""
                    <div class="result-box success">
                        <h3>✅ Loan Approved!</h3>
                        <p>Based on the provided information, you are eligible for the loan.</p>
                    </div>
                """, unsafe_allow_html=True)
            else:
                st.markdown("""
                    <div class="result-box failure">
                        <h3>❌ Loan Not Approved</h3>
                        <p>Unfortunately, based on the provided information, the loan cannot be approved.</p>
                    </div>
                """, unsafe_allow_html=True)
        else:
            st.error(f"Error from API: {response.text}")
            
    except requests.exceptions.RequestException as e:
        st.error(f"Error connecting to the backend service: {str(e)}")

with st.expander("ℹ️ Input Field Information"):
    st.markdown("""
    - **CD Account**: Whether you have a certificate of deposit account (0=No, 1=Yes)
    - **Education Level**: 1=Undergrad, 2=Graduate, 3=Advanced/Professional
    - **CCAvg**: Average spending on credit cards per month
    - **Mortgage**: Value of house mortgage if any
    - **Age**: Customer's age in years
    - **Income**: Annual income in thousands
    """)

st.markdown("---")
st.markdown("### 📊 Model Information")
st.write("This model uses machine learning to classify whether loan was approved based on various financial and personal factors.")

