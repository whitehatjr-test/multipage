import streamlit as st
import eda
import plots
import model
import numpy as np
import pandas as pd





PAGES = {
	"View Data": eda,
    "Visualise Data": plots,
    "Predict": model
}

st.set_option('deprecation.showPyplotGlobalUse', False)

@st.cache(persist=True)
def load_data():
# Read the dataset
    df = pd.read_csv("https://student-datasets-bucket.s3.ap-south-1.amazonaws.com/whitehat-ds-datasets/car-prices.csv")

# Extract the name of the manufactures from the car names and display the first 25 cars to verify whether names are extracted successfully.
    car_companies = pd.Series([car.split(" ")[0] for car in df['CarName']], index = df.index)

# Create a new column named 'car_company'. It should store the company names of a the cars.
    df['car_company'] = car_companies



    df = df[['enginesize','horsepower','carwidth','drivewheel','price']]

    df['drivewheel'] = df['drivewheel'].map({'rwd': 0, 'fwd': 1, '4wd':2})
    
         

        
    return df

    
car_df = load_data()

st.title("Welcome to Car Price Prediction App")
st.sidebar.title('Navigation')
selection = st.sidebar.radio("Go to", list(PAGES.keys()))
page = PAGES[selection]
page.app(car_df)