# Hands-on Lab:Data Warehouse Reporting

<img src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DB0321EN-SkillsNetwork/images/IDSN-logo.png" width="300">

## Estimated time needed: **30** minutes.

## Software Used in this Lab

</br>

To complete this lab you will utilize the <a href="https://www.postgresql.org/?utm_medium=Exinfluencer&utm_source=Exinfluencer&utm_content=000026UJ&utm_term=10006555&utm_id=NA-SkillsNetwork-Channel-SkillsNetworkCoursesIBMDB0110ENSkillsNetwork24601058-2021-01-01">PostgreSQL Database</a> relational database service available as part of IBM Skills Network Labs (SN Labs) Cloud IDE. SN Labs is a virtual lab environment used in this course.

<img src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DB0321EN-SkillsNetwork/datawarehousing/images/postgresql.png" alt="PostgreSQL" width="150">

</br>

## Scenario

You are a data engineer hired by an ecommerce company named SoftCart.com . The company retails download only items like E-Books, Movies, Songs etc. The company has international presence and customers from all over the world. You have designed the schema for the data warehouse in the previous assignment. Data engineering is a team game. Your senior data engineer reviewed your design. Your schema design was improvised to suit the production needs of the company. In this assignment you will generate reports out of the data in the data warehouse.

## Objectives

In this assignment you will:

- Load data into Data Warehouse
- Write aggregation queries
- Create MQTs


>

# About the dataset"

The dataset you would be using in this assignment is not a real life dataset. It was programmatically created for this assignment purpose.

## Prepare the lab environment



Before you start the assignment:

1. Right Click on this [link](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/nm75oOK5n7AGME1F7_OIQg/CREATE-SCRIPT.sql) and save this SQL file in you local system.

2. Start PostgreSQL server

3. Create a new database Test1

4. Create the following tables

    *  DimDate
    *  DimCategory
    *  DimCountry
    *  FactSales
	

>After completing each task, save both the executed commands and their corresponding outputs in a text document, or take screenshots—depending on the option you have chosen. This information will be required to answer questions during the final project submission.


## Loading Data

In this exercise you will load the data into the tables. You will load the data provided by the company in csv format.

### Task 1 - Load data into the dimension table DimDate

- Download the data from <a href="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DB0321EN-SkillsNetwork/datawarehousing/data/DimDate.csv"> this link</a>

- Load the downloaded data into DimDate table.

- Write a SQL query to display the first 5 rows of the table.

- Save the SQL statement you executed and its output in a text document, or take a screenshot of both for future reference.


### Task 2 - Load data into the dimension table DimCategory

- Download the data from <a href="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DB0321EN-SkillsNetwork/datawarehousing/DimCategory.csv"> this link</a>

- Load the downloaded data into DimCategory table.

- Write a SQL query to display the first 5 rows of the table.

- Save the SQL statement you executed and its output in a text document, or take a screenshot of both for future reference.

### Task 3 - Load data into the dimension table DimCountry

- Download the data from <a href="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DB0321EN-SkillsNetwork/datawarehousing/DimCountry.csv"> this link</a>

- Load the downloaded data into DimCountry table.

- Write a SQL query to display the first 5 rows of the table.

- Save the SQL statement you executed and its output in a text document, or take a screenshot of both for future reference.

### Task 4 - Load data into the fact table FactSales

- Download the data from <a href="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DB0321EN-SkillsNetwork/datawarehousing/FactSales.csv"> this link</a>

- Load this data into FactSales table.

- Write a SQL query to display the first 5 rows of the table.

- Save the SQL statement you executed and its output in a text document, or take a screenshot of both for future reference.

## Queries for data analytics

In this exercise you will query the data you have loaded in the previous exercise.

### Task 5 - Create a grouping sets query

- Create a grouping sets query using the columns country, category, totalsales.

- Save the SQL statement you executed and its output in a text document, or take a screenshot of both for future reference.

### Task 6 - Create a rollup query

- Create a rollup query using the columns year, country, and totalsales.

- Save the SQL statement you executed and its output in a text document, or take a screenshot of both for future reference

### Task 7 - Create a cube query

- Create a cube query using the columns year, country, and average sales.

- Save the SQL statement you executed and its output in a text document, or take a screenshot of both for future reference.

### Task 8 - Create an MQT

- Create an MQT named total_sales_per_country that has the columns country and total_sales.

- Save the SQL statement you executed and its output in a text document, or take a screenshot of both for future reference

End of the assignment.

## Authors

[Niveditha Pandith](https://www.linkedin.com/in/niveditha-pandith-53a057231)

### Other Contributors

Rav Ahuja

## Change Log

| Date (YYYY-MM-DD) | Version | Changed By        | Change Description                 |
| ----------------- | ------- | ----------------- | ---------------------------------- |
|2022-12-16|0.3|Niveditha Pandith|Converted initial version to Postgres
| 2021-12-12        | 0.1     | Ramesh Sannareddy | Created initial version |
| 2022-02-02        | 0.2     | Ramesh Sannareddy | Updated version |

<center><h5>Copyright (c) 2022 IBM Corporation. All rights reserved.</h5></center>
