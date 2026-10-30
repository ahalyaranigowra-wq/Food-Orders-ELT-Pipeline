import pandas as pd


def validate_data(valid_df, rejected_df):

    report = {}

    # 1. Check expected columns
    expected_columns = [
        "order_id", "customer_id", "restaurant_id",
        "order_datetime", "delivery_datetime",
        "order_value", "delivery_fee", "payment_method",
        "discounts_and_offers", "commission_fee",
        "payment_processing_fee", "refunds_chargebacks",
        "weather_condition", "order_channel",
        "delivery_time_minutes", "order_date",
        "order_hour", "platform_net_revenue"
    ]

    report["Expected columns present"] = (
        set(expected_columns).issubset(valid_df.columns)
    )

    # 2. Check duplicate rows
    report["Duplicate rows"] = int(valid_df.duplicated().sum())

    # 3. Check repeated Order IDs
    report["Repeated Order IDs"] = int(
        valid_df["order_id"].duplicated().sum()
    )

    # 4. Check negative delivery durations
    report["Negative delivery durations"] = int(
        (valid_df["delivery_time_minutes"] < 0).sum()
    )

    # 5. Check missing delivery durations
    report["Missing delivery durations"] = int(
        valid_df["delivery_time_minutes"].isna().sum()
    )

    # 6. Check invalid timestamps
    report["Invalid timestamps"] = int(
        (
            valid_df["order_datetime"].isna()
            | valid_df["delivery_datetime"].isna()
        ).sum()
    )

    # 7. Record valid and rejected counts
    report["Valid records"] = len(valid_df)
    report["Rejected records"] = len(rejected_df)

    report_df = pd.DataFrame(
        list(report.items()),
        columns=["Validation Check", "Result"]
    )

    print(report_df)

    report_df.to_csv("validation_report.csv", index=False)

    return report_df


if __name__ == "__main__":
    from transform import transform_data
    from retrieve_raw import retrieve_raw_data

    batches = retrieve_raw_data()
    valid_df, rejected_df = transform_data(batches)

    validate_data(valid_df, rejected_df)