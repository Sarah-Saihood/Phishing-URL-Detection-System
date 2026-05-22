# Phishing URL Detection System

## Overview

This project is a Machine Learning-based phishing URL detection system developed using Python, Flask, and multiple machine learning models.  
The system analyzes URLs and determines whether they are legitimate or phishing websites using layered security checks and machine learning prediction.

---

# Features

- URL structure validation
- HTTPS security checking
- Connection verification
- Blacklist phishing detection
- Whitelist trusted website detection
- Feature extraction from URLs
- Machine Learning prediction
- Multiple ML models comparison
- Professional Flask web interface
- Desktop executable support (.exe)

---

# Technologies Used

- Python 3.9
- Flask
- Scikit-learn
- CatBoost
- NumPy
- Pandas
- Graphviz
- HTML/CSS

---

# Machine Learning Models

The following models are trained and evaluated:

- Random Forest
- Gradient Boosting
- CatBoost

The system automatically selects the best-performing model based on accuracy.

---

# Project Structure

```bash
phishing_detection_project/
│
├── app.py
├── run.py
├── train_model.py
├── feature.py
├── requirements.txt
│
├── modified_phishing_dataset.csv
├── phishing_sites.csv
├── trusted_sites.csv
│
├── pickle/
│   └── model.pkl
│
├── templates/
│   ├── index.html
│   ├── phishing.html
│   ├── trusted.html
│   └── error.html
│
├── diagrams/
│   ├── Digraph.gv
│   ├── diagram.png
│   ├── system_architecture.gv
│   └── system_architecture.png
│
└── dist/
    └── run.exe




System Workflow
1-User enters a URL.
2-URL validation is performed.
3-HTTPS security is checked.
4-Website connectivity is verified.
5-Blacklist and whitelist checks are applied.
6-Features are extracted from the URL.
7-The machine learning model predicts the result.
8-The final result is displayed to the user.




markdown

## How to Run the Project

### 1. Create Virtual Environment

```bash
py -3.9 -m venv venv

## 2. Activate Virtual Environment

venv\Scripts\activate

## 3. Install Requirements

pip install -r requirements.txt

## 4. Train the Machine Learning Model

python train_model.py

## 5. Run the Flask Application

python app.py

## 6. Open the Browser

http://127.0.0.1:5000


##author: Sarah Saihood Abdulrazzq Al-Agele