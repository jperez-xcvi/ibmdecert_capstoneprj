## 1. Enter to pgcli
```bash
docker exec -it postgresql_container  psql -U postgres
```
## 2. Create database "staging"
```sql
CREATE DATABASE staging;
```

## 3. Design table "softcartDimDate"
```sql
CREATE TABLE softcartDimDate (
    dateid INT PRIMARY KEY,
    date DATE NOT NULL,
    year INT NOT NULL,
    quarter INT NOT NULL,
    quartername VARCHAR(2) NOT NULL,
    month INT NOT NULL,
    monthname VARCHAR(20) NOT NULL,
    day INT NOT NULL,
    weekday INT NOT NULL,
    weekdayname VARCHAR(20) NOT NULL
);
```
## 4. Design tables softcartDimCategory, softcartDimItem, softcartDimCountry
```sql
CREATE TABLE softcartDimCategory (
    categoryid INT PRIMARY KEY,
    category VARCHAR(50) NOT NULL
);

CREATE TABLE softcartDimItem (
    itemid INT PRIMARY KEY,
    item VARCHAR(255) NOT NULL
);

CREATE TABLE softcartDimCountry (
    countryid INT PRIMARY KEY,
    country VARCHAR(100) NOT NULL
);
```

## 5. Design table softcartFactSales
```sql
CREATE TABLE softcartFactSales (
    orderid INT PRIMARY KEY,
    dateid INT NOT NULL,
    categoryid INT NOT NULL,
    itemid INT NOT NULL,
    countryid INT NOT NULL,
    price NUMERIC(10,2) NOT NULL
);
```
## 6. Set the relations
```sql
ALTER TABLE softcartFactSales 
    ADD CONSTRAINT fk_sales_date 
    FOREIGN KEY (dateid) REFERENCES softcartDimDate(dateid);

ALTER TABLE softcartFactSales 
    ADD CONSTRAINT fk_sales_category 
    FOREIGN KEY (categoryid) REFERENCES softcartDimCategory(categoryid);

ALTER TABLE softcartFactSales 
    ADD CONSTRAINT fk_sales_item 
    FOREIGN KEY (itemid) REFERENCES softcartDimItem(itemid);

ALTER TABLE softcartFactSales 
    ADD CONSTRAINT fk_sales_country 
    FOREIGN KEY (countryid) REFERENCES softcartDimCountry(countryid);
```