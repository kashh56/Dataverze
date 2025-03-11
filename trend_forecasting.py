from prophet import Prophet
import pandas as pd

def forecast_trends(df):
    """Forecast product purchase trends using Prophet."""
    df["Date"] = pd.date_range(start="2023-01-01", periods=len(df), freq="D")
    
    trend_df = df.groupby("Date")["Past_Purchases"].count().reset_index()
    trend_df.columns = ["ds", "y"]
    
    model = Prophet()
    model.fit(trend_df)
    
    future = model.make_future_dataframe(periods=30)
    forecast = model.predict(future)
    
    return forecast
