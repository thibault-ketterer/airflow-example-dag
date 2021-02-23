# DAG to test Airflow pods permissions

import os
import inspect

from datetime import timedelta, datetime

from airflow import DAG
from airflow.operators.bash_operator import BashOperator

default_args = {
    "owner": "quark",
    "depends_on_past": False,
    "email_on_failure": False,
}


def get_base_folder():
    """
    Get relative path of current script.
    """
    return os.path.dirname(
        os.path.dirname(os.path.realpath(inspect.getfile(inspect.stack()[1][0])))
    )


with DAG(
    "canary_dag",
    start_date=datetime(2021, 2, 22),
    default_args=default_args,
    tags=["monitoring", "quark"],
    max_active_runs=1,
    concurrency=1,
    schedule_interval=timedelta(minutes=1),
    catchup=False,
) as dag:
    BashOperator(
        task_id="list_buckets",
        bash_command=f"""date ;
        python {get_base_folder()}/scripts/list_s3.py
        """,
        retries=0,
    ).doc_md = "task lists S3 buckets"
