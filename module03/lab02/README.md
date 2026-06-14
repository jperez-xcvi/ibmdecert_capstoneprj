## 1. Download SQL script:
```bash
curl -O https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/nm75oOK5n7AGME1F7_OIQg/CREATE-SCRIPT.sql
```
## 2. Download datasets (.csv)
```bash
curl -O https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DB0321EN-SkillsNetwork/datawarehousing/DimCategory.csv
```
```bash
curl -O https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DB0321EN-SkillsNetwork/datawarehousing/DimCountry.csv
```
```bash
curl -O https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DB0321EN-SkillsNetwork/datawarehousing/DimDate.csv
```
```bash
curl -O https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DB0321EN-SkillsNetwork/datawarehousing/FactSales.csv
```

## 3. Create database "Test1"
```sql
CREATE DATABASE "Test1";
```
## 4. Copy csv files to container from host
```bash
docker cp /home/jose/projects/ibmdecert_capstoneprj/module03/lab01/DimCategory.csv postgresql_container:/tmp/
```
```bash
docker cp /home/jose/projects/ibmdecert_capstoneprj/module03/lab01/DimCountry.csv postgresql_container:/tmp/
```
```bash
docker cp /home/jose/projects/ibmdecert_capstoneprj/module03/lab01/DimDate.csv postgresql_container:/tmp/
```
```bash
docker cp /home/jose/projects/ibmdecert_capstoneprj/module03/lab01/FactSales.csv postgresql_container:/tmp/
```

## 5. Upload csv data to corresponding table of the database
### Option 1 postgres console

```bash
docker exec -it postgresql_container  psql -U postgres -d Test1
```
```sql
\copy "DimDate" FROM '/tmp/DimDate.csv' DELIMITER ',' CSV HEADER;

\copy "DimCategory" FROM '/tmp/DimCategory.csv' DELIMITER ',' CSV HEADER;

\copy "DimCountry" FROM '/tmp/DimCountry.csv' DELIMITER ',' CSV HEADER;

\copy "FactSales" FROM '/tmp/FactSales.csv' DELIMITER ',' CSV HEADER;
```

### Option 2 pgadmin
```sql
COPY "DimDate" FROM '/tmp/DimDate.csv' DELIMITER ',' CSV HEADER;

COPY "DimCategory" FROM '/tmp/DimCategory.csv' DELIMITER ',' CSV HEADER;

COPY "DimCountry" FROM '/tmp/DimCountry.csv' DELIMITER ',' CSV HEADER;

COPY "FactSales" FROM '/tmp/FactSales.csv' DELIMITER ',' CSV HEADER;
```
## 6. Verify if data was loaded sucessfully
```sql
SELECT * FROM "TableName(replace with table name)" LIMIT 5;
```

## 7. Create a grouping sets query
```sql
SELECT 
    co.country, 
    ca.category, 
    SUM(f.amount) AS total_sales
FROM "FactSales" f
JOIN "DimCountry" co ON f.countryid = co.countryid
JOIN "DimCategory" ca ON f.categoryid = ca.categoryid
GROUP BY 
    GROUPING SETS ((co.country), (ca.category), ());
```

## 8. Create rollup query
```sql
SELECT 
    d.year, 
    co.country, 
    SUM(f.amount) AS total_sales
FROM "FactSales" f
JOIN "DimDate" d ON f.dateid = d.dateid
JOIN "DimCountry" co ON f.countryid = co.countryid
GROUP BY 
    ROLLUP (d.year, co.country);
```

## 9. Create cube query
```sql
SELECT 
    d.year, 
    co.country, 
    AVG(f.amount) AS average_sales
FROM "FactSales" f
JOIN "DimDate" d ON f.dateid = d.dateid
JOIN "DimCountry" co ON f.countryid = co.countryid
GROUP BY 
    CUBE (d.year, co.country);
```

## 10. Create MQT
```sql
-- 1. View
CREATE MATERIALIZED VIEW total_sales_per_country AS
SELECT 
    co.country, 
    SUM(f.amount) AS total_sales
FROM "FactSales" f
JOIN "DimCountry" co ON f.countryid = co.countryid
GROUP BY co.country;
```
```sql
-- 2. Verification
SELECT * FROM total_sales_per_country;
```
