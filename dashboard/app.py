# dashboard/app.py
import streamlit as st
import pandas as pd
import plotly.express as px
import joblib
import os
from predict import predict_churn

st.set_page_config(page_title="Churn Analysis", layout="wide")
st.title("📉 Customer Churn Analysis")

# 1. Get the directory that app.py lives in (C:\DataAnalyst\churn-analysis\dashboard)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# 2. Go one level up to the project root folder (C:\DataAnalyst\churn-analysis)
PROJECT_ROOT = os.path.dirname(BASE_DIR)

# 3. Construct a bulletproof absolute path to the dataset
DATA_PATH = os.path.join(PROJECT_ROOT, "data", "raw", "WA_Fn-UseC_-Telco.csv")

# ── Auto-load data ────────────────────────────────────────────
# @st.cache_data
# def load_data():
#     # path = "data/raw/WA_Fn-UseC_-Telco.csv"
#     df = pd.read_csv(DATA_PATH)
#     df["TotalCharges"] = pd.to_numeric(df["TotalCharges"], errors="coerce")
#     return df
@st.cache_data
def load_data():
    url = "https://raw.githubusercontent.com/dsrscientist/dataset1/master/Telco-Customer-Churn.csv"
    df = pd.read_csv(url)
    df["TotalCharges"] = pd.to_numeric(df["TotalCharges"], errors="coerce")
    return df

df = load_data()

# ── Tabs ──────────────────────────────────────────────────────
tab1, tab2 = st.tabs(["📊 Analysis", "🔮 Churn Predictor"])

with tab1:
    # KPIs
    churn_rate = (df["Churn"] == "Yes").mean() * 100
    k1, k2, k3, k4 = st.columns(4)
    k1.metric("Total Customers",  f"{len(df):,}")
    k2.metric("Churn Rate",        f"{churn_rate:.1f}%")
    k3.metric("Avg Monthly Charge",f"${df['MonthlyCharges'].mean():.0f}")
    k4.metric("Avg Tenure",        f"{df['tenure'].mean():.0f} months")

    st.divider()
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Churn by Contract Type")
        fig = px.histogram(df, x="Contract", color="Churn",
                           barmode="group",
                           color_discrete_sequence=["#4C72B0","#DD8452"])
        st.plotly_chart(fig, use_container_width=True)

    with col2:
        st.subheader("Monthly Charges Distribution")
        fig = px.box(df, x="Churn", y="MonthlyCharges", color="Churn",
                     color_discrete_sequence=["#4C72B0","#DD8452"])
        st.plotly_chart(fig, use_container_width=True)

    st.subheader("Churn by Internet Service & Payment Method")
    col3, col4 = st.columns(2)
    with col3:
        fig = px.histogram(df, x="InternetService", color="Churn",
                           barmode="group",
                           color_discrete_sequence=["#4C72B0","#DD8452"])
        st.plotly_chart(fig, use_container_width=True)
    with col4:
        fig = px.histogram(df, x="PaymentMethod", color="Churn",
                           barmode="group",
                           color_discrete_sequence=["#4C72B0","#DD8452"])
        st.plotly_chart(fig, use_container_width=True)

with tab2:
    st.subheader("Predict Churn Probability for a Customer")
    st.caption("Fill in customer details to get a churn risk score.")

    col1, col2, col3 = st.columns(3)

    with col1:
        tenure          = st.slider("Tenure (months)", 0, 72, 12)
        monthly_charges = st.slider("Monthly Charges ($)", 18, 120, 65)
        total_charges   = st.number_input("Total Charges ($)", 0.0, 9000.0, float(tenure * monthly_charges))

    with col2:
        contract     = st.selectbox("Contract", ["Month-to-month","One year","Two year"])
        internet     = st.selectbox("Internet Service", ["Fiber optic","DSL","No"])
        payment      = st.selectbox("Payment Method", ["Electronic check","Mailed check","Bank transfer (automatic)","Credit card (automatic)"])

    with col3:
        senior       = st.selectbox("Senior Citizen", ["No","Yes"])
        paperless    = st.selectbox("Paperless Billing", ["Yes","No"])
        tech_support = st.selectbox("Tech Support", ["No","Yes","No internet service"])

    if st.button("Predict Churn Risk", type="primary"):
        input_data = {
            "tenure": tenure,
            "MonthlyCharges": monthly_charges,
            "TotalCharges": total_charges,
            "SeniorCitizen": 1 if senior == "Yes" else 0,
            "PaperlessBilling": 1 if paperless == "Yes" else 0,
            "TechSupport": 1 if tech_support == "Yes" else 0,
            f"Contract_{contract}": 1 if contract != "Month-to-month" else 0,
            f"InternetService_{internet}": 1 if internet != "DSL" else 0,
            f"PaymentMethod_{payment}": 1,
        }
        prob, label = predict_churn(input_data)
        color = "red" if label == "High Risk" else "green"
        st.markdown(f"### Churn Probability: :{color}[{prob}%] — {label}")
        st.progress(int(prob))