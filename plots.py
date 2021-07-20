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
        lc_x = st.selectbox("Select the X-axis for Line chart",('enginesize','horsepower','carwidth','price'))
        lc_y = st.selectbox("Select the Y-axis for Line chart",('enginesize','horsepower','carwidth','price'))
        #st.line_chart(car_df[lc_x])
        #st.write(car_df.index)
        plt.plot(car_df[lc_x],car_df[lc_y])
        st.pyplot()
            
    if 'Area Chart' in plot_list:
        st.subheader("Area Chart")
        ac_x = st.selectbox("Select the X-axis for Area chart",('enginesize','horsepower','carwidth','price'))
        ac_y = st.selectbox("Select the Y-axis for Area chart",('enginesize','horsepower','carwidth','price'))
        #st.area_chart(car_df[ac_x])
        plt.stackplot(car_df[ac_x], car_df[ac_y])
        st.pyplot()

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
