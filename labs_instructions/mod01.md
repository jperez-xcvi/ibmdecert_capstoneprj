::page{title="Hands-on Lab: OLTP Database"}

<img src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DB0321EN-SkillsNetwork/Images/SN_web_lightmode.png" width="300">

<br></br>
Estimated time needed: **30** minutes.

## About This SN Labs Cloud IDE 

This Skills Network Labs Cloud IDE provides a hands-on environment for course and project related labs. It utilizes Theia, an open-source IDE (Integrated Development Environment) platform, that can be run on desktop or on the cloud. To complete this lab, we will be using the Cloud IDE based on Theia and MySQL running in a Docker container.

## Important Notice about this lab environment

Please be aware that sessions for this lab environment are not persisted. Every time you connect to this lab, a new environment is created for you. Any data you may have saved in the earlier session would get lost. Plan to complete these labs in a single session, to avoid losing your data.

## Scenario

You are a data engineer at an e-commerce company. Your company needs you to design a data platform that uses MySQL as an OLTP database. You will be using MySQL to store the OLTP data.

## Objectives

In this assignment you will:

- design the schema for OLTP database.
- load data into OLTP database.
- automate admin tasks.

## Tools / Software

 - MySQL 8.0.22
 - phpMyAdmin 5.0.4


> Optional: After completing each task, save both the executed commands and their corresponding outputs in a text document, or take screenshots—depending on the option you have chosen. This information will be required to answer questions during the final project submission.

::page{title="Exercises - Setting up the database"}


## Exercise 1 - Check the lab environment

Before you proceed with the assignment :

 - Start MySQL server.

## Exercise 2 - Design the OLTP Database

### Task 1 - Create a database.

Create a database named `sales`.

### Task 2 - Design a table named `sales_data`.

Design a table named `sales_data` based on the sample data given.

![](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DB0321EN-SkillsNetwork/oltp/sampledata.png)

> **Note: Ensure that the field names (i.e., column names) in your SQL statement for creating the table exactly match those shown in the screenshot above.**

Create the `sales_data` table in `sales` database.

Save the SQL statement used to create the table and its output in a text document for future reference.

::page{title="Exercises - Querying and Admin tasks"}

## Exercise 3 - Load the Data

### Task 3 - Import `oltpdata.csv` into the `sales_data` table and write a SQL query to count the number of records in it.

Download the file oltpdata.csv from <a href=https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DB0321EN-SkillsNetwork/oltp/oltpdata.csv target="_blank">here</a>.

Save the SQL statement you used and its output in a text document for future reference.
## Exercise 4 - Set up Admin tasks

### Task 4 - Create an index

Create an index named `ts` on the `timestamp` field.

### Task 5 - List indexes

List indexes on the table `sales_data`.

Save the SQL statement you used and its output in a text document for future reference.

### Task 6 - Write a bash script to export data.

Write a bash script named `datadump.sh` that exports all the rows in the sales_data table to a file named `sales_data.sql`

Save the contents of the `datadump.sh` bash file, the command you used, and the resulting output in a text document for future reference.

::page{title="Conclusion"}

You have successfully created the OLTP database with all the required tables and data.

## Authors

Ramesh Sannareddy

## Other Contributors

Rav Ahuja
Abhishek Gagneja

<h3 align="center"> &#169; IBM Corporation. All rights reserved. <h3/>

<!--

## Change Log

| Date (YYYY-MM-DD) | Version | Changed By        | Change Description                 |
| ----------------- | ------- | ----------------- | ---------------------------------- |
| 2021-11-22        | 0.1     | Ramesh Sannareddy | Created initial version |
| 2022-10-17        | 0.2     | Ramesh Sannareddy | Updated version |
| 2022-10-24        | 0.3     | Alison Woolford   | Updated version |
| 2022-05-16        | 0.4     | Lakshmi Holla     | Changed Task8 markdown |
| 2024-03-13		| 0.5	  | Abhishek Gagneja  | Format update |


