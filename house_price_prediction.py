
# app.py

import streamlit as st
import pandas as pd

from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression

# ---------------------------------------
# Page Configuration
# ---------------------------------------

st.set_page_config(
    page_title="House Price Prediction",
    page_icon="🏠",
    layout="centered"
)

st.title("🏠 House Price Prediction")
st.write("Predict the median house value using Linear Regression.")

# ---------------------------------------
# Load Dataset
# ---------------------------------------

housing = fetch_california_housing(as_frame=True)

df = housing.frame
df.rename(columns={"MedHouseVal": "PRICE"}, inplace=True)

# ---------------------------------------
# Features and Target
# ---------------------------------------

X = df.drop("PRICE", axis=1)
y = df["PRICE"]

# ---------------------------------------
# Train-Test Split
# ---------------------------------------

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# ---------------------------------------
# Scaling
# ---------------------------------------

scaler = StandardScaler()

X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# ---------------------------------------
# Train Model
# ---------------------------------------

model = LinearRegression()
model.fit(X_train_scaled, y_train)

# ---------------------------------------
# Sidebar Inputs
# ---------------------------------------

st.sidebar.header("Enter House Details")

MedInc = st.sidebar.number_input(
    "Median Income",
    value=8.32
)

HouseAge = st.sidebar.number_input(
    "House Age",
    value=41.0
)

AveRooms = st.sidebar.number_input(
    "Average Rooms",
    value=6.98
)

AveBedrms = st.sidebar.number_input(
    "Average Bedrooms",
    value=1.02
)

Population = st.sidebar.number_input(
    "Population",
    value=322.0
)

AveOccup = st.sidebar.number_input(
    "Average Occupancy",
    value=2.55
)

Latitude = st.sidebar.number_input(
    "Latitude",
    value=37.88
)

Longitude = st.sidebar.number_input(
    "Longitude",
    value=-122.23
)

# ---------------------------------------
# Prediction
# ---------------------------------------

input_data = pd.DataFrame(
    [[
        MedInc,
        HouseAge,
        AveRooms,
        AveBedrms,
        Population,
        AveOccup,
        Latitude,
        Longitude
    ]],
    columns=X.columns
)

scaled_input = scaler.transform(input_data)

prediction = model.predict(scaled_input)

st.subheader("Predicted House Price")

st.success(f"${prediction[0] * 100000:.2f}")

# ---------------------------------------
# Show Dataset
# ---------------------------------------

if st.checkbox("Show Dataset"):
    st.dataframe(df)

# ---------------------------------------
# Show Statistics
# ---------------------------------------

if st.checkbox("Show Summary Statistics"):
    st.write(df.describe())

# ---------------------------------------
# Feature Correlation
# ---------------------------------------

if st.checkbox("Show Correlation Matrix"):
    st.write(df.corr())

