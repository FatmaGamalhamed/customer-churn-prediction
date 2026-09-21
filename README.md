# Customer Churn Prediction

An end-to-end Machine Learning project that predicts whether a customer is likely to churn using the Telco Customer Churn dataset.

## Project Overview

Customer churn prediction helps identify customers who are at risk of leaving a service.

In this project, customer information is analyzed and a Machine Learning classification model is used to predict:

- Whether the customer will churn
- Churn probability
- Customer risk level

The project includes data preprocessing, exploratory data analysis, model training, evaluation, and a FastAPI prediction API connected to a simple web interface.

## Dataset

The project uses the **Telco Customer Churn Dataset**.

- Customers: 7,043
- Features: 19 input features
- Target: `Churn`

The dataset contains information about:

- Customer demographics
- Services
- Contract type
- Payment method
- Monthly charges
- Total charges
- Customer tenure

## Machine Learning

Two classification models were evaluated:

### Logistic Regression

- Accuracy: 80.48%
- Precision: 65.33%
- Recall: 56.42%
- F1 Score: 60.55%
- ROC-AUC: 84.31%

### Random Forest

- Accuracy: 78.85%
- Precision: 63.01%
- Recall: 49.20%
- F1 Score: 55.26%
- ROC-AUC: 81.66%

Logistic Regression was used as the final prediction pipeline based on the evaluation results.

## Data Preprocessing

The preprocessing pipeline includes:

- Converting `TotalCharges` to numeric
- Handling missing values
- Removing `customerID`
- Encoding categorical features using One-Hot Encoding
- Keeping numerical features as numerical values
- Stratified train/test split

## Exploratory Data Analysis

Some of the main patterns observed:

### Churn by Contract

| Contract | Churn Rate |
|---|---:|
| Month-to-month | 42.71% |
| One year | 11.27% |
| Two year | 2.83% |

### Churn by Internet Service

| Internet Service | Churn Rate |
|---|---:|
| Fiber optic | 41.89% |
| DSL | 18.96% |
| No Internet | 7.40% |

These are patterns observed in the dataset and do not imply causation.

## Project Structure

```text
customer-churn-prediction/
│
├── backend/
│   └── app.py
│
├── frontend/
│   ├── index.html
│   ├── style.css
│   └── script.js
│
├── model/
│   └── churn_pipeline.pkl
│
├── requirements.txt
├── .gitignore
└── README.md