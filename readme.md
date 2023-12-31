## Sepsis Prediction FastAPI API 🌡️💻

Welcome to the Sepsis Prediction FastAPI API, where predicting sepsis is just a click away! 🚀 This repository houses a cutting-edge machine learning model built with scikit-learn, wrapped in a FastAPI API that can swiftly analyze health parameters and provide insights into the likelihood of sepsis.
 
 
🛠️ Setup

To embark on this sepsis-predicting journey, make sure you have Docker installed on your machine. Follow these steps:

 
 
1. Clone the repository:
 
    ```bash
    git clone https://github.com/kojoboyoo/Lp6pro.git
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
 
 
Your API will be waiting for you at http://127.0.0.1:8000. Exciting, right?
 
🚀 Endpoints
Home Endpoint
Visit http://127.0.0.1:8000/docs to receive a warm welcome from the Sepsis Prediction App API.
 
Prediction Endpoint
Head over to http://127.0.0.1:8000/docs#/default/predict_predict_post to submit POST requests with health parameters and get predictions in return.
 
📋 Input Data Format

For predictions, send a POST request in JSON format:
```json
{
  "Plasma_glucose": "int",
  "Blood_work1": "int",
  "Blood_Pressure": "int",
  "Blood_work2": "int",
  "Blood_work3": "int",
  "BMI": "float",
  "Blood_work4": "float",
  "Age": "int",
  "Insurance": "int"
}
```

 
## Response Format

The prediction endpoint will return a JSON response with the predicted result:

```json
{
  "prediction": "Positive"
}
```



 docker run sep_results -p 8000:800

 This will start the model on port 8000. You can then access the model's documentation at http://localhost:8000/docs#/default/predict_predict_post.

🧑‍💻 Author
 Enoch Taylor-Nketiah

📰 Article Link
Read more about the deployment process on https://www.linkedin.com/pulse/deploying-api-applications-docker-container-enoch-taylor-nketiah-ziaee/

📸 App Screenshots
<img width="787" alt="Screenshot 2023-12-10 at 4 59 47 PM" src="https://github.com/kojoboyoo/Lp6pro/assets/137324360/5fb4e0c4-6bdf-4c80-ba91-ade7bc14a858">



🚀 Deployed App
Behold the deployed app! http://localhost:8000/docs#/default/predict_predict_post
Also available on Docker Hub https://hub.docker.com/repository/docker/kojoboyoo/sep_results/general. Launch it into the Docker universe! 🌌

