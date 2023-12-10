# Sepsis Prediction FastAPI API
 
## Overview
 
This repository contains a FastAPI API for predicting sepsis based on a machine learning model. The model is built using scikit-learn and is available as a joblib pipeline. The API accepts input data related to various health parameters and returns a prediction regarding the likelihood of sepsis.
 
## Setup
To run the sepsis prediction model, you will need to have Docker installed on your machine. Once you have Docker installed, you can run the following command to start the model:



 docker run sep_results -p 8000:800

 This will start the model on port 8000. You can then access the model's documentation at http://localhost:8000/docs#/default/predict_predict_post.

Author
 Enoch Taylor-Nketiah

Article Link
 Deploying API Applications in Docker Containers

App Screenshots
 ![Uploading Screenshot 2023-12-06 at 3.33.20 PM.png…]()


www.computerbild.de
app screenshot 1
Deployed App Link
 http://localhost:8000/docs#/default/predict_predict_post