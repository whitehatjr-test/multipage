import streamlit as st
import numpy as np
import pandas as pd

import data
import plots
import predict


@st.cache()
def load_data():
    # Read the dataset
    df = pd.read_csv("https://student-datasets-bucket.s3.ap-south-1.amazonaws.com/whitehat-ds-datasets/car-prices.csv")


    df = df[['enginesize','horsepower','carwidth','drivewheel','price']]

    df['drivewheel'] = df['drivewheel'].map({'rwd': 0, 'fwd': 1, '4wd':2})   
                 
    return df

    
car_df = load_data()

st.title("Welcome to Car Price Prediction App")

with st.beta_expander("Watch Video"):
    st.write("You can learn how to host a Streamlit app on Heroku by watching this video:")
    st.video("https://youtu.be/oBA5I__AfmY")

PAGES = {
    "View Data": data,
    "Visualise Data": plots,
    "Predict": predict
}

st.sidebar.title('Navigation')
selection = st.sidebar.radio("Go to", list(PAGES.keys()))
page = PAGES[selection]
page.app(car_df)
