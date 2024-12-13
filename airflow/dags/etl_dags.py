from datetime import datetime
from airflow.providers.ssh.operators.ssh import SSHOperator
from airflow import DAG


with DAG(
    dag_id = "first_etl_dag",
    start_date = datetime(2024, 12, 12),
    schedule_interval = "@daily",
    catchup = False
) as dag:
     
    t0 = SSHOperator(
        task_id="starting",
        ssh_conn_id="python_ssh",
        cmd_timeout=None,
        command="echo 'Starting the script'"
    )

    t1 = SSHOperator(
        task_id="load_to_mariadb",
        ssh_conn_id="python_ssh",
        cmd_timeout=None,
        command="python /app/scripts/load_to_mariadb.py"
    )

    t2 = SSHOperator(
        task_id="transform",
        ssh_conn_id="python_ssh",
        cmd_timeout=None,
        command="python /app/scripts/transfrom.py" 
    )

    t3 = SSHOperator(
        task_id="load",
        ssh_conn_id="python_ssh",
        cmd_timeout=None,
        command="python /app/scripts/load.py"
    )

    t4 = SSHOperator(
        task_id="the_end",
        ssh_conn_id="python_ssh",
        cmd_timeout=None,
        command="echo 'The script has ended'"
    )

    t0 >> t1 >> t2 >> t3 >> t4