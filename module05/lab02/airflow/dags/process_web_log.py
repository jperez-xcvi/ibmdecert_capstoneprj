from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.bash import BashOperator

# Base local directory definition according to the environment
BASE_DIR = "/opt/airflow/dags/capstone"

# Exercise 2 - Task 1: Define the DAG arguments
default_args = {
    'owner': 'joseperez',
    'start_date': datetime(2026, 6, 1),
    'email': ['hosuke.cano@gmail.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

# Exercise 2 - Task 2: Define the DAG
with DAG(
    'process_web_log',
    default_args=default_args,
    description='ETL pipeline to process web server logs',
    schedule='@daily',  # Daily execution
    catchup=False,
) as dag:

    # Task 3: Extract the IP address (first field of a standard access log)
    extract_data = BashOperator(
        task_id='extract_data',
        bash_command=f"cut -d' ' -f1 {BASE_DIR}/accesslog.txt > {BASE_DIR}/extracted_data.txt"
    )

    # Task 4: Filter out all occurrences of the specific IP "198.46.149.143"
    transform_data = BashOperator(
        task_id='transform_data',
        bash_command=f"grep -v '198.46.149.143' {BASE_DIR}/extracted_data.txt > {BASE_DIR}/transformed_data.txt"
    )

    # Task 5: Archive the transformed file into a tar file
    # -C flag changes directory to prevent storing absolute paths inside the tar file
    load_data = BashOperator(
        task_id='load_data',
        bash_command=f"tar -cvf {BASE_DIR}/weblog.tar -C {BASE_DIR} transformed_data.txt"
    )

    # Task 6: Define the task pipeline
    extract_data >> transform_data >> load_data