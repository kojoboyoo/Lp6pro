# Sepsis Prediction FastAPI API
 
## Overview
 
This repository contains a FastAPI API for predicting sepsis based on a machine learning model. The model is built using scikit-learn and is available as a joblib pipeline. The API accepts input data related to various health parameters and returns a prediction regarding the likelihood of sepsis.
 
## Setup
 
 
1. Clone the repository:
 
    ```bash
    git clone https://github.com/doeabla/Last_project.git
    cd your-repository
    ```
 
2. Install the required Python packages:
 
    ```bash
    pip install -r requirements.txt
    ```
 
3. Run the FastAPI Server:
    ```bash
    uvicorn main:app --reload
    ```
 
 
The API will be accessible at http://127.0.0.1:8000.
 
## Endpoints
### Home Endpoint
http://127.0.0.1:8000/docs
Provides a welcome message for the Sepsis Prediction App API.
 
### Prediction Endpoint
http://127.0.0.1:8000/predict
Accepts POST requests with input data for sepsis prediction. Returns the prediction result.
 
## Input Data Format
The input data for the prediction endpoint should be sent as a POST request in the JSON format with the following structure:
    ```bash
    {
  "Plasma_glucose": int,
  "Blood_work1": int,
  "Blood_Pressure": int,
  "Blood_work2": int,
  "Blood_work3": int,
  "BMI": float,
  "Blood_work4": float,
  "Age": int,
  "Insurance": int
}
    ```
 
## Response Format
The prediction endpoint will return a JSON response with the predicted result:
    ```bash
    {
  "prediction": "Positive"
}
    ```
 
## Note:
 
Make sure to have Python installed.
Ensure that FastAPI and other dependencies are installed using the provided requirements.txt file.
The API runs on http://127.0.0.1:8000 by default.