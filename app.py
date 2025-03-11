import streamlit as st
import pandas as pd
from data_Loader import load_customer_data
from sentiment_analysis import analyze_sentiment
from trend_forecasting import forecast_trends
from vizualization import plot_trend_chart
from twitter_scrapper import fetch_tweets
from PIL import Image

# ---- Branding & Styling ----
st.set_page_config(page_title="Dataverze AI Dashboard", page_icon="📊", layout="wide")

st.markdown(
 """
<style>
    .title {
        color: #154360;
        text-align: center;
        font-size: 70px;
        font-weight: bold;
        font-family: 'Helvetica', sans-serif;
    }
    .subtitle {
        color: #1A5276;
        text-align: center;
        font-size: 38px;
        font-style: italic;
        font-family: 'Helvetica', sans-serif;
    }
    .footer {
        text-align: center;
        font-size: 20px;
        color: #555;
        font-family: 'Helvetica', sans-serif;
    }
    .sidebar-title {
        font-size: 26px;
        font-weight: bold;
        color: #1A5276;
        font-family: 'Helvetica', sans-serif;
    }
    .center-image {
        display: flex;
        justify-content: center;
        align-items: center;
    }
</style>
    """,
    unsafe_allow_html=True
)

# ---- Sidebar: About the App ----
st.sidebar.markdown("<p class='sidebar-title'>📌 About Dataverze AI Suite</p>", unsafe_allow_html=True)
st.sidebar.markdown(
    """
    **Dataverze AI Suite 2025** is a cutting-edge business intelligence platform designed to harness AI for data-driven decision-making. This product offers two powerful modules:
    
    🔹 **Consumer Trend Predictor** 📊
    - Upload customer purchase data.
    - AI analyzes patterns and predicts future trends.
    - Get insights on upcoming high-demand products/services.
    
    🔹 **Real-Time Twitter Sentiment Analysis** 📢
    - Enter a keyword (e.g., 'Bitcoin', 'Tesla').
    - AI fetches and analyzes live tweets.
    - See public sentiment trends to refine marketing strategies.
    
    🚀 **Empower your business with Dataverze AI-powered analytics!**
    """, 
    unsafe_allow_html=True
)

st.sidebar.markdown("---")

# ---- Sidebar: Navigation ----
st.sidebar.markdown("<p class='sidebar-title' style='margin-bottom: 20px;'>🔍 Navigate</p>", unsafe_allow_html=True)
page = st.sidebar.radio("Select Feature", ["📊 Consumer Trend Predictor", "📢 Twitter Sentiment Analysis"], index=0)
st.sidebar.markdown("<br><br>", unsafe_allow_html=True)

st.sidebar.markdown("<br><br>", unsafe_allow_html=True)
st.sidebar.image("dataverze_logo.png", width=200)
st.sidebar.markdown("**Dataverze AI Suite 2025**\n🚀 All Rights Reserved.", unsafe_allow_html=True)


# ---- Header Section ----
st.markdown("<p class='title' style='font-size:40px; font-weight:bold; color:#1F618D; font-family:Arial, sans-serif;'>Dataverze AI Suite 2025</p>", unsafe_allow_html=True)
st.markdown("<p class='subtitle' style='font-size:25px; font-style:italic; color:#2874A6; font-family:Arial, sans-serif;'>AI-Powered Trends & Sentiment Analytics for Smarter Business Decisions</p>", unsafe_allow_html=True)
st.image("business_insights.jpg", width=400)

# ---- Consumer Trend Predictor ----
if page == "📊 Consumer Trend Predictor":
    st.header("📊 AI-Powered Consumer Trend Predictor")
    st.write("Upload customer purchase data to forecast future trends using machine learning.")
    
    uploaded_file = st.file_uploader("Upload Customer Data (CSV)", type=["csv"])
    
    if uploaded_file:
        df = load_customer_data(uploaded_file)
        st.write("### Data Preview", df.head())
        
        df = analyze_sentiment(df)
        st.write("### Customer Sentiment Analysis")
        st.write(df[['Customer_ID', 'Online_Sentiment']].head())
        
        forecast_df = forecast_trends(df)
        st.write("### Trend Forecasting")
        st.write(forecast_df.tail())
        
        plot_trend_chart(forecast_df)

# ---- Twitter Sentiment Analysis ----
if page == "📢 Twitter Sentiment Analysis":
    st.header("📢 Real-Time Twitter Sentiment Analysis")
    st.write("Analyze live Twitter sentiment for any topic using AI-powered NLP models.")
    
    keyword = st.text_input("Enter a keyword to track sentiment (e.g., 'iPhone', 'Crypto'):")
    
    if keyword:
        tweet_df = fetch_tweets(keyword, max_tweets=50)
        if tweet_df.empty:
            st.warning("No tweets found. Try a different keyword.")
        else:
            tweet_df = analyze_sentiment(tweet_df, column="Tweet")
            st.write("### Sentiment Analysis of Tweets")
            st.write(tweet_df[["Tweet", "Online_Sentiment"]])
            
            st.write("### Sentiment Distribution")
            st.bar_chart(tweet_df["Online_Sentiment"].value_counts())

# ---- Footer ----
st.markdown("""
    <p class='footer'>
    Ⓒ 2025 Dataverze AI Suite | All Rights Reserved.
    </p>
    """, unsafe_allow_html=True)
