## 1. Delete Previous database called "sales"
Unlike cloud IDE provided by IBM that offers temporal development environments, our local one using docker persist data in volumes, so we need to enter corresponding container to delete previous database called `sales` made in `module01`
```bash
docker exec -it mysql_container  mysql -u root -p
```
Now in the mysql cli
```sql
DROP DATABASE IF EXISTS sales;
```
## 2. Download required files
first change to `./module05/lab01` before execute the downloads
```bash
curl -O https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DB0321EN-SkillsNetwork/ETL/sales.sql
```
```bash
curl -O https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/BFgMvlR8BKEjijGlWowK1Q/mysqlconnect.py
```
```bash
curl -O https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/OHNZDzk-BAcrpy75I0DCoA/postgresqlconnect.py
```
```bash
curl -O https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/OHNZDzk-BAcrpy75I0DCoA/postgresqlconnect.py
```
```bash
curl -O https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DB0321EN-SkillsNetwork/ETL/automation.py
```
```bash
curl -O https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/sales-csv3mo8i5SHvta76u7DzUfhiw.csv
```
## 3. Create Python environment
```bash
uv init --python "==3.13.11"
```

## 4. Install dependecies
```bash
uv add psycopg2-binary python-dotenv mysql-connector-python
```

## 5. Import backup sql to sales database in MySQL using PhpMyAdmin
Open PhpMyAdmin and import `sales.sql`

## 6. Execute Python script for database "sales" in MySQL
Execute `mysqlconnect.py`

## 7. Create database "sales" in PostgreSQL
```bash
docker exec -it postgresql_container  psql -U postgres
```
```sql
CREATE DATABASE sales;
```

## 9. Execute Python script for database "sales" in PostgreSQL
Execute `postgresqlconnect.py`

## 10. Execute Python automation script
Execute `automation.py`

