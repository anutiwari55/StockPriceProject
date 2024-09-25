import streamlit as st

def show_home_page():
    st.title("Welcome to the Stock Market Dashboard")
    st.markdown("""
    This dashboard allows you to explore and analyze stock market data, 
    filter by ticker, date, and volume, and gain insights into the performance 
    of various stocks.
    
    **Features:**
    - 15 Interactive Data Visualizations
    - Filter by Ticker, Date, and Volume
    - Overview of key stock metrics
    """)
    st.image('https://via.placeholder.com/800x400.png?text=Stock+Market+Data', use_column_width=True)
