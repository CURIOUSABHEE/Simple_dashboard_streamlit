import streamlit as st
import pandas as pd


st.title("Dashboard App")


uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

if uploaded_file is not None:
    st.write("Your File is Uploaded....")
    df = pd.read_csv(uploaded_file)

    st.write(df.head())

    st.subheader("Data Summary")
    st.write(df.describe())


    columns = df.columns.tolist()
    selected_columns = st.selectbox("Select Columns", columns)
    uniques_values = df[selected_columns].unique()
    selected_values = st.selectbox("Select Values", uniques_values)
    filtered_data = df[df[selected_columns] == selected_values]
    st.write(filtered_data)

    st.subheader("Data Visualization")
    x_columns = st.selectbox("X Axis", columns)
    y_columns = st.selectbox("Y Axis", columns)

    if st.button("Generate Plot"):
        st.line_chart(filtered_data.set_index(x_columns)[ y_columns] )
else :
    st.write("Please Upload a File")
