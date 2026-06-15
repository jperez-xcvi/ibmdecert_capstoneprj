import os
from dotenv import load_dotenv
import mysql.connector

load_dotenv()

# connect to database
# You can get the Hostname and Password from the connection information section of Mysql 
connection = mysql.connector.connect(user='root', password=os.environ.get("MYSQL_ROOT_PASSWORD"),host='localhost',database='sales')

# create cursor

cursor = connection.cursor()

# create table

SQL = """CREATE TABLE IF NOT EXISTS products(

rowid int(11) NOT NULL AUTO_INCREMENT PRIMARY KEY,
product varchar(255) NOT NULL,
category varchar(255) NOT NULL

)"""

cursor.execute(SQL)

print("Table created")

# insert data

SQL = """INSERT INTO products(product,category)
	 VALUES
	 ("Television","Electronics"),
	 ("Laptop","Electronics"),
	 ("Mobile","Electronics")
	 """

cursor.execute(SQL)
connection.commit()


# query data

SQL = "SELECT * FROM products"

cursor.execute(SQL)

for row in cursor.fetchall():
	print(row)

# close connection
connection.close()