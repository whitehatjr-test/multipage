import numpy as np
import pandas as pd
import streamlit as st
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

def app(car_df): 

    X = car_df.iloc[:, :-1] 

    y = car_df['price']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.3, random_state = 42) 


    # Normalise the numeric columns.
    def standard_norm(series):
        series_mean = series.mean()
        series_std = series.std()
        new_series = (series - series_mean) / series_std
        return new_series

    X_train[X_train.columns] = X_train[X_train.columns].apply(standard_norm, axis = 0)
    X_test[X_test.columns] = X_test[X_test.columns].apply(standard_norm, axis = 0)

    # Creating the linear regression model and storing the accuracy score in a variable 'score'
    lin_reg = LinearRegression()
    lin_reg.fit(X_train, y_train)
    score = lin_reg.score(X_train, y_train)



    # Create a function 'prediction()' which accepts engine_size, horse_power, car_width, drive_wheel as input and returns car price.
    @st.cache()
    def prediction(engine_size, horse_power, car_width, drive_wheel):
        price = lin_reg.predict([[engine_size, horse_power, car_width, drive_wheel]])
        price = price[0]
        return price

    
    
    st.markdown("<p style='color:blue;font-size:25px'>This app uses <b>Linear regression</b> to predict the price of a car based on your inputs.", unsafe_allow_html=True)

    st.subheader("Select Values:")
    # Add 4 sliders and store the value returned by them in 4 separate variables. 
    es = st.slider("Engine Size", int(car_df["enginesize"].min()), int(car_df["enginesize"].max()))
    hp = st.slider("Horse Power", int(car_df["horsepower"].min()), int(car_df["horsepower"].max()))
    cw = st.slider("Car Width", float(car_df["carwidth"].min()), float(car_df["carwidth"].max()))

    dw = st.radio("Drive Wheel",("rwd", "fwd", "4wd"))
    if dw == 'rwd':
        dw = 0
    elif dw == 'fwd':
        dw = 1
    else:
        dw = '4wd' 

    
    if st.button("Predict"):
        st.subheader("Prediction results:")
        price = prediction(es, hp, cw, dw)
        st.write("The predicted price of the car: {:,}".format(int(price)))

        st.write("Accuracy score of this model is:", round(score,2))
