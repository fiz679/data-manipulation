import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(
    page_title="Data Manipulation Using Pandas",
    page_icon="📊",
    layout="wide"
)

st.title("📊 Data Manipulation Using Pandas")
st.markdown("Upload a CSV file to perform data analysis and visualization.")

uploaded_file = st.file_uploader(
    "Upload CSV File",
    type=["csv"]
)

if uploaded_file is not None:

    try:
        df = pd.read_csv(uploaded_file)

        st.success("Dataset uploaded successfully!")

        st.subheader("Dataset Preview")
        st.dataframe(df, use_container_width=True)

        st.subheader("Dataset Information")

        col1, col2, col3 = st.columns(3)

        col1.metric("Rows", df.shape[0])
        col2.metric("Columns", df.shape[1])
        col3.metric("Missing Values", int(df.isnull().sum().sum()))

        st.subheader("Column Data Types")
        st.write(df.dtypes)

        st.subheader("Summary Statistics")
        st.write(df.describe(include="all"))

        st.subheader("Missing Values")
        st.write(df.isnull().sum())

        st.subheader("Duplicate Rows")
        st.write(f"Duplicate Rows: {df.duplicated().sum()}")

        st.subheader("Filter Dataset")

        filtered_df = df.copy()

        for column in filtered_df.columns:
            if filtered_df[column].dtype == "object":
                values = st.multiselect(
                    f"Filter {column}",
                    filtered_df[column].dropna().unique()
                )

                if values:
                    filtered_df = filtered_df[
                        filtered_df[column].isin(values)
                    ]

        st.subheader("Filtered Dataset")
        st.dataframe(filtered_df, use_container_width=True)

        if "Sales" in filtered_df.columns:

            st.subheader("Sales Analysis")

            c1, c2, c3 = st.columns(3)

            c1.metric("Total Sales", int(filtered_df["Sales"].sum()))
            c2.metric("Average Sales", round(filtered_df["Sales"].mean(), 2))
            c3.metric("Maximum Sales", int(filtered_df["Sales"].max()))

            if "Store" in filtered_df.columns:

                st.subheader("Sales by Store")

                sales_store = (
                    filtered_df
                    .groupby("Store")["Sales"]
                    .sum()
                )

                st.bar_chart(sales_store)

            if "Month" in filtered_df.columns:

                st.subheader("Monthly Sales")

                sales_month = (
                    filtered_df
                    .groupby("Month")["Sales"]
                    .sum()
                )

                st.line_chart(sales_month)

        st.subheader("Download Filtered Dataset")

        csv = filtered_df.to_csv(index=False).encode("utf-8")

        st.download_button(
            label="Download CSV",
            data=csv,
            file_name="filtered_data.csv",
            mime="text/csv"
        )

    except Exception as e:
        st.error(f"Error: {e}")

else:
    st.info("Please upload a CSV file to begin.")