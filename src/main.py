from src.data.load_data import load_uploaded_csv
from src.data.preprocess import clean_sales_data
from src.features.build_features import create_features
from src.models.train_model import train_demand_model
from src.models.predict import predict_demand


def main():
    print("🚀 Pricing Intelligence System Started")

    input_path = "src/data/uploads/sample_sales.csv"

    # Step 1: Load & clean data
    data = load_uploaded_csv(input_path)
    clean_data = clean_sales_data(data)

    # Step 2: Feature engineering
    X, y = create_features(clean_data)

    # Step 3: Train model
    train_demand_model(X, y)
    print("✅ ML model trained")

    # Step 4: Predict demand
    test_price = 500
    predicted_demand = predict_demand(test_price)

    print(f"📊 Predicted demand for price {test_price} is {predicted_demand}")
    print("🎉 Data → Features → Model step completed")


if __name__ == "__main__":
    main()
