import pandas as pd

def load_customer_data(uploaded_file):
    """Load and clean customer purchase data."""
    df = pd.read_csv(uploaded_file)
    
    # Ensure column names are consistent
    required_columns = ["Customer_ID", "Age", "Past_Purchases", "Online_Reviews"]
    for col in required_columns:
        if col not in df.columns:
            raise ValueError(f"Missing required column: {col}")
    
    return df
