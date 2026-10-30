import mysql.connector

# MySQL Database Configuration
DB_CONFIG = {
    "host": "localhost",
    "user": "root",
    "password": "YOUR_MYSQL_PASSWORD",
    "port": 3306
}

# Database Names
RAW_DATABASE = "food_orders_raw_db"
ANALYTICS_DATABASE = "food_orders_analytics_db"


def get_connection(database=None):
    config = DB_CONFIG.copy()

    if database:
        config["database"] = database

    return mysql.connector.connect(**config)