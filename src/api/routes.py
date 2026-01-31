from flask import Blueprint, request, jsonify, render_template
import os

from data.load_data import load_uploaded_csv
from data.preprocess import clean_sales_data
from features.build_features import create_features
from models.train_model import train_demand_model
from models.predict import predict_demand
from pricing.dynamic_pricing import recommend_price


api_routes = Blueprint("api_routes", __name__)

UPLOAD_FOLDER = "src/data/uploads"


@api_routes.route("/")
def home():
    return render_template("index.html")


@api_routes.route("/graphs")
def graphs():
    return render_template("graphs.html")


@api_routes.route("/predict-price", methods=["POST"])
def predict_price():
    if "file" not in request.files:
        return jsonify({"error": "CSV file required"}), 400

    file = request.files["file"]
    base_price = float(request.form.get("base_price", 500))

    file_path = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(file_path)

    data = load_uploaded_csv(file_path)
    clean_data = clean_sales_data(data)
    X, y = create_features(clean_data)

    train_demand_model(X, y)

    predicted_demand = predict_demand(base_price)
    final_price = recommend_price(base_price, predicted_demand)

    return jsonify({
        "base_price": base_price,
        "predicted_demand": predicted_demand,
        "recommended_price": final_price
    })
