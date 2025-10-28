import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Sales Dashboard", layout="wide")

st.title("Interactive Sales Performance Dashboard")

@st.cache_data
def load_data():
    # Replace with your actual data loading
    data = pd.DataFrame({
        'Date': pd.to_datetime(['2025-01-01', '2025-01-02', '2025-01-03', '2025-01-04']),
        'Region': ['East', 'West', 'East', 'West'],
        'Sales': [100, 150, 120, 180]
    })
    return data

df = load_data()

st.sidebar.header("Filters")
selected_region = st.sidebar.multiselect("Select Region", options=df['Region'].unique(), default=df['Region'].unique())

filtered_df = df[df['Region'].isin(selected_region)]

col1, col2 = st.columns(2)

with col1:
    st.subheader("Sales Over Time")
    fig = px.line(filtered_df, x='Date', y='Sales', color='Region', title='Daily Sales Trends')
    st.plotly_chart(fig, use_container_width=True)

with col2:
    st.subheader("Sales by Region")
    region_sales = filtered_df.groupby('Region')['Sales'].sum().reset_index()
    fig2 = px.bar(region_sales, x='Region', y='Sales', title='Total Sales by Region')
    st.plotly_chart(fig2, use_container_width=True)

st.subheader("Raw Data")
st.dataframe(filtered_df)
