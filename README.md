# 🏠 House Price Prediction using Linear Regression

## 📌 Project Overview

The **House Price Prediction** project is a Machine Learning application that predicts the price of a house based on various housing features such as median income, house age, average rooms, population, and geographical location.

The project uses the **Linear Regression** algorithm from Scikit-learn and provides an **interactive Streamlit web application** where users can input house details and instantly get the predicted house price.

---

## 🎯 Objective

To build a regression model that predicts house prices using numerical features from a housing dataset and deploy it as a user-friendly web application.

---

## 🚀 Features

* 📊 Interactive Streamlit interface
* 🏠 Predict house prices in real time
* 📋 View the housing dataset
* 📈 Display summary statistics
* 🔍 Explore feature correlations
* 📏 Data preprocessing using StandardScaler
* 🤖 Linear Regression model for prediction
* ⚡ Simple and beginner-friendly implementation

---

## 🛠️ Technologies Used

* Python
* Streamlit
* Pandas
* Scikit-learn
* NumPy

---

## 📂 Project Structure

```
House-Price-Prediction/
│── data/
│   └── housing.csv
│── house_prediction.py
│── house_price_prediction.py
│── README.md
│── requirements.txt
```

---

## 📊 Dataset

This project uses the **California Housing Dataset** provided by **Scikit-learn**.

### Features

| Feature    | Description                |
| ---------- | -------------------------- |
| MedInc     | Median income              |
| HouseAge   | Median age of houses       |
| AveRooms   | Average number of rooms    |
| AveBedrms  | Average number of bedrooms |
| Population | Population in the area     |
| AveOccup   | Average occupancy          |
| Latitude   | Latitude coordinate        |
| Longitude  | Longitude coordinate       |

### Target Variable

* **PRICE** – Predicted median house value

---

## ⚙️ Machine Learning Workflow

1. Load the dataset
2. Split data into features and target
3. Divide data into training and testing sets
4. Normalize features using `StandardScaler`
5. Train the Linear Regression model
6. Make predictions
7. Display predicted house prices through Streamlit

---

## 📥 Installation

### Clone the repository

```bash
git clone https://github.com/your-username/House-Price-Prediction.git
```

### Move to the project directory

```bash
cd House-Price-Prediction
```

### Install dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Run the Application

Start the Streamlit app using:

```bash
python -m streamlit run house_prediction.py
```

The application will open automatically in your default web browser.

---

## 💻 How to Use

1. Launch the Streamlit application.
2. Enter house details from the sidebar:

   * Median Income
   * House Age
   * Average Rooms
   * Average Bedrooms
   * Population
   * Average Occupancy
   * Latitude
   * Longitude
3. View the predicted house price instantly.
4. Optionally:

   * Display the dataset
   * View summary statistics
   * Explore the correlation matrix

---

## 📊 Model

**Algorithm Used:** Linear Regression

The model is trained after:

* Splitting the dataset into training and testing sets
* Normalizing features using `StandardScaler`
* Fitting the data using `LinearRegression()`

---

## 📷 Application Features

* 🏠 House Price Prediction
* 📋 Dataset Viewer
* 📈 Statistical Summary
* 🔗 Correlation Matrix
* ⚡ Fast Predictions with Streamlit

---

## 🎓 Skills Demonstrated

* Data Preprocessing
* Feature Scaling
* Regression Analysis
* Machine Learning Model Training
* Data Visualization
* Streamlit Web Application Development
* Python Programming

---

## 🔮 Future Improvements

* Save the trained model using Joblib
* Add Random Forest and Decision Tree regression models
* Compare multiple algorithms
* Improve UI with charts and visualizations
* Deploy the application online using Streamlit Community Cloud or Render
* Add prediction history and downloadable reports

---

## 👩‍💻 Author

**Kalyani Varpe**

* GitHub: https://github.com/varpekalyani
* LinkedIn: https://linkedin.com/in/kalyani-varpe-7724a6319

---

## 📄 License

This project is developed for educational and learning purposes. You are free to use, modify, and extend it for personal or academic projects.
