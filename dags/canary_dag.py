# mandatory dag for prometheus exporter and airflow self-check
#
from datetime import timedelta, datetime

from airflow import DAG

from airflow.operators.bash_operator import BashOperator

default_args = {
    "owner": "quark",
    "depends_on_past": False,
    "email_on_failure": False,
}

with DAG(
    "canary_dag",
    start_date=datetime(2020, 10, 8),
    default_args=default_args,
    tags=["monitoring", "quark"],
    max_active_runs=1,
    concurrency=1,
    schedule_interval=timedelta(minutes=1),
    catchup=False,
) as dag:
    BashOperator(
        task_id="check_alive",
        bash_command="""date ;
        date +%s ;
        date > /tmp/airflow_last_schedule;
        date +%s >> /tmp/airflow_last_schedule
        """,
        retries=0,
    ).doc_md = "task is to check airflow is able to schedule"
