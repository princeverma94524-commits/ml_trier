import pandas as pd

def clean_sales_data(df: pd.DataFrame):
    """
    Clean and preprocess sales data
    """

    # 1. Remove missing values (make a copy)
    df = df.dropna().copy()

    # 2. Ensure correct data types (safe assignment)
    df.loc[:, "price"] = df["price"].astype(float)
    df.loc[:, "sales"] = df["sales"].astype(int)

    # 3. Remove invalid values
    df = df[(df["price"] > 0) & (df["sales"] >= 0)]

    return df


def save_processed_data(df: pd.DataFrame, output_path: str):
    """
    Save cleaned data to processed folder
    """
    df.to_csv(output_path, index=False)


