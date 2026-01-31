import pandas as pd

def create_features(df: pd.DataFrame):
    """
    Convert cleaned data into ML features

    Input:
        df -> cleaned DataFrame

    Output:
        X -> features
        y -> target
    """

    # Feature matrix (input)
    X = df[["price"]]

    # Target variable (output)
    y = df["sales"]

    return X, y
