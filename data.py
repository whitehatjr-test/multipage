import numpy as np
import pandas as pd
import streamlit as st

def app(car_df):
    st.header("View Data")
    
    with st.beta_expander("View Dataset"):
        
        st.table(car_df)

    st.subheader("Columns Description:")
    c1, c2= st.beta_columns(2)

    with c1:
        if st.checkbox("Show all column names"):
            st.table(car_df.columns)

    with c2:
        if st.checkbox("View column data"):
            column_data = st.selectbox('Select column',('enginesize','horsepower','carwidth','drivewheel','price'))
            if column_data == 'drivewheel':
                st.write(car_df['drivewheel'])
            elif column_data == 'carwidth':
                st.write(car_df['carwidth'])
            elif column_data == 'enginesize':
                st.write(car_df['enginesize'])
            elif column_data == 'horsepower':
                st.write(car_df['horsepower'])
            else:
                st.write(car_df['price'])   


    if st.checkbox("Show summary"):
        st.table(car_df.describe())
    

