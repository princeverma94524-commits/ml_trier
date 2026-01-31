from sklearn.linear_model import LinearRegression
import joblib
import os


def train_demand_model(X, y, model_path="src/models/demand_model.pkl"):
    """
    Train ML model to predict demand based on price
    """

    model = LinearRegression()
    model.fit(X, y)

    # Save trained model
    joblib.dump(model, model_path)

    return model
