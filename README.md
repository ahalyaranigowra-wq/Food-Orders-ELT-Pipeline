# Food Orders – Batch ELT Pipeline Using Python, Pandas and MySQL

## 1. Project Overview

The **Food Orders ELT Batch Pipeline** is a data engineering project developed to process and analyse food order records.

The main objective of this project is to take raw food order data from a CSV file, store it in a MySQL database, retrieve it in batches, perform data cleaning and transformation using Python and Pandas, validate the processed records, and finally store the cleaned data in a separate analytics database.

This project follows a batch processing approach, where records are processed in groups of 100 instead of processing the entire dataset at once.

Through this project, I worked on different stages of a data pipeline, from handling raw data to preparing meaningful information for business analysis.

## 2. Project Objectives

The main objectives of this project are:

- To understand how a batch ELT pipeline works.
- To extract food order records from a CSV file.
- To load and maintain original records in a raw MySQL database.
- To retrieve records from the database in batches of 100.
- To identify and remove fully duplicated records.
- To handle missing values and convert columns into appropriate data types.
- To calculate delivery duration and platform net revenue.
- To validate the transformed dataset.
- To store the cleaned records in a separate analytics database.
- To perform business analysis using SQL queries.

## 3. Technologies and Tools Used

| Technology | Purpose |
|---|---|
| Python | Pipeline development and execution |
| Pandas | Data cleaning and transformation |
| NumPy | Numerical operations and missing-value handling |
| MySQL | Raw and analytics data storage |
| SQL | Business analysis and data retrieval |
| VS Code | Writing and executing Python scripts |
| Jupyter Notebook | Data understanding and initial analysis |

## 4. Dataset Information

The project uses a food orders dataset in CSV format.

**Input file:** `food_orders.csv`

**Original records:** 1,010

The dataset contains information related to:

- Order ID
- Customer ID
- Restaurant ID
- Order Date and Time
- Delivery Date and Time
- Order Value
- Delivery Fee
- Payment Method
- Discounts and Offers
- Commission Fee
- Payment Processing Fee
- Refunds and Chargebacks
- Weather Condition
- Order Channel

## 5. Project Workflow

The pipeline is organised into the following stages.

### Stage 1: Data Extraction

The original food orders dataset is read from the CSV file using Pandas. The extracted records are divided into batches of 100.

### Stage 2: Loading Raw Data

The original records are loaded into the `raw_food_orders` table in the `food_orders_raw_db` database.

The raw data is maintained separately so that the original records remain available for further processing.

### Stage 3: Retrieving Raw Data

The records are retrieved from MySQL in batches of 100 and converted into Pandas DataFrames for transformation.

### Stage 4: Data Transformation

The retrieved data is cleaned and transformed using Pandas.

The operations include:

- Removing fully duplicated records.
- Handling missing categorical values.
- Converting datetime columns into appropriate formats.
- Converting financial columns into numeric data types.
- Calculating delivery duration in minutes.
- Extracting order date and order hour.
- Calculating platform net revenue using the available financial components.
- Separating valid and rejected records.

### Stage 5: Data Validation

Validation checks are performed on the transformed dataset to verify the expected columns, duplicate records, repeated Order IDs, delivery durations and timestamps.

A validation report is also generated to record the results.

### Stage 6: Loading Transformed Data

After validation, the cleaned records are loaded into the `cleaned_food_orders` table in the `food_orders_analytics_db` database.

The records are inserted in batches of 100.

### Stage 7: Pipeline Execution

All the individual Python modules are connected through `elt_batch_pipeline.py`.

The complete pipeline can be executed using a single command:

```bash
python elt_batch_pipeline.py
```

## 6. Project Folder Structure

```text
Food_Orders_ELT_Pipeline/
│
├── food_orders.csv
├── elt_pipeline.ipynb
│
├── config.py
├── extract.py
├── load_raw.py
├── retrieve_raw.py
├── transform.py
├── validate.py
├── load_transformed.py
├── elt_batch_pipeline.py
│
├── validation_report.csv
├── execution_report.md
├── requirements.txt
└── README.md
```

### Description of Python Files

| File | Responsibility |
|---|---|
| `config.py` | Stores database configuration and connection function |
| `extract.py` | Reads CSV data and creates batches |
| `load_raw.py` | Loads original records into the raw database |
| `retrieve_raw.py` | Retrieves raw records from MySQL |
| `transform.py` | Cleans and transforms the retrieved data |
| `validate.py` | Performs validation checks and generates a report |
| `load_transformed.py` | Loads validated records into the analytics database |
| `elt_batch_pipeline.py` | Executes the complete pipeline |

## 7. Database Design

Two separate MySQL databases are used in this project.

### Raw Database

- Database: `food_orders_raw_db`
- Table: `raw_food_orders`
- Records loaded: 1,010

This database stores the original food order records before transformation.

### Analytics Database

- Database: `food_orders_analytics_db`
- Table: `cleaned_food_orders`
- Records loaded: 1,000

This database stores the cleaned and transformed records, including the additional calculated columns.

## 8. Final Pipeline Execution Results

The complete pipeline was executed successfully through the VS Code terminal.

| Execution Metric | Result |
|---|---:|
| Total records extracted | 1,010 |
| Extraction batches | 11 |
| Raw records loaded | 1,010 |
| Raw records retrieved | 1,010 |
| Retrieval batches | 11 |
| Valid transformed records | 1,000 |
| Rejected records | 0 |
| Analytics records loaded | 1,000 |
| Successful raw batches | 11 |
| Successful analytics batches | 10 |

All batches reported successful loading in the terminal output.

## 9. Business Analysis Using SQL

After loading the transformed data, SQL queries were executed to understand the food ordering patterns and platform performance.

The following results were obtained:

| Business Metric | Result |
|---|---:|
| Total Orders | 1,000 |
| Total Order Value | ₹10,13,415.00 |
| Average Order Value | ₹1,055.64 |
| Most Used Payment Method | Cash on Delivery |
| Cash on Delivery Orders | 336 |
| Most Preferred Order Channel | Mobile App |
| Mobile App Orders | 686 |
| Average Delivery Time | 73.58 minutes |
| Total Platform Net Revenue | ₹80,877.00 |

### Key Findings

1. **Order Value:** The total order value is ₹10,13,415, with an average order value of ₹1,055.64.
2. **Payment Preference:** Cash on Delivery is the most frequently used payment method, with 336 orders.
3. **Ordering Channel:** The Mobile App is the most preferred channel, accounting for 686 orders.
4. **Delivery Performance:** The average delivery time is 73.58 minutes.
5. **Platform Revenue:** The calculated total platform net revenue is ₹80,877.

These findings provide a basic view of customer ordering behaviour and platform performance.

## 10. Requirements and Installation

### Prerequisites

Make sure the following are available:

- Python 3
- MySQL Server
- MySQL Workbench
- Visual Studio Code

### Required Python Packages

The project uses the following Python libraries:

```text
pandas
numpy
mysql-connector-python
```

Install the packages using:

```bash
pip install -r requirements.txt
```

## 11. How to Execute the Project

Follow these steps to run the pipeline:

**Step 1:** Open the project folder in Visual Studio Code.

**Step 2:** Make sure the MySQL server is running and the required databases and tables are available.

**Step 3:** Update the MySQL connection details in `config.py`. Keep your database password private.

**Step 4:** Open the VS Code terminal in the project folder.

**Step 5:** Execute the following command:

```bash
python elt_batch_pipeline.py
```

**Step 6:** Check the terminal output to review the extraction, loading, transformation, validation and execution summary.

## 12. Conclusion

Working on this project gave me practical experience in building a batch ELT pipeline using Python, Pandas and MySQL.

I learned how to extract data from CSV files, store raw records in a database, retrieve data in batches, clean and transform records, perform validation checks and load the processed data into a separate analytics database.

I also used SQL queries to analyse order values, customer payment preferences, ordering channels, delivery time and platform net revenue.

Overall, this project helped me understand the complete data processing workflow and how cleaned data can be used to generate useful business insights.

---

**Project:** Food Orders – ELT Batch Pipeline  
**Tools:** Python, Pandas, NumPy, MySQL and SQL  
**Processing Method:** Batch Processing (100 records per batch)