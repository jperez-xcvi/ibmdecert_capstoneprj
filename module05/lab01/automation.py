import os
import mysql.connector
import psycopg2
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# ==========================================
# DB Auth Settings
# ==========================================
# MySQL (Staging Warehouse)
MYSQL_HOST = 'localhost'
MYSQL_USER = 'root'
MYSQL_PWD = os.environ.get("MYSQL_ROOT_PASSWORD")
MYSQL_PORT = os.environ.get("MYSQL_PORT")
MYSQL_DB = 'sales'

# PostgreSQL (Production Data Warehouse)
POSTGRES_HOST = 'localhost'
POSTGRES_USER = os.environ.get("POSTGRES_USER")
POSTGRES_PWD = os.environ.get("POSTGRES_PASSWORD")
POSTGRES_PORT = os.environ.get("POSTGRES_PORT")
POSTGRES_DB = 'sales'


# ==========================================
# ETL Flow Functions
# ==========================================

def get_last_rowid():
    """
    Task 1: Connect to the PostgreSQL Data Warehouse and return the last rowid 
    in the sales_data table. If the table is empty, return 0.
    """
    last_rowid = 0
    try:
        conn = psycopg2.connect(
            database=POSTGRES_DB, user=POSTGRES_USER, password=POSTGRES_PWD,
            host=POSTGRES_HOST, port=POSTGRES_PORT
        )
        cursor = conn.cursor()
        
        # Get the maximum value of rowid
        cursor.execute("SELECT MAX(rowid) FROM sales_data;")
        result = cursor.fetchone()
        
        if result and result[0] is not None:
            last_rowid = result[0]
            
        cursor.close()
        conn.close()
    except Exception as e:
        print(f"Error in get_last_rowid(): {e}")
        
    return last_rowid


def get_latest_records(rowid):
    """
    Task 2: Connect to the MySQL staging database and extract all records 
    with a rowid greater than the provided parameter.
    """
    records = []
    try:
        conn = mysql.connector.connect(
            host=MYSQL_HOST, user='root', password=MYSQL_PWD,
            port=MYSQL_PORT, database=MYSQL_DB
        )
        cursor = conn.cursor()
        
        # IMPORTANT: MySQL does not include 'price' or 'timestamp' by default in sales.sql.
        # We select the native columns in the exact order PostgreSQL expects to receive them,
        # assigning default values for 'price' and 'timestamp' since the MySQL staging table lacks them.
        query = """
            SELECT rowid, product_id, customer_id, 0.0 AS price, quantity, NOW() AS timestamp 
            FROM sales_data 
            WHERE rowid > %s;
        """
        cursor.execute(query, (rowid,))
        records = cursor.fetchall()
        
        cursor.close()
        conn.close()
    except Exception as e:
        print(f"Error in get_latest_records(): {e}")
        
    return records


def insert_records(records):
    """
    Task 3: Connect to the PostgreSQL Data Warehouse and insert the list of tuples
    (new records) extracted from the staging source database.
    """
    if not records:
        print("No new records to insert.")
        return

    try:
        conn = psycopg2.connect(
            database=POSTGRES_DB, user=POSTGRES_USER, password=POSTGRES_PWD,
            host=POSTGRES_HOST, port=POSTGRES_PORT
        )
        cursor = conn.cursor()
        
        # Parameterized statement to prevent SQL Injection and handle proper type formatting
        insert_query = """
            INSERT INTO sales_data (rowid, product_id, customer_id, price, quantity, timestamp)
            VALUES (%s, %s, %s, %s, %s, %s)
            ON CONFLICT (rowid) DO NOTHING;
        """
        
        # Execute batch insertions efficiently
        cursor.executemany(insert_query, records)
        conn.commit()
        
        cursor.close()
        conn.close()
    except Exception as e:
        print(f"Error in insert_records(): {e}")


# ==========================================
# MAIN AUTOMATION FLOW (Task 4)
# ==========================================

if __name__ == "__main__":
    print("Starting data synchronization cycle...")

    # 1. Fetch the last synchronized row ID from the Production Data Warehouse
    last_row_id = get_last_rowid()
    print("Last row id on production datawarehouse = ", last_row_id)

    # 2. Extract staging records from MySQL that are newer than that ID
    new_records = get_latest_records(last_row_id)
    print("New rows on staging datawarehouse = ", len(new_records))

    # 3. Load the incremental data into the Production Data Warehouse
    if len(new_records) > 0:
        insert_records(new_records)
        print("New rows inserted into production datawarehouse = ", len(new_records))
    else:
        print("The Data Warehouse is already fully synchronized.")

    print("Program completed successfully.")