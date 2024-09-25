import streamlit as st
import pandas as pd

def load_data():
    data = pd.read_csv("stocks.csv")  # Replace with actual dataset path
    return data

def show_dataset_page():
    st.title("Dataset Overview")
    
    data = load_data()

    st.write("Here is a quick overview of the dataset:")
    st.write(data.head())

    st.write("**Basic Statistics**")
    st.write(data.describe())
    
    st.write("**Column Information**")
    st.write("""
    - `Ticker`: Stock symbol
    - `Date`: Date of the stock data
    - `Open`: Opening price
    - `High`: Highest price during the day
    - `Low`: Lowest price during the day
    - `Close`: Closing price
    - `Adj Close`: Adjusted closing price
    - `Volume`: Number of shares traded
    """)
