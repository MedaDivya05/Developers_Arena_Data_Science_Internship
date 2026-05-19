# 📊 Week 10 - Customer Churn Prediction using Data Preprocessing & Feature Engineering

## 📌 Project Overview

This project was completed as part of Week 10 of the Data Science Online Internship at The Developers Arena.

The objective of this project is to build a complete customer churn prediction pipeline by applying advanced data preprocessing and feature engineering techniques. The project focuses on preparing raw customer data for machine learning, engineering meaningful features, handling categorical variables, scaling numerical features, detecting outliers, and building an end-to-end preprocessing pipeline.

The project demonstrates a real-world machine learning preprocessing workflow including:

- Data Cleaning
- Categorical Encoding
- Feature Scaling
- Outlier Detection & Handling
- Feature Engineering
- Feature Selection
- Pipeline Creation
- Churn Prediction Modeling

This project helps understand the importance of preprocessing and feature engineering in improving machine learning model performance.

---

# 🎯 Objectives

- Understand data preprocessing techniques
- Apply multiple encoding methods
- Perform feature scaling
- Detect and handle outliers
- Create engineered business features
- Build preprocessing pipelines
- Train customer churn prediction model
- Analyze preprocessing impact on machine learning

---

# 🛠️ Technologies Used

- Python 3
- Google Colab
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn

---

# 📂 Project Structure

```bash
Week-10-Customer-Churn-Prediction/
│── README.md
│── churn_prediction_pipeline.ipynb
│── customer_churn.csv
│── preprocessing_report.md
│── visualizations/
│   ├── churn_distribution.png
│   ├── outlier_boxplots.png
│   ├── correlation_heatmap.png
│   ├── confusion_matrix.png
│   └── feature_analysis.png
```

---

# ⚙️ Setup Instructions

## Google Colab (Recommended)

1. Open Google Colab
2. Upload the customer churn dataset
3. Run notebook cells step by step
4. Save visualizations and reports

---

# 📁 Dataset Information

Dataset Used:

- customer_churn.csv

---

## Dataset Description

The dataset contains customer subscription and churn information.

### Features Included

- CustomerID
- Tenure
- MonthlyCharges
- TotalCharges
- Contract
- PaymentMethod
- PaperlessBilling
- SeniorCitizen
- Churn

---

## Dataset Summary

| Attribute | Value |
|----------|------|
| Rows | 500 |
| Columns | 9 |

---

# 📊 Data Preprocessing Workflow

## 1. Data Cleaning

Performed:

- Missing value handling
- Duplicate record removal
- Data type conversion
- Invalid value handling

---

## 2. Categorical Encoding

Three different encoding methods were implemented.

### Label Encoding

Used for binary and ordinal-style categorical variables.

### One-Hot Encoding

Used for nominal categorical variables such as payment methods.

### Ordinal Encoding

Used for ordered categorical features.

---

## 3. Feature Scaling

Two scaling techniques were applied.

### Standard Scaling

Used to standardize numerical features.

### Min-Max Scaling

Used to normalize values within a fixed range.

---

## 4. Outlier Detection & Handling

Outliers were identified using:

- IQR Method
- Boxplots

Outliers were handled using capping techniques.

---

## 5. Feature Engineering

More than five engineered features were created.

### Engineered Features

- Customer_Lifetime_Value
- Avg_Revenue_Per_Tenure
- Tenure_Group
- Monthly_Charge_Category
- Contract_Risk
- Digital_Billing_Flag
- High_Value_Customer

These features improved business understanding and machine learning performance.

---

## 6. Feature Selection

Correlation analysis and business understanding were used to identify important features.

---

## 7. Preprocessing Pipeline

A complete preprocessing pipeline was created using:

- ColumnTransformer
- Pipeline
- StandardScaler
- OneHotEncoder

This ensured automated and reusable preprocessing.

---

# 🤖 Machine Learning Model

A Logistic Regression model was trained using the preprocessed dataset.

### Steps Performed

- Train-test split
- Pipeline integration
- Model training
- Prediction generation
- Evaluation

---

# 📈 Evaluation Metrics

The following metrics were used to evaluate the model:

## 1. Accuracy Score

Measures overall prediction accuracy.

## 2. Classification Report

Includes:

- Precision
- Recall
- F1-score

## 3. Confusion Matrix

Used to visualize prediction performance.

---

# 📊 Visualizations Created

The project includes multiple visualizations.

---

## 1️⃣ Customer Churn Distribution

Shows churn vs non-churn customers.

---

## 2️⃣ Outlier Detection Boxplots

Visualizes outliers in numerical columns.

---

## 3️⃣ Correlation Heatmap

Shows relationships between numerical variables.

---

## 4️⃣ Confusion Matrix

Displays model prediction performance.

---

## 5️⃣ Feature Analysis

Shows engineered feature patterns and business insights.

---

# 📈 Key Findings

- Month-to-month customers showed higher churn risk.
- Customers with shorter tenure were more likely to churn.
- Feature engineering improved predictive understanding.
- Preprocessing pipelines simplified machine learning workflow.
- Scaling and encoding improved model compatibility.

---

# 📸 Screenshots

Recommended screenshots:

- Dataset preview
- Churn distribution chart
- Outlier boxplots
- Correlation heatmap
- Encoded dataset preview
- Scaling output
- Confusion matrix
- Final churn prediction report

---

# 💼 Business Insights

- High-risk customers can be identified early using preprocessing techniques.
- Customer lifetime value helps identify valuable customers.
- Tenure-based segmentation supports retention planning.
- Feature engineering improves customer behavior understanding.
- Predictive analytics can help reduce customer churn.

---

# 🚀 Future Improvements

- Use advanced machine learning models
- Perform hyperparameter tuning
- Add feature importance visualization
- Create real-time prediction dashboard
- Deploy model using Streamlit or Flask
- Integrate automated preprocessing pipelines

---

# 📦 Deliverables

The project includes:

- Churn Prediction Notebook
- Preprocessing Report
- Feature Engineering Documentation
- Visualizations
- Requirements File
- Portfolio-ready Documentation

---

# 🧪 Testing Evidence

| Test Case | Expected Result | Status |
|----------|----------------|-------|
| Dataset Loading | Dataset loads successfully | Passed |
| Data Cleaning | Missing values handled correctly | Passed |
| Encoding Methods | Encoding applied successfully | Passed |
| Scaling Techniques | Features scaled correctly | Passed |
| Outlier Handling | Outliers handled successfully | Passed |
| Feature Engineering | Engineered features created | Passed |
| Pipeline Creation | Preprocessing pipeline built successfully | Passed |
| Model Training | Logistic Regression trained successfully | Passed |
| Visualizations | Charts displayed successfully | Passed |

---

# 📚 Learning Outcomes

Through this project, I learned how to preprocess raw datasets for machine learning applications using advanced preprocessing and feature engineering techniques. I gained practical experience in encoding, scaling, outlier handling, feature creation, pipeline automation, and churn prediction modeling.

This project strengthened my understanding of:

- Data Preprocessing
- Feature Engineering
- Machine Learning Pipelines
- Data Cleaning
- Feature Scaling
- Categorical Encoding
- Predictive Analytics
- Business Interpretation of ML Models

---

# ✅ Conclusion

The Week 10 Customer Churn Prediction project successfully demonstrates a complete data preprocessing and feature engineering workflow for machine learning applications. The project combines preprocessing, feature engineering, pipeline creation, and predictive modeling to solve a real-world customer churn problem.

This project strengthened practical skills required for Data Science, Machine Learning, and Predictive Analytics roles.
