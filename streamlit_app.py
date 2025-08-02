import streamlit as st
import pandas as pd
import joblib
from PIL import Image

# Load model, feature columns, and scaler
model, feature_columns, scaler = joblib.load("churn_model.pkl")

st.set_page_config(page_title="Customer Churn Predictor", page_icon="📱", layout="centered")
st.image("https://cdn-icons-png.flaticon.com/512/4321/4321936.png", width=100)
st.title("Customer Churn Prediction App")

st.markdown("Use this tool to predict whether a customer is likely to **churn or stay** based on their telecom usage patterns.")

st.header("📋 Customer Info")

# Core demographic and billing inputs
gender = st.selectbox("Gender", ["Male", "Female"])
SeniorCitizen = st.selectbox("Senior Citizen", ["No", "Yes"])
Partner = st.radio("Has a Partner?", ["Yes", "No"], horizontal=True)
Dependents = st.radio("Has Dependents?", ["Yes", "No"], horizontal=True)
tenure = st.slider("Tenure (months)", 0, 72, 12)
MonthlyCharges = st.number_input("Monthly Charges ($)", 0.0, 200.0, 70.0)
TotalCharges = st.number_input("Total Charges ($)", 0.0, 10000.0, 2000.0)

# Service usage options
PhoneService = st.selectbox("Phone Service", ["Yes", "No"])
MultipleLines = st.selectbox("Multiple Lines", ["No", "Yes", "No phone service"])
InternetService = st.selectbox("Internet Service", ["DSL", "Fiber optic", "No"])
OnlineSecurity = st.selectbox("Online Security", ["No", "Yes", "No internet service"])
OnlineBackup = st.selectbox("Online Backup", ["No", "Yes", "No internet service"])
DeviceProtection = st.selectbox("Device Protection", ["No", "Yes", "No internet service"])
TechSupport = st.selectbox("Tech Support", ["No", "Yes", "No internet service"])
StreamingTV = st.selectbox("Streaming TV", ["No", "Yes", "No internet service"])
StreamingMovies = st.selectbox("Streaming Movies", ["No", "Yes", "No internet service"])

# Contract & billing
Contract = st.selectbox("Contract Type", ["Month-to-month", "One year", "Two year"])
PaperlessBilling = st.selectbox("Paperless Billing", ["Yes", "No"])
PaymentMethod = st.selectbox("Payment Method", [
    "Electronic check", "Mailed check", "Bank transfer (automatic)", "Credit card (automatic)"
])

# Manual encoding
input_dict = {
    "gender": 1 if gender == "Male" else 0,
    "SeniorCitizen": 1 if SeniorCitizen == "Yes" else 0,
    "Partner": 1 if Partner == "Yes" else 0,
    "Dependents": 1 if Dependents == "Yes" else 0,
    "tenure": tenure,
    "MonthlyCharges": MonthlyCharges,
    "TotalCharges": TotalCharges,
    "PhoneService": 1 if PhoneService == "Yes" else 0,
    "PaperlessBilling": 1 if PaperlessBilling == "Yes" else 0,

    # One-hot encoded features
    f"MultipleLines_{MultipleLines}": 1,
    f"InternetService_{InternetService}": 1,
    f"OnlineSecurity_{OnlineSecurity}": 1,
    f"OnlineBackup_{OnlineBackup}": 1,
    f"DeviceProtection_{DeviceProtection}": 1,
    f"TechSupport_{TechSupport}": 1,
    f"StreamingTV_{StreamingTV}": 1,
    f"StreamingMovies_{StreamingMovies}": 1,
    f"Contract_{Contract}": 1,
    f"PaymentMethod_{PaymentMethod}": 1,
}

# Fill in remaining columns with 0s if missing
for col in feature_columns:
    if col not in input_dict:
        input_dict[col] = 0

# DataFrame in order
input_df = pd.DataFrame([input_dict])[feature_columns]

# Scale and predict
input_scaled = scaler.transform(input_df)

if st.button("🔮 Predict Churn"):
    prediction = model.predict(input_scaled)[0]
    st.subheader("📊 Prediction Result")
    if prediction == 1:
        st.error("⚠️ This customer is likely to CHURN.")
        st.markdown("💡 Consider offering loyalty discounts or better service plans.")
    else:
        st.success("✅ Great! This customer is likely to STAY.")
        st.markdown("🎯 Keep them engaged with consistent service.")

st.markdown("---")
st.caption("Built with ❤️ using Streamlit | Project: Customer Churn Predictor")
