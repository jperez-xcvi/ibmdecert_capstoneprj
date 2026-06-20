::page{title="Hands-on Lab:Data Pipelines Using Apache AirFlow"}

<img src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DB0321EN-SkillsNetwork/Images/SN_web_lightmode.png" width="300">

# 

Estimated time needed: **30** minutes.

## Scenario

Write a pipeline that analyzes the web server log file, extracts the required lines(ending with html) and fields(time stamp, size ) and transforms (bytes to mb) and load (append to an existing file.)

## Objectives

In this assignment, you will author an Apache Airflow DAG using **Bash operators** that will:

- Extract data from a web server log file
- Transform the data
- Load the transformed data into a tar file

## Tools / Software
 - Apache AirFlow

## About This SN Labs Cloud IDE

This Skills Network Labs Cloud IDE provides a hands-on environment for course and project related labs. It utilizes Theia, an open-source IDE (Integrated Development Environment) platform, that can be run on desktop or on the cloud. To complete this lab, we will be using the Cloud IDE based on Theia and Apache Airflow running in a Docker container.

## Important Notice about this lab environment

Please be aware that sessions for this lab environment are not persistent. A new environment is created for you every time you connect to this lab. Any data you may have saved in an earlier session will get lost. To avoid losing your data, please plan to complete these labs in a single session.


>After completing each task, save both the executed commands and their corresponding outputs in a text document, or take screenshots—depending on the option you have chosen. This information will be required to answer questions during the final project submission..


::page{title="Exercise 1 - Prepare the lab environment"}

Before you start the assignment:

 - Start Apache Airflow.
 - Download the dataset from the source to the destination mentioned below.

Source : <a href=https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DB0321EN-SkillsNetwork/ETL/accesslog.txt target="_blank">accesslog.txt</a> 

Destination : `/home/project/airflow/dags/capstone`

::page{title="Exercise 2 - Create a DAG"}

### Task 1 - Define the DAG arguments

Create a DAG with these arguments.

- owner
- start_date
- email

You may define any suitable additional arguments.

Save the code you used, along with its output, by either taking screenshots or saving it in a text document for future reference.

### Task 2 - Define the DAG

Create a DAG named `process_web_log` that runs daily.

Use suitable description.

Save the code you used, along with its output, by either taking screenshots or saving it in a text document for future reference.

### Task 3 - Create a task to extract data

Create a task named `extract_data`.

This task should extract the ipaddress field from the web server log file and save it into a file named extracted_data.txt

Save the code you used, along with its output, by either taking screenshots or saving it in a text document for future reference.

### Task 4 - Create a task to transform the data in the txt file

Create a task named `transform_data`.

This task should filter out all the occurrences of ipaddress "198.46.149.143" from extracted_data.txt and save the output to a file named `transformed_data.txt`.

Save the code you used, along with its output, by either taking screenshots or saving it in a text document for future reference.

### Task 5 - Create a task to load the data

Create a task named `load_data`.

This task should archive the file `transformed_data.txt` into a tar file named `weblog.tar`.

Save the code you used, along with its output, by either taking screenshots or saving it in a text document for future reference.

### Task 6 - Define the task pipeline

Define the task pipeline as per the details given below:

| Task | Functionality |
| ----------------- | ------- |
|First task 	| `extract_data` |
|Second task | `transform_data` |
|Third task 	| `load_data` |

Save the code you used, along with its output, by either taking screenshots or saving it in a text document for future reference.

::page{title="Exercise 3 - Getting the DAG operational"}

Save the DAG you defined into a file named `process_web_log.py`.

### Task 7 - Submit the DAG

Submit the DAG you have created to your Airflow environment so it can be scheduled and executed as defined.

Save the code you used, along with its output, by either taking screenshots or saving it in a text document for future reference.Save the code you used in a text document for future reference.

### Task 8 - Unpause the DAG

Unpause the DAG in your Airflow environment to enable its scheduled execution.

Save the code you used, along with its output, by either taking screenshots or saving it in a text document for future reference.

### Task 9 - Monitor the DAG

Take a screenshot of the DAG runs for the Airflow console.


::page{title="Conclusion"}

You have successfully used Airflow to set up an ETL pipeline to extract data from a log file.

## Authors

Ramesh Sannareddy

### Other Contributors

Rav Ahuja

Abhishek Gagneja


<h3 align="center"> &#169; IBM Corporation. All rights reserved. <h3/>

<!--

## Change Log

| Date (YYYY-MM-DD) | Version | Changed By        | Change Description                 |
| ----------------- | ------- | ----------------- | ---------------------------------- |
| 2021-13-12        | 0.1     | Ramesh Sannareddy | Created initial version |
| 2022-30-01        | 0.2     | Alison Woolford | Updated version |
| 2022-04-14        | 0.2     | Alison Woolford | Updated version |
| 2025-03-14 | 0.3 | Abhishek Gagneja | Format update |

