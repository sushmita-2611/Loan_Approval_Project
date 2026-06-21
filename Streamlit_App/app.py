import streamlit as st
import pandas as pd
import joblib
import os

st.set_page_config(
    page_title="Loan Approval Prediction",
    page_icon="🏦",
    layout="centered"
)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
model = joblib.load(os.path.join(BASE_DIR, "..", "Model", "loan_model.pkl"))

st.title("🏦 Loan Approval Prediction System")

st.info(
    "This application predicts whether a loan application is likely to be approved "
    "based on applicant details using a Machine Learning model."
)

st.markdown("---")

st.subheader("👤 Applicant Information")

gender = st.selectbox(
    "Gender",
    ["Select Gender", "Male", "Female"]
)

married = st.selectbox(
    "Marital Status",
    ["Select Marital Status", "Married", "Unmarried"]
)

dependents = st.selectbox(
    "Number of Dependents",
    [0, 1, 2, 3]
)

education = st.selectbox(
    "Education",
    ["Select Education", "Graduate", "Not Graduate"]
)

employment = st.selectbox(
    "Employment Type",
    ["Select Employment Type", "Salaried", "Self Employed"]
)

st.markdown("---")

st.subheader("💰 Financial Information")

applicant_income = st.number_input(
    "Applicant Monthly Income (₹)",
    min_value=0,
    value=0,
    step=500
)

coapplicant_income = st.number_input(
    "Co-Applicant Monthly Income (₹)",
    min_value=0,
    value=0,
    step=500
)

loan_amount = st.number_input(
    "Requested Loan Amount (₹ Thousand)",
    min_value=0,
    value=0,
    step=10
)

loan_amount_term = st.number_input(
    "Loan Repayment Period (Months)",
    min_value=12,
    value=360,
    step=12
)

credit_history = st.selectbox(
    "Credit History",
    ["Select Credit History", "Good", "Bad"]
)

property_area = st.selectbox(
    "Property Area",
    ["Select Property Area", "Rural", "Semiurban", "Urban"]
)

st.markdown("---")

if st.button("Predict Loan Status", use_container_width=True):

    # Validation

    if gender == "Select Gender":
        st.warning("Please select Gender.")
        st.stop()

    if married == "Select Marital Status":
        st.warning("Please select Marital Status.")
        st.stop()

    if education == "Select Education":
        st.warning("Please select Education.")
        st.stop()

    if employment == "Select Employment Type":
        st.warning("Please select Employment Type.")
        st.stop()

    if credit_history == "Select Credit History":
        st.warning("Please select Credit History.")
        st.stop()

    if property_area == "Select Property Area":
        st.warning("Please select Property Area.")
        st.stop()

    if applicant_income <= 0:
        st.warning("Please enter Applicant Monthly Income.")
        st.stop()

    if loan_amount <= 0:
        st.warning("Please enter Requested Loan Amount.")
        st.stop()

    # Encoding

    gender = 1 if gender == "Male" else 0

    married = 1 if married == "Married" else 0

    education = 0 if education == "Graduate" else 1

    self_employed = 1 if employment == "Self Employed" else 0

    credit_history = 1 if credit_history == "Good" else 0

    if property_area == "Rural":
        property_area = 0
    elif property_area == "Semiurban":
        property_area = 1
    else:
        property_area = 2

    # Create Input DataFrame

    input_data = pd.DataFrame([[
        gender,
        married,
        dependents,
        education,
        self_employed,
        applicant_income,
        coapplicant_income,
        loan_amount,
        loan_amount_term,
        credit_history,
        property_area
    ]], columns=[
        "Gender",
        "Married",
        "Dependents",
        "Education",
        "Self_Employed",
        "ApplicantIncome",
        "CoapplicantIncome",
        "LoanAmount",
        "Loan_Amount_Term",
        "Credit_History",
        "Property_Area"
    ])

    prediction = model.predict(input_data)

    st.markdown("---")
    st.subheader("Prediction Result")

    if prediction[0] == 1:

        st.success("✅ Loan Status: APPROVED")

        st.write(
            """
The applicant satisfies the eligibility criteria.

According to the trained Machine Learning model,
the loan application is likely to be approved.
"""
        )

    else:

        st.error("❌ Loan Status: REJECTED")

        st.write(
            """
The applicant does not satisfy the eligibility criteria.

According to the trained Machine Learning model,
the loan application is likely to be rejected.
"""
        )

st.markdown("---")
st.markdown(
    "<div style='text-align: center; color: gray;'>Developed by <b>Sushmita Tiwari and Tanu Khatri</b></div>",
    unsafe_allow_html=True
)
