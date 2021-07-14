import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns

def app(car_df):
    st.header('Visualise data')
    
    car_df =car_df

    st.subheader("Visualisation Selector")
    plot_list = st.multiselect("Select the Charts/Plots:",('Correlation Heatmap', 'Line Chart', 'Area Chart', 'Box Plot', 'Histogram'))
      
    st.set_option('deprecation.showPyplotGlobalUse', False)


    if 'Correlation Heatmap' in plot_list:
        st.subheader("Correlation Heatmap")
        sns.heatmap(car_df.corr(),annot=True)
        st.pyplot()

    if 'Line Chart' in plot_list:
        st.subheader("Line Chart")
        lc = st.selectbox("Select the variable for Line chart",('enginesize','horsepower','carwidth','drivewheel','price'))
        st.line_chart(car_df[lc])
            
    if 'Area Chart' in plot_list:
        st.subheader("Area Chart")
        ac = st.selectbox("Select the variable for Area chart",('enginesize','horsepower','carwidth','drivewheel','price'))
        st.area_chart(car_df[ac])


    if 'Box Plot' in plot_list:
        st.subheader("Box Plot")
        bp = st.selectbox("Select the variable for boxplot",('enginesize','horsepower','carwidth','drivewheel','price'))
        sns.boxplot(car_df[bp])
        st.pyplot()

    if 'Histogram' in plot_list:
        st.subheader("Histogram")
        hg = st.selectbox("Select the variable for histogram",('enginesize','horsepower','carwidth','drivewheel','price'))
        plt.hist(car_df[hg])
        st.pyplot()