from data.load_data import load_uploaded_csv
from data.preprocess import clean_sales_data, save_processed_data
from features.build_features import create_features


def main():
    print("🚀 Pricing Intelligence System Started")

    input_path = "src/data/uploads/sample_sales.csv"
    output_path = "src/data/processed/clean_sales_data.csv"

    # Step 1: Load CSV
    data = load_uploaded_csv(input_path)

    # Step 2: Clean data
    clean_data = clean_sales_data(data)

    # Step 3: Save cleaned data
    save_processed_data(clean_data, output_path)

    # Step 4: Feature engineering
    X, y = create_features(clean_data)

    print("✅ Features created")
    print("X (features):")
    print(X.head())

    print("y (target):")
    print(y.head())

    print("🎉 Data → Features step completed")


if __name__ == "__main__":
    main()
