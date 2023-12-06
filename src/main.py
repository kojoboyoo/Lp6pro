# Import necessary libraries and modules
from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np
import os
import pandas as pd
from typing import Union,Optional

# Load pre-trained machine learning model and label encoder


file_path_pipeline= os.path.abspath("dev/logpipelinebal.joblib")
file_path_label = os.path.abspath("dev/labelencoderbal.joblib")

pipeline = joblib.load(file_path_pipeline)
encoder = joblib.load(file_path_label)

# Create a FastAPI instance
app = FastAPI()

# Define a Pydantic model for input data
class InputData(BaseModel):
    PRG: int
    PL: int
    PR: int
    SK: int
    TS: int
    M11: float
    BD2: float
    Age: int
    Insurance: int

# Define a Pydantic model for the prediction result
class PredictionResult(BaseModel):
    pprediction: str  

# Define a route for the root endpoint
@app.get("/")
def sephome():
    # Return a simple message for the root endpoint
    return "New Sepsis Prediction app"

# Define a route for the prediction endpoint with HTTP POST method
@app.post("/predict", response_model=PredictionResult)

def predict(data: InputData):

    try:
        # Create a DataFrame using the fields from InputData
        df = pd.DataFrame([data.dict()])

        # Make predictions using the pre-trained model
        predicted_data = pipeline.predict(df)

        # Decode the predicted data using the label encoder
        decoded_data = encoder.inverse_transform(predicted_data)

        # Return the prediction result in the specified format
        return PredictionResult(pprediction=decoded_data[0])  

    # Handle a specific type of error (ValueError) with a custom response
    except ValueError as ve:
        return PredictionResult(pprediction=None, error=f"ValueError: {str(ve)}")

    # Handle other types of exceptions with a custom response
    except Exception as e:
        return PredictionResult(pprediction=None, error=f"Internal Server Error: {str(e)}")
