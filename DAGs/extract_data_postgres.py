from datetime import datetime
from airflow import DAG
from airflow.providers.docker.operators.docker import DockerOperator
from airflow.providers.postgres.operators.postgres import PostgresOperator
from airflow.operators.python import PythonOperator

default_args = {
    'start_date': datetime(2023, 4, 28)
}

with DAG('postgresql_docker_example', default_args=default_args, schedule_interval=None) as dag:
    
    # Task to extract data from PostgreSQL inside Docker
    extract_data = DockerOperator(
        task_id='extract_data',
        image='postgres',
        api_version='auto',
        auto_remove=True,
        command='bash -c "pg_dump -U postgres -h db_psql -d banco_teste_python > /tmp/data_dump.sql"', #os.environ.get('DB_NAME')
        docker_url='unix://var/run/docker.sock',
        network_mode='bridge',
        mounts=[],
    )
    
    # Task to print the result on the terminal
    print_result = PythonOperator(
        task_id='print_result',
        python_callable=lambda: print(open('/tmp/data_dump.sql').read()),
    )
    
    extract_data >> print_result