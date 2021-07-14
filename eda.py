import numpy as np
import pandas as pd
import streamlit as st


#st.set_page_config(page_title="Car Price Dataset", layout="wide")

def app(car_df):
    st.header("View Data")
    car_df = car_df
    with st.beta_expander("View Dataset"):
        st.table(car_df) 

    st.subheader("Columns Description:")
    c1, c2= st.beta_columns(2)


    if c1.checkbox("Show all column names"):
        c1.table(car_df.columns)

    if c2.checkbox("View column data"):
        column_data = c2.selectbox('Select column',('enginesize','horsepower','carwidth','drivewheel','price'))
        if column_data == 'drivewheel':
            c2.write(car_df['drivewheel'])
        elif column_data == 'carwidth':
            c2.write(car_df['carwidth'])
        elif column_data == 'enginesize':
            c2.write(car_df['enginesize'])
        elif column_data == 'horsepower':
            c2.write(car_df['horsepower'])
        else:
            c2.write(car_df['price'])   


    if st.checkbox("Show summary"):
        st.table(car_df.describe())
    

