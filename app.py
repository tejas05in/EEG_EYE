import streamlit as st
import pandas as pd
from pycaret.classification import load_model, predict_model
import os
from pathlib import Path


def predict(data):
    best = load_model(
        Path(os.path.join('artifacts\model_trainer', 'best_pipeline')))
    prediction = predict_model(best,  data=data)
    return prediction


# Streamlit app

def main():
    st.title("EEG based EYE Movement Prediction")
    st.image(image='https://images.pexels.com/photos/818563/pexels-photo-818563.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1')

    # File upload section
    st.header("Upload CSV File")
    uploaded_file = st.file_uploader("Choose a CSV file", type=["csv"])

    if uploaded_file is not None:
        # Read the uploaded file
        df = pd.read_csv(uploaded_file)

        # Show the uploaded data
        st.subheader("Uploaded Data")
        st.write(df)

        # Button to trigger predictions
        if st.button("Predict"):
            # Make predictions
            predictions = predict(df)

            # Display predictions as a table
            st.subheader("Predicted Results")
            st.write(predictions)


if __name__ == "__main__":
    main()
