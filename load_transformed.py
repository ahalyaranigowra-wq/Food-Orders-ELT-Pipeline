import pandas as pd
from config import get_connection, ANALYTICS_DATABASE

BATCH_SIZE = 100


def load_transformed_data(valid_df):

    connection = get_connection(ANALYTICS_DATABASE)
    cursor = connection.cursor()

    columns = [
        "order_id", "customer_id", "restaurant_id",
        "order_datetime", "delivery_datetime",
        "order_value", "delivery_fee", "payment_method",
        "discounts_and_offers", "commission_fee",
        "payment_processing_fee", "refunds_chargebacks",
        "weather_condition", "order_channel",
        "delivery_time_minutes", "order_date",
        "order_hour", "platform_net_revenue"
    ]

    try:
        # Check existing records
        cursor.execute("SELECT COUNT(*) FROM cleaned_food_orders")
        existing_records = cursor.fetchone()[0]

        if existing_records == len(valid_df):
            print(f"Analytics table already contains {existing_records} records.")
            print("Skipping insertion.")
            return

        if existing_records > 0:
            print("Existing records:", existing_records)
            print("Expected records:", len(valid_df))
            print("Insertion stopped to prevent duplicates.")
            return

        insert_query = """
        INSERT INTO cleaned_food_orders (
            order_id, customer_id, restaurant_id,
            order_datetime, delivery_datetime,
            order_value, delivery_fee, payment_method,
            discounts_and_offers, commission_fee,
            payment_processing_fee, refunds_chargebacks,
            weather_condition, order_channel,
            delivery_time_minutes, order_date,
            order_hour, platform_net_revenue
        )
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s,
                %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """

        total = len(valid_df)

        for start in range(0, total, BATCH_SIZE):

            batch = valid_df.iloc[start:start + BATCH_SIZE]

            records = [
                tuple(
                    None if pd.isna(value) else
                    value.to_pydatetime() if isinstance(value, pd.Timestamp) else
                    value.item() if hasattr(value, "item") else value
                    for value in row
                )
                for row in batch[columns].itertuples(
                    index=False, name=None
                )
            ]

            cursor.executemany(insert_query, records)
            connection.commit()

            print(
                f"Batch {start // BATCH_SIZE + 1} loaded: {len(records)} records"
            )

        print("Total transformed records loaded:", total)

    except Exception as error:
        connection.rollback()
        print("Loading error:", error)

    finally:
        cursor.close()
        connection.close()