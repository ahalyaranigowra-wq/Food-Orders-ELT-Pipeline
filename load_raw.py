import pandas as pd
from config import get_connection, RAW_DATABASE
from extract import extract_data


def load_raw_data():

    batches = extract_data()
    expected_total = sum(len(batch) for batch in batches)

    connection = get_connection(RAW_DATABASE)
    cursor = connection.cursor()

    try:
        # Check existing records
        cursor.execute("SELECT COUNT(*) FROM raw_food_orders")
        existing_records = cursor.fetchone()[0]

        if existing_records == expected_total:
            print(f"Raw table already contains {existing_records} records.")
            print("Skipping raw data insertion.")
            return

        if existing_records > 0:
            print(f"Warning: Raw table contains {existing_records} records.")
            print("Expected:", expected_total)
            print("Insertion stopped to prevent duplicate records.")
            return

        insert_query = """
        INSERT INTO raw_food_orders (
            order_id, customer_id, restaurant_id,
            order_datetime, delivery_datetime,
            order_value, delivery_fee, payment_method,
            discounts_and_offers, commission_fee,
            payment_processing_fee, refunds_chargebacks,
            weather_condition, order_channel
        )
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s,
                %s, %s, %s, %s, %s, %s)
        """

        for batch_number, batch in enumerate(batches, start=1):

            records = [
                tuple(
                    None if pd.isna(value) else value
                    for value in row
                )
                for row in batch.itertuples(index=False, name=None)
            ]

            cursor.executemany(insert_query, records)
            connection.commit()

            print(f"Batch {batch_number} loaded: {len(records)} records")

    except Exception as error:
        connection.rollback()
        print("Error:", error)

    finally:
        cursor.close()
        connection.close()


if __name__ == "__main__":
    import pandas as pd
    load_raw_data()