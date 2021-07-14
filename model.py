import numpy as np
import pandas as pd
import streamlit as st
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

def app(car_df):
    st.header("Predict")
    car_df = car_df
    st.markdown("""
    Let us predict the price of a car using `Linear Regression`
    """)

    X = car_df.iloc[:, :-1] 

    y = car_df['price']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.3, random_state = 42)
    




# Normalise only the numeric columns.
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



# Create a function 'prediction()' which accepts SepalLength, SepalWidth, PetalLength, PetalWidth as input and returns species name.
    def prediction(engine_size, horse_power, car_width, drive_wheel):
        price = lin_reg.predict([[engine_size, horse_power, car_width, drive_wheel]])
        price = price[0]
        return price


    c1, c2 = st.beta_columns((2,2))
    with c1:
        inputs = st.beta_container()
        inputs.subheader("Select Values:")
    # Add 4 sliders and store the value returned by them in 4 separate variables. 
        es = inputs.slider("Engine Size", int(car_df["enginesize"].min()), int(car_df["enginesize"].max()))
        hp = inputs.slider("Horse Power", int(car_df["horsepower"].min()), int(car_df["horsepower"].max()))
        cw = inputs.slider("Car Width", float(car_df["carwidth"].min()), float(car_df["carwidth"].max()))

        dw = inputs.radio("Drive Wheel",("rwd", "fwd", "4wd"))
        if dw == 'rwd':
            dw = 0
        elif dw == 'fwd':
            dw = 1
        else:
            dw = '4wd'

        my_button = inputs.button("Predict")

    with c2:
        st.subheader("Prediction results with evaluation metrics:")
        if my_button:

            price = prediction(es, hp, cw, dw)
            st.write("The predicted price of the car:", int(price))
            st.write("Accuracy score of this model is:", round(score,2))