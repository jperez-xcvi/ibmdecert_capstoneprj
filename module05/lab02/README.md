## 1. Download "acceslog.text"
```bash
cd ./module05/lab02/airflow/dags/capstone
```
```bash
curl -O https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DB0321EN-SkillsNetwork/ETL/accesslog.txt
```
```bash
cd ~/projects/ibmdecert_capstoneprj
```
## 2. Deploy airflow
```bash
cd ./module05/lab02/airflow
```
```bash
curl -LfO 'https://airflow.apache.org/docs/apache-airflow/stable/docker-compose.yaml'
```
```bash
echo -e "AIRFLOW_UID=$(id -u)" > .env
```
```bash
cd dags
```
```bash
touch process_web_log.py
```
```bash
uv add apache-airflow --dev
```
return to /airflow and execute (before we need a .env with AIRFLOW_UID and FERNET_KEY as variables)
```bash
docker compose up -d
```
## 3. Execute the ETL Flow
We need to open airflow in the browser, search the dag and execute it the output will be `extracted_data.txt,` `transformed_data.txt` and `weblog.tar` in `airflow/dags/capstone`