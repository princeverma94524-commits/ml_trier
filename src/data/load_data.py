import pandas as pd
import os

def load_uploaded_csv(file_path: str):
    """
    Load CSV file uploaded by user

    Args:
        file_path (str): Path of uploaded CSV file

    Returns:
        pd.DataFrame: Loaded dataset
    """
    if not os.path.exists(file_path):
        raise FileNotFoundError("CSV file not found")

    if not file_path.endswith(".csv"):
        raise ValueError("Only CSV files are supported")

    data = pd.read_csv(file_path)
    return data
