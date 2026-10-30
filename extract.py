import pandas as pd
import os

# CSV file path
CSV_FILE = "food_orders.csv"

# Batch size
BATCH_SIZE = 100


def extract_data():
    if not os.path.exists(CSV_FILE):
        raise FileNotFoundError(f"{CSV_FILE} not found!")

    df = pd.read_csv(CSV_FILE)

    print("Total records extracted:", len(df))

    batches = []

    for start in range(0, len(df), BATCH_SIZE):
        batch = df.iloc[start:start + BATCH_SIZE]
        batches.append(batch)

    print("Total batches created:", len(batches))

    return batches


if __name__ == "__main__":
    extracted_batches = extract_data()