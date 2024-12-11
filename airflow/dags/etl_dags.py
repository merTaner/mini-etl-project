from datetime import datetime
from airflow.operators.bash import BashOperator
from airflow import DAG



with DAG(
    dag_id = "first_etl_dag",
    start_date = datetime(2024, 12, 11),
    schedule_interval = "@daily",
    catchup = False
):
    
    load_to_mariadb = BashOperator(
        task_id = "load_to_mariadb",
        bash_command = "python /opt/bitnami/airflow/dags/load_to_mariadb.py"
    )

    transform = BashOperator(
        task_id = "transform",
        bash_command = "python /opt/bitnami/airflow/dags/transfrom.py"
    )

    load = BashOperator(
        task_id = "load",
        bash_command = "python /opt/bitnami/airflow/dags/load.py"
    )

    load_to_mariadb >> transform >> load