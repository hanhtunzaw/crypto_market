import streamlit as st
import pandas as pd
import joblib
import numpy as np

# Load model and encoder
model = joblib.load("crypto_price_model.pkl")
encoder = joblib.load("crypto_encoder.pkl")

# App title
st.title("📈 Crypto Price Predictor")

# Dropdown for coin selection
coin = st.selectbox("Choose a Cryptocurrency:", ["BTC", "ETH", "USDT", "BNB", "SOL"])

# Inputs for features
market_cap = st.number_input("Market Cap (USD)", min_value=0.0, value=500000000.0)
volume = st.number_input("24h Volume (USD)", min_value=0.0, value=100000000.0)
pct_change_24h = st.number_input("24h % Change", value=0.0, format="%.2f")

# Prepare input data
symbol_encoded = encoder.transform([[coin]])
features = np.concatenate((symbol_encoded, [[market_cap, volume, pct_change_24h]]), axis=1)

# Predict button
if st.button("Predict Price"):
    prediction = model.predict(features)[0]
    st.success(f"💰 Estimated Price of {coin}: ${prediction:,.2f}")
