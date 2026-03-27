import streamlit as st
import numpy as np
import pickle

model = pickle.load(open('model.pkl', 'rb'))

st.title("💳 Credit Card Fraud Detection")

st.write("Enter 30 transaction values:")

input_data = st.text_area("Comma separated values")

if st.button("Predict"):
    try:
        values = list(map(float, input_data.split(',')))

        if len(values) != 30:
            st.warning("⚠️ Enter exactly 30 values")
        else:
            final_input = np.array(values).reshape(1, -1)
            prediction = model.predict(final_input)

            if prediction[0] == 1:
                st.error("🚨 Fraud Transaction")
            else:
                st.success("✅ Normal Transaction")

    except:
        st.error("Invalid input")