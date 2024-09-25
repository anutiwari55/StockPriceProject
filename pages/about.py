import streamlit as st

def show_about_page():
    st.title("About This Project")
    st.markdown("""
    This dashboard is designed to help users interactively explore stock market data.
    You can filter data by ticker, date, and volume to understand stock performance.
    
    **Technologies Used:**
    - Python
    - Streamlit
    - Pandas for data manipulation
    - Matplotlib & Seaborn for visualizations
    
    **Author**: Your Name
    """)
