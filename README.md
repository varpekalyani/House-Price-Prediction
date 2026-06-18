# 🏠 House Price Prediction using Machine Learning

## 📌 Project Overview

This project focuses on predicting house prices using Machine Learning techniques. The objective is to analyze housing data, identify the factors that influence property prices, and build predictive models capable of estimating house values accurately.

The project was completed as part of a Machine Learning Internship assignment and covers the complete data science workflow, including data exploration, cleaning, visualization, model building, evaluation, and business insights.

---

## 🎯 Problem Statement

Real estate buyers and sellers often struggle to estimate a property's fair value accurately. This project aims to develop a machine learning model that predicts house prices based on various property features such as area, bedrooms, bathrooms, parking availability, furnishing status, and other amenities.

---

## 📂 Dataset

Dataset: Housing Prices Dataset

The dataset contains information about residential properties, including:

* Price (Target Variable)
* Area
* Bedrooms
* Bathrooms
* Stories
* Main Road Access
* Guest Room Availability
* Basement Availability
* Hot Water Heating
* Air Conditioning
* Parking
* Preferred Area
* Furnishing Status

---

## 🛠️ Technologies Used

* Python 3
* Jupyter Notebook
* Pandas
* NumPy
* Scikit-learn
* Matplotlib
* Seaborn

---

## 📋 Project Tasks

### Task 1: Data Loading & Exploration

* Loaded dataset using Pandas
* Displayed first 10 records
* Checked dataset dimensions
* Identified target and feature columns
* Checked missing values

### Task 2: Data Cleaning

* Removed duplicate records
* Handled missing values
* Applied One-Hot Encoding to categorical features
* Prepared dataset for machine learning

### Task 3: Model Building

Two regression models were implemented:

#### Linear Regression

* Trained using 80/20 train-test split
* Evaluated using MAE, RMSE, and R² Score

#### Random Forest Regressor

* Trained and evaluated on the same dataset
* Compared performance against Linear Regression

### Task 4: Data Visualization

Generated visualizations including:

* House Price Distribution Histogram
* Correlation Heatmap
* Actual vs Predicted Price Scatter Plot

### Task 5: Insights & Summary

* Identified key features influencing house prices
* Compared model performance
* Derived business recommendations

---

## 📊 Evaluation Metrics

The models were evaluated using:

* Mean Absolute Error (MAE)
* Root Mean Squared Error (RMSE)
* R² Score

These metrics help measure prediction accuracy and model performance.

---

## 📈 Key Findings

* Property area was one of the strongest indicators of house price.
* Amenities such as air conditioning and preferred area significantly impacted pricing.
* Random Forest Regressor outperformed Linear Regression in predictive accuracy.
* Location and property features play a major role in determining market value.

---

## 📁 Project Structure

```text
HousePricePrediction/

├── analysis.ipynb
├── Housing.csv
├── charts/
│   ├── price_distribution.png
│   ├── correlation_heatmap.png
│   └── actual_vs_predicted.png
├── summary.pdf
├── requirements.txt
└── README.md
```

## 🚀 How to Run

1. Clone the repository

```bash
git clone <repository-url>
```

2. Navigate to the project folder

```bash
cd HousePricePrediction
```

3. Install dependencies

```bash
pip install -r requirements.txt
```

4. Open and run

```bash
jupyter notebook analysis.ipynb
```

---

## 👩‍💻 Author

Kalyani Varpe

Machine Learning Internship Project
