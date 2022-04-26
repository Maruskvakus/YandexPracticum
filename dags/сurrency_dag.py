from datetime import datetime, timedelta
# The DAG object; we'll need this to instantiate a DAG
from airflow import DAG
# Operators; we need this to operate!
from airflow.operators.bash_operator import BashOperator

with DAG(
    'currency',
    # These args will get passed on to each operator
    # You can override them on a per-task basis during operator initialization
    default_args={
        'depends_on_past': False,
        'email': ['airflow@example.com'],
        'email_on_failure': False,
        'email_on_retry': False,
        'retries': 1,
        'retry_delay': timedelta(minutes=5),
    },
    description='A simple tutorial DAG',
    schedule_interval=timedelta(hours=3),
    start_date=datetime(2021, 1, 1),
    catchup=False,
    template_searchpath=["${AIRFLOW_HOME}/dags/scripts"]
) as dag:

    # t1, t2 and t3 are examples of tasks created by instantiating operators
    t1 = BashOperator(
        task_id = 'test',
        bash_command = "python3 ${AIRFLOW_HOME}/dags/scripts/insert.py",
        )


    t1
