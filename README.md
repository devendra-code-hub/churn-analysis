# 📉 Customer Churn Analysis

An end-to-end data analytics and machine learning project built on the **Telco Customer Churn dataset**, covering exploratory analysis, feature engineering, logistic regression modeling, and an interactive two-tab Streamlit dashboard with a live churn predictor.

 

---

## 🖥️ Live Demo

> _Deploy to Render and paste your URL here_
> `https://churn-analysis-vx5a.onrender.com`

---

## 📁 Project Structure

```
churn-analysis/
│
├── data/
│   ├── raw/                          # Original Telco CSV from Kaggle
│   └── processed/clean_churn.csv    # Cleaned & encoded dataset
│
├── notebooks/
│   ├── 01_eda.ipynb                  # Exploratory data analysis
│   ├── 02_feature_engineering.ipynb # Encoding, scaling, null handling
│   ├── 03_model.ipynb               # Logistic regression + evaluation
│   └── 04_insights.ipynb            # Business recommendations
│
├── models/
│   ├── churn_model.pkl              # Trained logistic regression model
│   ├── scaler.pkl                   # StandardScaler
│   └── feature_columns.pkl          # Feature column order for inference
│
├── dashboard/
│   ├── app.py                        # Streamlit dashboard (main entry)
│   └── predict.py                    # Model inference pipeline
│
├── requirements.txt
├── .gitignore
└── README.md
```

---

## 🔍 Key Features

- **EDA** — churn rate breakdown by contract type, tenure, internet service, payment method, and monthly charges
- **Feature Engineering** — label encoding, one-hot encoding, TotalCharges null fix, StandardScaler normalization
- **ML Model** — logistic regression with ROC-AUC evaluation, confusion matrix, and feature importance coefficients
- **Interactive Dashboard** — two tabs: analysis charts + live churn predictor with probability score
- **Business Narrative** — insights framed as actionable retention recommendations

---

## 📊 Dashboard Preview

| Tab | Content |
|-----|---------|
| Analysis | KPI cards, churn by contract/internet/payment, monthly charges distribution |
| Churn Predictor | Input customer details → get churn probability % + risk label |

---

## 🛠️ Tech Stack

| Layer | Tools |
|-------|-------|
| Data manipulation | Python, Pandas, NumPy |
| Visualization | Matplotlib, Seaborn, Plotly |
| Machine Learning | Scikit-learn (LogisticRegression, StandardScaler) |
| Model persistence | Joblib |
| Dashboard | Streamlit |
| Notebook | Jupyter (VS Code) |

---

## ⚙️ Setup & Run Locally

### 1. Clone the repository
```bash
git clone https://github.com/your-username/churn-analysis.git
cd churn-analysis
```

### 2. Create a virtual environment
```bash
python -m venv venv

# Windows
venv\Scripts\activate

# Mac/Linux
source venv/bin/activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Download the dataset
Download the [Telco Customer Churn dataset from Kaggle](https://www.kaggle.com/datasets/blastchar/telco-customer-churn) and place it at:
```
data/raw/WA_Fn-UseC_-Telco.csv
```

### 5. Run the notebooks in order
```
notebooks/01_eda.ipynb
notebooks/02_feature_engineering.ipynb
notebooks/03_model.ipynb
```

This generates `data/processed/clean_churn.csv` and saves the model files under `models/`.

### 6. Run the dashboard
```bash
streamlit run dashboard/app.py
```

The app opens at `http://localhost:8501`

---

## 📓 Notebooks Walkthrough

| Notebook | Description |
|----------|-------------|
| `01_eda.ipynb` | Churn rate (26.5%), distribution by contract/tenure/charges, box plots |
| `02_feature_engineering.ipynb` | Binary encoding, one-hot encoding for Contract/InternetService/PaymentMethod, TotalCharges fix |
| `03_model.ipynb` | Train/test split (80/20), logistic regression, classification report, ROC-AUC, feature importance |

---

## 🔑 Key Findings

1. **Month-to-month contracts** churn at ~43% vs 11% for one-year and 3% for two-year — contract length is the strongest retention lever
2. **Fiber optic customers** churn at ~42% — high charges with dissatisfaction signal
3. **Electronic check users** have the highest churn rate among payment methods (~45%)
4. **Short-tenure customers (0–12 months)** are at highest risk — onboarding experience is critical
5. **Higher monthly charges correlate strongly with churn** — churned customers pay ~$20/month more on average

---

## 💡 Business Recommendations

- Offer **contract upgrade incentives** in month 3–6 (highest churn window)
- Target **fiber optic + electronic check** customers with retention campaigns
- Create an **early warning system** using the churn predictor for customers with score > 60%
- Consider **loyalty discounts** for customers approaching the 12-month mark

---

## 🚀 Deployment

Deployed on **Render** as a web service:

1. Push this repo to GitHub
2. Go to [render.com](https://render.com) → New Web Service → Connect repo
3. Set build command: `pip install -r requirements.txt`
4. Set start command: `streamlit run dashboard/app.py --server.port $PORT --server.address 0.0.0.0`

---

## 📄 Dataset

- **Source:** [Telco Customer Churn — Kaggle](https://www.kaggle.com/datasets/blastchar/telco-customer-churn)
- **Rows:** 7,043 customers
- **Features:** 21 columns including tenure, contract type, internet service, payment method, monthly/total charges
- **Target:** `Churn` (Yes/No)

---

## 👤 Author

**Devendra**
[GitHub](https://github.com/devendra-code-hub) · [LinkedIn](https://linkedin.com/in/your-profile)
