import os
import psycopg2
from dotenv import load_dotenv

load_dotenv()

# Connection details
dsn_hostname = 'localhost'
dsn_user = os.environ.get("POSTGRES_USER")
dsn_pwd = os.environ.get("POSTGRES_PASSWORD")
dsn_port = os.environ.get("POSTGRES_PORT")
dsn_database = 'sales'

# Create connection
conn = psycopg2.connect(
   database=dsn_database, 
   user=dsn_user,
   password=dsn_pwd,
   host=dsn_hostname, 
   port=dsn_port
)

cursor = conn.cursor()

# 1. Create the right table required in the lab instruction
SQL_CREATE_TABLE = """
CREATE TABLE IF NOT EXISTS sales_data (
    rowid INTEGER PRIMARY KEY NOT NULL,
    product_id INTEGER NOT NULL,
    customer_id INTEGER NOT NULL,
    price DECIMAL DEFAULT 0.0 NOT NULL,
    quantity INTEGER NOT NULL,
    timestamp TIMESTAMP WITHOUT TIME ZONE DEFAULT CURRENT_TIMESTAMP NOT NULL
);
"""

# Execute statement
cursor.execute(SQL_CREATE_TABLE)
conn.commit()
print("Table 'sales_data' verified/sucessfully created.")


# 2. load csv in the table sales_data (Paso 9)

path_to_csv = '/home/jose/projects/ibmdecert_capstoneprj/module05/lab01/sales.csv' 

try:
    with open(path_to_csv, 'r') as f:
        # CORREGIDO: Cambiamos la ruta por STDIN para que Python transmita el flujo local
        SQL_COPY = """
            COPY sales_data(rowid, product_id, customer_id, price, quantity, timestamp)
            FROM STDIN WITH (FORMAT CSV, HEADER true);
        """
        cursor.copy_expert(SQL_COPY, f)
    conn.commit()
    print(f"Datos de '{path_to_csv}' cargados exitosamente en 'sales_data'.")
except Exception as e:
    conn.rollback()
    print(f"Error al cargar el archivo CSV: {e}")


# ==============================================================================
# NOTA: This Query was commented because the schema differs from last requirements
# ==============================================================================
# cursor.execute("INSERT INTO products(rowid,product,category) VALUES(1,'Television','Electronics')")
# ...
# ==============================================================================


# 3. Show first five rows
print("\nFirst 5s rows from'sales_data':")
cursor.execute('SELECT * FROM sales_data LIMIT 5;')
rows = cursor.fetchall()

for row in rows:
    print(row)

# Close connections
cursor.close()
conn.close()