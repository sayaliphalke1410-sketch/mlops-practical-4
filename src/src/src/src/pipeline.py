import os

from data_collection import collect_data
from preprocessing import preprocess_data
from feature_engineering import engineer_features
from validation import validate_data


def run_pipeline():

    print("=" * 50)
    print("MLOPS DATA PIPELINE")
    print("=" * 50)

    # Step 1: Data Collection
    df = collect_data()

    # Step 2: Data Preprocessing
    df = preprocess_data(df)

    # Step 3: Feature Engineering
    df = engineer_features(df)

    # Step 4: Data Validation
    validate_data(df)

    # Step 5: Save processed data
    os.makedirs("data/processed", exist_ok=True)

    output_path = "data/processed/final_data.csv"

    df.to_csv(output_path, index=False)

    print("Processed data saved successfully")
    print("Output:", output_path)
    print("Final shape:", df.shape)

    print("=" * 50)
    print("PIPELINE COMPLETED SUCCESSFULLY")
    print("=" * 50)


if __name__ == "__main__":
    run_pipeline()
