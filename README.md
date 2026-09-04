# 📊 Customer Churn & LTV Analysis

### SQL • Python • Machine Learning • Power BI

A data analytics project focused on understanding customer churn, estimating customer lifetime value, identifying high-risk customer segments, and generating actionable business recommendations.

---

## 🎯 Business Problem

Customer churn can negatively impact revenue and long-term customer value.

The objective of this project is to analyze customer churn patterns, identify high-risk customer segments, understand customer value, and provide actionable recommendations for improving customer retention.

### Key Business Questions

- What is the overall customer churn rate?
- Which customer segments have higher churn?
- How does churn vary by contract and service type?
- Which customers represent higher potential lifetime value?
- How can the business improve customer retention?

---

## 📊 Dataset

The project uses a Telco Customer Churn dataset containing customer-level information such as:

- Customer demographics
- Tenure
- Contract type
- Internet service
- Monthly charges
- Total charges
- Churn status

Each row represents an individual customer.

---

## 🛠️ Tools & Technologies

- SQL
- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- Power BI
- Git & GitHub

---

## 🔄 Project Workflow

1. Data Collection
2. Data Understanding
3. Data Cleaning
4. SQL Analysis
5. Exploratory Data Analysis
6. Feature Engineering
7. LTV Analysis
8. Churn Prediction
9. Power BI Dashboard
10. Business Insights & Recommendations

---

## 🧹 Data Cleaning

The dataset was reviewed and prepared before analysis.

Key activities included:

- Checking missing values
- Checking data types
- Identifying inconsistent values
- Preparing numerical and categorical variables
- Preparing the dataset for analysis and modelling

---

## 📈 Exploratory Data Analysis

Python was used to explore customer churn patterns and relationships between churn and different customer attributes.

The analysis included:

- Overall churn distribution
- Churn by contract type
- Churn by internet service
- Monthly charges and churn
- Customer lifetime value analysis

---

## 💰 LTV Analysis

An estimated customer lifetime value metric was created using available customer tenure and monthly charge information.

This analysis helps identify customer segments that may represent higher customer value and therefore may deserve greater retention attention.

> Note: The LTV used in this project is an analytical estimate based on available customer information and is not a full profitability-based Customer Lifetime Value model.

---

## 🤖 Churn Prediction

A machine learning classification model was developed using Python to estimate customer churn risk.

The workflow included:

- Feature preparation
- Train-test split
- Categorical variable encoding
- Model training
- Model evaluation
- Interpretation of model results

Logistic Regression was used as an interpretable baseline classification model.

---

## 📊 Power BI Dashboard

The final analysis was presented through an interactive Power BI dashboard.

The dashboard provides key metrics and visualizations related to:

- Total Customers
- Churn Customers
- Churn Rate
- Average LTV
- Total Charges
- Average Monthly Charges
- Churn by customer segments

### Dashboard Preview

![Customer Churn & LTV Dashboard](screenshots/dashboard.png)

---

## 💡 Key Insights

The analysis helps identify important patterns in customer churn and customer value.

Key areas of focus include:

- Differences in churn across customer segments
- Contract-related churn patterns
- Service-related churn patterns
- Relationship between customer charges and churn
- Higher-value customer segments requiring retention attention

---

## 🚀 Business Recommendations

Based on the analysis, the following actions can be considered:

- Identify customers with higher churn risk.
- Prioritize high-value customers for retention campaigns.
- Investigate customer segments with consistently higher churn.
- Provide targeted offers based on customer characteristics.
- Monitor churn rate and customer value regularly through the Power BI dashboard.

---

## 📁 Project Structure

```text
customer-churn-ltv-prediction/
│
├── data/
│   └── WA_Fn-UseC_-Telco-Customer-Churn.csv
│
├── SQL/
│   └── churn_analysis.sql
│
├── Python_Analysis/
│   ├── 01_data_loading.py
│   ├── 02_data_cleaning_eda.py
│   ├── 03_feature_engineering_ltv.py
│   ├── 04_churn_prediction.py
│   ├── 05_model_insights.py
│   └── analysis_visualizations/
│
├── dashboard/
│   └── Customer_Churn_LTV_Dashboard.pbix
│
├── screenshots/
│   └── dashboard.png
│
├── requirements.txt
└── README.md
