## 1. Download oltpdata.csv:
```bash
curl -O https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DB0321EN-SkillsNetwork/oltp/oltpdata.csv
```

## 2. Create database "sales"
```sql
CREATE DATABASE sales;
USE sales;
```
## 3. Create table "sales_data"
```sql
CREATE TABLE sales_data (
    product_id INT NOT NULL,
    customer_id INT NOT NULL,
    price INT NOT NULL,
    quantity INT NOT NULL,
    timestamp DATETIME NOT NULL
);
```
## 4. Import data through PhpMyAdmin
We can import data from csv to the table by selecting the table, the click on import

## 5. Create an Index
```sql
CREATE INDEX ts ON sales_data (timestamp);
```
## 6. List indexes
```sql
SHOW INDEX FROM sales_data;
```
## 7. Create shell script to export the data
```bash
touch datadump.sh
```
```bash
chmod +x ./module01/datadump.sh
```