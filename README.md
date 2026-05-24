#  Wine Quality Prediction using ML

## Overview

This project predicts whether a wine is **High Quality** or **Low Quality** based on its chemical properties. The project was built to understand the complete machine learning workflow, starting from data analysis and model training to model explainability and API.
Instead of focusing only on achieving a high accuracy score, the goal was to understand the reasoning behind every step, evaluate different models, and build a deployable machine learning application.

---

## Problem Statement

Given the chemical properties of a wine, predict whether it belongs to:
- High Quality Wine
- Low Quality Wine

The original dataset contained wine quality ratings ranging from **3 to 8**. To create a more practical prediction system, the problem was converted into a binary classification task:

| Quality Score | Label |
|--------------|--------|
| < 6 | Low Quality (0) |
| ≥ 6 | High Quality (1) |

---

## Dataset

The dataset contains physicochemical properties of red wine samples.

### Features

- Fixed Acidity
- Volatile Acidity
- Citric Acid
- Residual Sugar
- Chlorides
- Free Sulfur Dioxide
- Total Sulfur Dioxide
- Density
- pH
- Sulphates
- Alcohol

### Target

- Wine Quality

---

## Project Workflow

### 1. Data Exploration

### 2. Exploratory Data Analysis (EDA)

### 3. Model Building

### 4. Model Evaluation

### 5. Hyperparameter Tuning

### 6. Model Explainability


---

## Model Performance

### Final Model

**Random Forest Classifier**

### Binary Classification Results

| Metric | Score |
|----------|----------|
| Accuracy | ~80% |
| Precision | ~80% |
| Recall | ~80% |
| F1 Score | ~80% |

---

## Tech Stack

### Machine Learning

- Python
- Pandas
- NumPy
- Scikit-learn
- SHAP

### Backend

- FastAPI
- Uvicorn
- Pydantic

### Model Persistence

- Joblib

---


## Key Learnings

Through this project, I gained hands-on experience with:

- Data preprocessing
- Exploratory Data Analysis (EDA)
- Feature importance analysis
- Correlation analysis
- Classification algorithms
- Overfitting and underfitting
- Hyperparameter tuning
- Cross-validation
- Explainable AI (SHAP)
- Model serialization
- FastAPI development
- Building and exposing ML models through REST APIs

---

