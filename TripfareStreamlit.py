import streamlit as st
import pandas as pd
import numpy as np
import joblib
from datetime import datetime

# -----------------------------------
# Load trained model
# -----------------------------------
model = joblib.load('taxi_fare_model.pkl')

# -----------------------------------
# App UI
# -----------------------------------
st.set_page_config(page_title="TripFare Predictor", layout="centered")

st.title("🚕 TripFare: Taxi Fare Prediction App")
st.write("Predict total taxi fare using trip details")

# -----------------------------------
# User Inputs
# -----------------------------------
st.header("Enter Trip Details")

passenger_count = st.number_input("Passenger Count", min_value=1, max_value=6, value=1)

trip_distance_km = st.number_input("Trip Distance (km)", min_value=0.1, value=2.0)

trip_duration_min = st.number_input("Trip Duration (minutes)", min_value=1.0, value=10.0)

pickup_hour = st.slider("Pickup Hour", 0, 23, 10)

is_night = 1 if pickup_hour >= 22 or pickup_hour <= 5 else 0
is_pm = 1 if pickup_hour >= 12 else 0
is_weekend = 0  # dataset has only weekdays

tip_amount = st.number_input("Tip Amount", min_value=0.0, value=1.0)
tolls_amount = st.number_input("Tolls Amount", min_value=0.0, value=0.0)
extra = st.number_input("Extra Charges", min_value=0.0, value=0.0)
mta_tax = 0.5
improvement_surcharge = 0.3

store_and_fwd_flag = 0

# -----------------------------------
# Build input dataframe
# -----------------------------------
input_data = {
    'passenger_count': passenger_count,
    'trip_distance_km': trip_distance_km,
    'trip_duration_min': trip_duration_min,
    'pickup_hour': pickup_hour,
    'pickup_day': 1,
    'is_weekend': is_weekend,
    'is_pm': is_pm,
    'is_night': is_night,
    'tip_amount': tip_amount,
    'tolls_amount': tolls_amount,
    'extra': extra,
    'mta_tax': mta_tax,
    'improvement_surcharge': improvement_surcharge,
    'store_and_fwd_flag': store_and_fwd_flag
}

input_df = pd.DataFrame([input_data])

# -----------------------------------
# Align input with model features
# -----------------------------------
model_features = model.feature_names_in_

for col in model_features:
    if col not in input_df.columns:
        input_df[col] = 0

input_df = input_df[model_features]

# -----------------------------------
# Prediction
# -----------------------------------
if st.button("Predict Fare 💰"):
    prediction = model.predict(input_df)[0]
    st.success(f"Estimated Total Fare: ₹ {prediction:.2f}")
