# Hands on Lab - ETL

<img src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DB0321EN-SkillsNetwork/Images/SN_web_lightmode.png" width="300">


Estimated time needed: **30** minutes.


## Scenario

You are a data engineer at an e-commerce company.  You need to keep data synchronized between different databases/data warehouses as a part of your daily routine. One task that is routinely performed is the sync up of staging data warehouse and production data warehouse. Automating this sync up will save you a lot of time and standardize your process. You will be given a set of python scripts to start with. You will use/modify them to perform the incremental data load from MySQL server which acts as a staging warehouse to the IBM DB2 or PostgreSQL which is a production data warehouse. This script will be scheduled by the data engineers to sync up the data between the staging and production data warehouse.


## Objectives

In this assignment you will write a python program that will:

- Connect to PostgreSQL data warehouse and identify the last row on it.
- Connect to MySQL staging data warehouse and find all rows later than the last row on the datawarehouse.
- Insert the new data in the MySQL staging data warehouse into the PostgreSQL production data warehouse.

## About This SN Labs Cloud IDE

This Skills Network Labs Cloud IDE provides a hands-on environment for course and project related labs. It utilizes Theia, an open-source IDE (Integrated Development Environment) platform, that can be run on desktop or on the cloud. To complete this lab, we will be using the Cloud IDE based on Theia and MySQL database running in a Docker container. You will also need an instance of DB2 running in IBM Cloud or PostgreSQL database running in a Docker container.

## Important Notice about this lab environment

Please be aware that sessions for this lab environment are not persistent. A new environment is created for you every time you connect to this lab. Any data you may have saved in an earlier session 1will get lost. To avoid losing your data, please plan to complete these labs in a single session.


## Software Required

 - MySQL Server
 - PostgreSQL

>After completing each task, save both the executed commands and their corresponding outputs in a text document, or take screenshots—depending on the option you have chosen. This information will be required to answer questions during the final project submission.

# Prepare the lab environment

Before you start the assignment:

Step 1: Start MySQL server

Step 2: Create a database named `sales`

Step 3: Download the file below

<a href=https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DB0321EN-SkillsNetwork/ETL/sales.sql target="_blank">sales.sql</a>

Step 4: Import the data in the file `sales.sql` into the `sales` database.

Step 5: Download the mysqlconnect.py python programs from link below.

<a href=https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/BFgMvlR8BKEjijGlWowK1Q/mysqlconnect.py target="_blank">mysqlconnect.py</a>

Step 6: `mysqlconnect.py` has the sample code to help you understand how to connect to MySQL using Python.

Step 7: Modify `mysqlconnect.py` suitably and make sure you are able to connect to the MySQL server instance on the Theia environment.

> Note: Before executing `mysqlconnect.py` note that you install the connector using the command  `python3.11 -m pip install mysql-connector-python; `



Step 12: Download the postgresqlconnect.py python program from the link below.

<a href=https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/OHNZDzk-BAcrpy75I0DCoA/postgresqlconnect.py target="_blank">postgresqlconnect.py</a>

`postgresqlconnect.py` has the sample code to help you understand how to connect to the PostgreSql data warehouse using Python.

> Note: Before executing `postgresqlconnect.py` note that you install the connector using the command  
```
python3 -m pip install psycopg2
```

Step 7: Modify postgresqlconnect.py suitably and make sure you are able to connect to PostgreSql from the Theia environment.

Step 8: Download the file below

<a href = https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/sales-csv3mo8i5SHvta76u7DzUfhiw.csv target="_blank">sales.csv</a>

> Note: By default, the sales.csv file contains price and timestamp columns, which are not present in sales.sql. Therefore, you can use the below lines of code in your script to include price and timestamp columns when creating the table in Postgres.

```sql
price decimal DEFAULT 0.0 NOT NULL,
timeestamp timestamp without time zone DEFAULT CURRENT_TIMESTAMP NOT NULL
```

Step 9:  Create a table called `sales_data` using the columns `rowid`,` product_id`,` customer_id`,` price`,` quantity`
`timeestamp`. Load sales.csv into the table `sales_data` on your PostgreSql database.

> Note: Ensure that you upload the file to this path: /var/lib/pgadmin/

Step 10: Download the `automation.py` from the following URL : <a href=https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DB0321EN-SkillsNetwork/ETL/automation.py target="_blank">automation.py</a>

You will be using `automation.py` as a scafolding program to execute the tasks in this assignment

## Exercise 1 - Automate loading of incremental data into the data warehouse

One of the routine tasks that is carried out around a data warehouse is the extraction of daily new data from the operational database and loading it into the data warehouse.  In this exercise you will automate the extraction of incremental data, and loading it into the data warehouse.

	
### Task 1 - Implement the function `get_last_rowid()`

In the program `automation.py`, implement the function `get_last_rowid()` to connect to the PostgreSQL data warehouse and return the last `rowid`.

Save the function implementation code by either taking screenshots or saving them in a text document for future reference.

### Task 2 - Implement the function `get_latest_records()`

In the program `automation.py`, implement the function `get_latest_records()` to connect to the MySQL database and return all records with a rowid greater than the given last_rowid.

Save the function implementation code by either taking screenshots or saving them in a text document for future reference.

### Task 3 - Implement the function insert_records()

In the program `automation.py`, implement the function `insert_records()` to connect to the PostgreSQL data warehouse and insert all the provided records.

Save the function implementation code by either taking screenshots or saving them in a text document for future reference.

### Task 4 - Test the data synchronization

Run the program `automation.py` and verify that the data synchronization is functioning as expected.

Save the function implementation code by either taking screenshots or saving them in a text document for future reference.


::page{title="Conclusion"}

You have succesfully completed all the relevant tasks of ETL and pipelining set up as required.

## Author
Ramesh Sannareddy

### Other Contributors

Rav Ahuja
Abhishek Gagneja

<h3 align="center"> &#169; IBM Corporation. All rights reserved. <h3/>

<!--

## Change Log
| Date  (YYYY-MM-DD) | Version | Changed By        | Change Description                 |
| ----------------- | ------- | ----------------- | ---------------------------------- |
| 2025-03-14		| 0.8     | Abhishek Gagneja  | Format update |
|2023-06-29| 0.7 | Lakshmi Holla | Updated PostgreSql |
|2023-05-11| 0.6 | Eric Hao & Vladislav Boyko | Updated Page Frames |
|2023-05-10| 0.5 | Eric Hao & Vladislav Boyko | Updated Page Frames |
|2023-05-10| 0.4 | Eric Hao & Vladislav Boyko | Updated Page Frames |
| 2021-13-12        | 0.1     | Ramesh Sannareddy | Created initial version |
| 2022-09-29        | 0.2     | Appalabhaktula Hema | Updated code and instructions |
| 2023-05-04        | 0.3     | Benny Li | Republished |


