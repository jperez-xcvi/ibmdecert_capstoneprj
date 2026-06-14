<center>
    <img src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DB0321EN-SkillsNetwork/Images/SN_web_lightmode.png" width="300">
</center>

# Hands-on Lab:Querying data in NoSQL databases

Estimated time needed: **30** minutes.

It is highly recommened that you finish the <a href="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DB0151EN-SkillsNetwork/labs/Final%20Assignment/Setup%20and%20Practice%20Assignment.md.html" target="_blank">Setup and Practice Assignment Lab</a> before you proceed with this Assignment.

## About This SN Labs Cloud IDE

This Skills Network Labs Cloud IDE provides a hands-on environment for course and project related labs. It utilizes Theia, an open-source IDE (Integrated Development Environment) platform, that can be run on desktop or on the cloud. To complete this lab, we will be using the Cloud IDE based on Theia and Mongodb running in a Docker container.

## Important Notice about this lab environment

Please be aware that sessions for this lab environment are not persisted. Every time you connect to this lab, a new environment is created for you. Any data you may have saved in the earlier session would get lost. Plan to complete these labs in a single session, to avoid losing your data.

## Scenario

You are a data engineer at an e-commerce company. Your company needs you to design a data platform that uses MongoDB as a NoSQL database. You will be using MongoDB to store the e-commerce catalog data.

## Objectives

In this assignment you will:

- import data into a MongoDB database.
- query data in a MongoDB database.
- export data from MongoDB.

## Tools / Software

 - MongoDB Server
 - MongoDB Command Line Backup Tools

 > After completing each task, save both the executed commands and their corresponding outputs in a text document, or take screenshots—depending on the option you have chosen. This information will be required to answer questions during the final project submission.


# Exercise 1 - Check the lab environment

Before you proceed with the assignment :

 - Check if you have the 'mongoimport' and 'mongoexport' installed on the lab, otherwise install them.
 - Download the `catalog.json` file from  <a href="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DB0321EN-SkillsNetwork/nosql/catalog.json">here</a>.


# Exercise 2 - Working with MongoDB

### Task 1 Import data into MongoDB

Import the `catalog.json` file into MongoDB, using `catalog` as the database and `electronics` as the collection.

Save the command you executed and its output in a text document, or take a screenshot showing both the command and its output for future reference.

### Task 2 - List all databases

List out all the databases available in your MongoDB server.

Save the command you executed and its output in a text document, or take a screenshot showing both the command and its output for future reference.

### Task 3 - List all collections in the `catalog` database

List out all the collections present in the MongoDB database named `catalog`.

Save the command you executed and its output in a text document, or take a screenshot showing both the command and its output for future reference.

### Task 4 - Create an index on the `type` field

Create an index on the `type` field in the `electronics` collection of the `catalog` database.

Save the command you executed and its output in a text document, or take a screenshot showing both the command and its output for future reference.

### Task 5 -Find the count of laptops

Write a query to count documents with `type` equal to `laptop` in the `electronics` collection.

Save the command you executed and its output in a text document, or take a screenshot showing both the command and its output for future reference.

### Task 6 - Count smart phones with 6-inch screen size

Write a query to find the number of `smart phones` with screen size of 6 inches

Save the command you executed and its output in a text document, or take a screenshot showing both the command and its output for future reference.


### Task 7 - Find average screen size of smart phones

Write a query to find out the average screen size of `smart phones`.

Save the command you executed and its output in a text document, or take a screenshot showing both the command and its output for future reference.

### Task 8 - Export selected fields to a CSV file

Export the fields `_id`, `type`, `model`, from the `electronics` collection into a file named `electronics.csv`

Save the command you executed and its output in a text document, or take a screenshot showing both the command and its output for future reference.

End of assignment.

## Authors

Ramesh Sannareddy

## Other Contributors

Rav Ahuja

## Change Log

| Date (YYYY-MM-DD) | Version | Changed By        | Change Description                 |
| ----------------- | ------- | ----------------- | ---------------------------------- |
| 2022-04-14        | 0.2     |Lakshmi Holla | Changed question |
| 2021-14-18        | 0.1     | Ramesh Sannareddy | Created initial version |

<center><h5>Copyright (c) 2022 IBM Corporation. All rights reserved.</h5></center>
