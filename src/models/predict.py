import joblib


def predict_demand(price, model_path="src/models/demand_model.pkl"):
    """
    Predict demand for a given price
    """

    model = joblib.load(model_path)
    prediction = model.predict([[price]])

    return int(prediction[0])
