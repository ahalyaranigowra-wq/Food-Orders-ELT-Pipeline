import pandas as pd
import numpy as np


def transform_data(batches):

    # Combine all batches to handle duplicates across batches
    df = pd.concat(batches, ignore_index=True)

    print("Records before cleaning:", len(df))

    # 1. Remove fully duplicated rows
    df = df.drop_duplicates().copy()

    # 2. Handle missing categorical values
    df["payment_method"] = df["payment_method"].fillna("Unknown")
    df["discounts_and_offers"] = (
        df["discounts_and_offers"].fillna("Not Specified")
    )

    # 3. Convert datetime columns
    df["order_datetime"] = pd.to_datetime(
        df["order_datetime"], errors="coerce"
    )

    df["delivery_datetime"] = pd.to_datetime(
        df["delivery_datetime"], errors="coerce"
    )

    # 4. Convert financial columns to numeric
    financial_columns = [
        "order_value",
        "delivery_fee",
        "commission_fee",
        "payment_processing_fee",
        "refunds_chargebacks"
    ]

    for column in financial_columns:
        df[column] = pd.to_numeric(df[column], errors="coerce")

    # 5. Calculate delivery duration
    df["delivery_time_minutes"] = (
        df["delivery_datetime"] - df["order_datetime"]
    ).dt.total_seconds() / 60

    # 6. Create derived date and hour columns
    df["order_date"] = df["order_datetime"].dt.date
    df["order_hour"] = df["order_datetime"].dt.hour

    # 7. Calculate platform net revenue
    revenue_columns = [
        "commission_fee",
        "delivery_fee",
        "payment_processing_fee",
        "refunds_chargebacks"
    ]

    complete_revenue = df[revenue_columns].notna().all(axis=1)

    df["platform_net_revenue"] = np.nan

    df.loc[complete_revenue, "platform_net_revenue"] = (
        df.loc[complete_revenue, "commission_fee"]
        + df.loc[complete_revenue, "delivery_fee"]
        - df.loc[complete_revenue, "payment_processing_fee"]
        - df.loc[complete_revenue, "refunds_chargebacks"]
    )

    # 8. Separate valid and rejected records
    valid_condition = (
        df["order_datetime"].notna()
        & df["delivery_datetime"].notna()
        & (df["delivery_time_minutes"] > 0)
    )

    valid_df = df[valid_condition].copy()
    rejected_df = df[~valid_condition].copy()

    print("Valid records:", len(valid_df))
    print("Rejected records:", len(rejected_df))

    return valid_df, rejected_df


if __name__ == "__main__":
    from retrieve_raw import retrieve_raw_data

    batches = retrieve_raw_data()
    valid_df, rejected_df = transform_data(batches)