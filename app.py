import streamlit as st
import pickle
import numpy as np

# Load model
with open(r'C:\Users\manoh\OneDrive\Desktop\Sales Deploy\linear_model.pkl', 'rb') as f:
    model = pickle.load(f)

# Page config
st.set_page_config(page_title="Sales Predictor", layout="centered")

# Title
st.markdown("<h1 style='text-align: center; color: green;'>📊 Sales Prediction App</h1>", unsafe_allow_html=True)

st.write("### Enter advertising budget to predict sales")

# Inputs
col1, col2, col3 = st.columns(3)

with col1:
    tv = st.number_input("📺 TV Budget", min_value=0.0)

with col2:
    radio = st.number_input("📻 Radio Budget", min_value=0.0)

with col3:
    newspaper = st.number_input("📰 Newspaper Budget", min_value=0.0)

# Button
if st.button("🚀 Predict Sales"):
    input_data = np.array([[tv, radio, newspaper]])
    prediction = model.predict(input_data)

    st.success(f"💰 Predicted Sales: {prediction[0]:.2f}")