import pandas as pd
from config import get_connection, RAW_DATABASE

BATCH_SIZE = 100


def retrieve_raw_data():

    connection = get_connection(RAW_DATABASE)
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM raw_food_orders")

    columns = [column[0] for column in cursor.description]

    batches = []

    while True:
        rows = cursor.fetchmany(BATCH_SIZE)

        if not rows:
            break

        batch_df = pd.DataFrame(rows, columns=columns)
        batches.append(batch_df)

    print("Total records retrieved:",
          sum(len(batch) for batch in batches))

    print("Total batches retrieved:", len(batches))

    cursor.close()
    connection.close()

    return batches


if __name__ == "__main__":
    retrieved_batches = retrieve_raw_data()