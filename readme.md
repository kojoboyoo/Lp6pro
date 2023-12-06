# Sepsis Prediction Model

## Introduction

Sepsis is a life-threatening medical condition that arises when the body's response to infection causes widespread inflammation, leading to organ dysfunction. Early detection of sepsis is critical for timely intervention and improved patient outcomes. In the context of an Intensive Care Unit (ICU), where patients are already vulnerable, the ability to predict the likelihood of sepsis can be a game-changer. This project aims to leverage machine learning techniques to create a predictive model that can identify patients at risk of developing sepsis based on their medical details.

## Problem Statement
Despite advances in medical technology, sepsis remains a major challenge in ICUs, with its rapid onset and diverse clinical presentations. Early identification of sepsis is often difficult, leading to delayed interventions and increased mortality rates. This project addresses the need for a reliable and timely predictive model to assist healthcare professionals in identifying ICU patients who are at a higher risk of developing sepsis.

## Setup
To run the sepsis prediction model, you will need to have Docker installed on your machine. Once you have Docker installed, you can run the following command to start the model:

Use code with caution. Learn more

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