# Copyright (c) 2025 Kemar Christie
# Authors: Kemar Christie

from fastapi import FastAPI
import pickle
import numpy as np

app = FastAPI()
model = pickle.load(open("local_ml_model.pkl", "rb"))

@app.get("/")
def root():
    return {"message": "API is live"}

@app.post("/predict")
def predict(features: list[float]):
    prediction = model.predict([features])
    print(f"Prediction: {prediction[0]}, Type: {type(prediction[0])}")
    return {"prediction": int(prediction[0])}