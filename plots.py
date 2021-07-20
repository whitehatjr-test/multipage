# S2.1: Design the Page 2 of the multipage app.
# Import necessary modules 
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns

# # Define a function 'app()' which accepts 'car_df' as an input.
def app(car_df):
    st.header('Visualise data')
    
    # Add a multiselect widget with label 'Select the Charts/Plots:'
    # and with 4 options passed as a tuple ('Correlation Heatmap', 'Scatter Plot', 'Box Plot', 'Histogram').
    # Store the current value of this widget in a variable 'plot_list'.
    st.subheader("Visualisation Selector")
    plot_list = st.multiselect("Select the Charts/Plots:",
                               ('Correlation Heatmap', 'Scatter Plot', 'Box Plot', 'Histogram'))

    # Remove deprecation warning 
    st.set_option('deprecation.showPyplotGlobalUse', False)

    # Display correlation heatmap using seaborn module and 'st.pyplot()'
    if 'Correlation Heatmap' in plot_list:
        st.subheader("Correlation Heatmap")
        sns.heatmap(car_df.corr(),annot=True)
        st.pyplot()

    # Display scatter plot
    if 'Scatter Plot' in plot_list:
        st.subheader("Scatter Plot")
        sp_x = st.selectbox("Select the X-axis for Scatter Plot",('enginesize','horsepower','carwidth','price'))
        sp_y = st.selectbox("Select the Y-axis for Scatter Plot",('enginesize','horsepower','carwidth','price'))
        plt.scatter(car_df[sp_x], car_df[sp_y])
        #plt.title("title")
        plt.xlabel(sp_x)
        plt.ylabel(sp_y)
        st.pyplot()

       # Display box plot using seaborn module and 'st.pyplot()'
    if 'Box Plot' in plot_list:
        st.subheader("Box Plot")
        bp = st.selectbox("Select the variable for Box Plot",('enginesize','horsepower','carwidth','drivewheel','price'))
        sns.boxplot(car_df[bp])
        st.pyplot()

    # Display histogram using matplotlib module and 'st.pyplot()'
    if 'Histogram' in plot_list:
        st.subheader("Histogram")
        hg = st.selectbox("Select the variable for Histogram",('enginesize','horsepower','carwidth','drivewheel','price'))
        plt.hist(car_df[hg])
        plt.xlabel(hg)
        plt.ylabel("Frequency")
        st.pyplot()
