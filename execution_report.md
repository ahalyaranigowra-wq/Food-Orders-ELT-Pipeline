# Food Orders – ELT Batch Pipeline Execution Report

## 1. Introduction

The main aim of this project is to process food order data and prepare it for business analysis. For this, I developed a batch ELT pipeline using Python, Pandas and MySQL.

The process starts by reading the food orders from a CSV file. The original data is stored in a MySQL database, retrieved in batches, cleaned and transformed using Pandas, and finally stored in a separate database for analysis.

The pipeline was executed successfully, and the results are presented below.

## 2. Pipeline Execution Details

During the execution, the CSV file contained 1,010 records. These records were processed in batches of 100. The last batch contained only 10 records.

After loading the raw data into MySQL, I retrieved the records in batches and performed the required cleaning and transformation operations.

The final execution results are:

| Description | Result |
|---|---:|
| Total records extracted | 1,010 |
| Extraction batches | 11 |
| Records loaded into raw database | 1,010 |
| Records retrieved from raw database | 1,010 |
| Retrieval batches | 11 |
| Valid records after transformation | 1,000 |
| Rejected records | 0 |
| Records loaded into analytics database | 1,000 |
| Successful raw loading batches | 11 |
| Successful analytics loading batches | 10 |

## 3. Data Validation

After completing the transformation process, I performed validation checks to make sure the cleaned dataset was suitable for further analysis.

The validation results showed that:

- All expected columns were available in the cleaned dataset.
- No fully duplicated rows remained.
- No repeated Order ID values remained.
- No negative delivery durations were found in the valid records.
- No missing delivery durations were found in the valid records.
- All valid records had appropriate timestamps.
- A total of 1,000 records were classified as valid, with 0 rejected records.

The validation checks displayed by the pipeline were successful.

## 4. Business Analysis Using SQL

After loading the cleaned data into the analytics database, I used SQL queries to understand the order patterns and business performance.

The following results were obtained:

| Analysis | Result |
|---|---:|
| Total number of orders | 1,000 |
| Total order value | ₹10,13,415.00 |
| Average order value | ₹1,055.64 |
| Most used payment method | Cash on Delivery |
| Cash on Delivery orders | 336 |
| Most preferred order channel | Mobile App |
| Mobile App orders | 686 |
| Average delivery time | 73.58 minutes |
| Total platform net revenue | ₹80,877.00 |

### Key Observations

**1. Order Value:** The dataset contains 1,000 orders with a total order value of ₹10,13,415. The average value of an order is approximately ₹1,055.64.

**2. Payment Method:** Cash on Delivery is the most frequently used payment method, with 336 orders.

**3. Order Channel:** Most customers placed their orders through the Mobile App, accounting for 686 orders.

**4. Delivery Time:** The average delivery time across the valid records is 73.58 minutes.

**5. Platform Revenue:** The calculated total platform net revenue is ₹80,877.00.

These results provide a basic understanding of customer ordering behaviour and the platform's performance.

## 5. Database Information

The project uses two separate MySQL databases to maintain the raw and processed data.

**Raw Database**
- Database name: `food_orders_raw_db`
- Table name: `raw_food_orders`
- Total records: 1,010

**Analytics Database**
- Database name: `food_orders_analytics_db`
- Table name: `cleaned_food_orders`
- Total records: 1,000

Keeping the raw and cleaned data in separate databases makes it easier to maintain the original records and use the transformed data for analysis.

## 6. Conclusion

Through this project, I successfully developed and executed a batch ELT pipeline for the food orders dataset.

I worked on extracting records from CSV files, loading raw data into MySQL, retrieving records in batches, cleaning and transforming the data using Pandas, validating the results, and loading the final records into an analytics database.

Out of the 1,010 original records, 1,000 valid records were available after transformation. I also used SQL queries to analyse order values, payment methods, order channels, delivery time and platform net revenue.

Overall, this project helped me understand how raw data can be processed step by step and converted into useful information for business analysis.