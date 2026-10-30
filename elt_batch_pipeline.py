from extract import extract_data
from load_raw import load_raw_data
from retrieve_raw import retrieve_raw_data
from transform import transform_data
from validate import validate_data
from load_transformed import load_transformed_data


def run_pipeline():

    print("\n========== ELT PIPELINE STARTED ==========")

    # Step 1: Extract
    print("\nSTEP 1: EXTRACT")
    extracted_batches = extract_data()

    total_extracted = sum(len(batch) for batch in extracted_batches)
    print("Total extracted records:", total_extracted)
    print("Total extracted batches:", len(extracted_batches))

    # Step 2: Load raw data
    print("\nSTEP 2: LOAD RAW DATA")
    load_raw_data()

    # Step 3: Retrieve raw data
    print("\nSTEP 3: RETRIEVE RAW DATA")
    retrieved_batches = retrieve_raw_data()

    total_retrieved = sum(len(batch) for batch in retrieved_batches)
    print("Total retrieved records:", total_retrieved)

    # Step 4: Transform
    print("\nSTEP 4: TRANSFORM DATA")
    valid_df, rejected_df = transform_data(retrieved_batches)

    print("Valid records:", len(valid_df))
    print("Rejected records:", len(rejected_df))

    # Step 5: Validate
    print("\nSTEP 5: VALIDATE DATA")
    validation_report = validate_data(valid_df, rejected_df)

    # Step 6: Load transformed data
    print("\nSTEP 6: LOAD ANALYTICS DATA")
    load_transformed_data(valid_df)

    print("\n========== EXECUTION SUMMARY ==========")
    print("Extracted records:", total_extracted)
    print("Retrieved records:", total_retrieved)
    print("Valid records:", len(valid_df))
    print("Rejected records:", len(rejected_df))
    print("Validation report generated successfully.")

    print("\n========== ELT PIPELINE COMPLETED ==========")


if __name__ == "__main__":
    run_pipeline()