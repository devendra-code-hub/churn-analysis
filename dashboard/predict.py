# dashboard/predict.py
import joblib
import numpy as np
import pandas as pd
import os


# 1. Get the directory that predict.py lives in (C:\DataAnalyst\churn-analysis\dashboard)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# 2. Go one level up to the project root folder (C:\DataAnalyst\churn-analysis)
# (Skip this step if your 'models' folder is actually INSIDE the dashboard folder!)
PROJECT_ROOT = os.path.dirname(BASE_DIR)

# 3. Construct the bulletproof path to your model
MODEL_PATH = os.path.join(PROJECT_ROOT, "models", "churn_model.pkl")

# 4. Load it up safely
model = joblib.load(MODEL_PATH)

# model   = joblib.load("models/churn_model.pkl")
scaler  = joblib.load(MODEL_PATH)
columns = joblib.load(MODEL_PATH)

def predict_churn(input_dict):
    df = pd.DataFrame([input_dict])
    df = df.reindex(columns=columns, fill_value=0)
    scaled = scaler.transform(df)
    prob = model.predict_proba(scaled)[0][1]
    label = "High Risk" if prob > 0.5 else "Low Risk"
    return round(prob * 100, 1), label