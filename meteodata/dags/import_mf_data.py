"""
In file we will create the airflow dag to import mf dataset
We use airflow 2.0

We want the dag to :
- run every hours
- download the radar data
- load the data in the database
"""

from airflow.decorators import dag, task
import datetime

from download_mf_tools.download_mf import download_radar_data, preprocess_radar_data


@task()
def download_data():
    """Download the radar data from Meteo France"""
    filename = download_radar_data()
    return filename

@task()
def process_data(filename: str):
    """Preprocess the downloaded radar data"""
    preprocess_radar_data(filename)

@dag(
    dag_id="import_mf_data",
    schedule=datetime.timedelta(hours=1),
    start_date=datetime.datetime(2025, 1, 1),
    catchup=False
)
def import_mf_data():
    """Import the radar data from Meteo France"""
    # Define the task dependencies
    filename = download_data()
    process_data(filename)
    
import_mf_dag = import_mf_data()