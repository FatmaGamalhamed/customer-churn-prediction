from pathlib import Path
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from pydantic import BaseModel
import joblib
import pandas as pd

BASE_DIR = Path(__file__).resolve().parent.parent

app = FastAPI(title="Customer Churn Prediction API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

model = joblib.load(BASE_DIR / "model" / "churn_pipeline.pkl")


class CustomerData(BaseModel):
    gender: str
    SeniorCitizen: int
    Partner: str
    Dependents: str
    tenure: int
    PhoneService: str
    MultipleLines: str
    InternetService: str
    OnlineSecurity: str
    OnlineBackup: str
    DeviceProtection: str
    TechSupport: str
    StreamingTV: str
    StreamingMovies: str
    Contract: str
    PaperlessBilling: str
    PaymentMethod: str
    MonthlyCharges: float
    TotalCharges: float


@app.get("/")
def home():
    return FileResponse(BASE_DIR / "frontend" / "index.html")


@app.post("/predict")
def predict(data: CustomerData):
    input_data = pd.DataFrame([data.model_dump()])

    prediction = model.predict(input_data)[0]
    probability = model.predict_proba(input_data)[0][1]

    if probability < 0.30:
        risk = "Low"
    elif probability < 0.60:
        risk = "Medium"
    else:
        risk = "High"

    return {
        "churn_prediction": "Yes" if prediction == 1 else "No",
        "churn_probability": round(float(probability), 4),
        "risk_level": risk
    }
