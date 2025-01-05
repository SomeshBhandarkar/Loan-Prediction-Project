from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np

app = FastAPI()
model = joblib.load('RF_loan_prediction_model.pkl')



class LoanPredictionInput(BaseModel):
    CD_Account: int
    Education: int
    CCAvg: float
    Mortgage: float
    Age: int
    Income: float

@app.post("/predict")
def predict_loan(input_data: LoanPredictionInput):
    features = [[
        input_data.CD_Account,
        input_data.Education,
        input_data.CCAvg,
        input_data.Mortgage,
        input_data.Age,
        input_data.Income
    ]]
    prediction = model.predict(features)
    return {"loan_prediction": int(prediction[0])}

@app.get("/")
def read_root():
    return {"message": "Loan Prediction API"}
