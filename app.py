import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="Data Manipulation Using Pandas", layout="wide")

st.title("📊 Data Manipulation Using Pandas")

uploaded_file = st.file_uploader(
    "Upload CSV File",
    type=["csv"]
)

if uploaded_file is not None:

    df = pd.read_csv(uploaded_file)

    st.header("Dataset")
    st.dataframe(df)

    st.header("Dataset Information")

    col1, col2 = st.columns(2)

    with col1:
        st.write("Rows :", df.shape[0])
        st.write("Columns :", df.shape[1])

    with col2:
        st.write(df.dtypes)

    st.header("Summary Statistics")
    st.write(df.describe())

    st.header("Filter Data")

    month = st.selectbox(
        "Select Month",
        ["All"] + list(df["Month"].unique())
    )

    if month != "All":
        df = df[df["Month"] == month]

    store = st.selectbox(
        "Select Store",
        ["All"] + list(df["Store"].unique())
    )

    if store != "All":
        df = df[df["Store"] == store]

    st.dataframe(df)

    st.header("Sales Summary")

    st.metric("Total Sales", int(df["Sales"].sum()))
    st.metric("Average Sales", round(df["Sales"].mean(),2))

    st.header("Bar Chart")

    st.bar_chart(df.set_index("Store")["Sales"])

    st.header("Line Chart")

    chart = df.groupby("Month")["Sales"].sum()

    st.line_chart(chart)

else:
    st.info("Upload a CSV file to begin.")