import matplotlib.pyplot as plt
import seaborn as sns

import plotly.express as px
import streamlit as st

def plot_trend_chart(forecast_df):
    fig = px.line(forecast_df, x="ds", y="yhat", title="Forecasted Consumer Trends",
                  labels={"ds": "Date", "yhat": "Predicted Purchases"},
                  template="plotly_dark")
    st.plotly_chart(fig)

