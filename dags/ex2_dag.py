from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.python_operator import PythonOperator
from datetime import datetime

def my_custom_task():
    print("Running custom task")

# default args sent to operators
default_args = {
    'owner': 'airflow',
    'start_date': datetime(2024, 1, 1),
}

# Définir le DAG
with DAG('example_dag2',
         default_args=default_args,
         description='Exemple simple de DAG #2',
         schedule_interval='*/2 * * * *', # Once a day every 2 min
         catchup=False) as dag:
    
    # DAG Tasks / Operators
    start_task = DummyOperator(
        task_id='start_task'
    )
    
    custom_python_task = PythonOperator(
        task_id='my_custom_task',
        python_callable=my_custom_task
    )
    
    end_task = DummyOperator(
        task_id='end_task'
    )

    start_task >> custom_python_task >> end_task
