"""
API for downloading radar data from Meteo France
"""
import os
import shutil  # Added shutil for removing directories

from fastapi import FastAPI
import uvicorn

from google.cloud import storage
from google.oauth2 import service_account

from download_mf_tools.download_mf import download_radar_data, preprocess_radar_data

app = FastAPI()

@app.get("/download_and_upload_radar_data")
async def download_and_upload_radar_data():
    """Download the radar data from Meteo France and upload it to the GCP bucket"""

    # Ensure the unzipped folder is empty before starting
    unzipped_dir = "data/raw/radar/unzipped"
    if os.path.exists(unzipped_dir):
        shutil.rmtree(unzipped_dir)
    os.makedirs(unzipped_dir, exist_ok=True)

    filename = download_radar_data()
    preprocess_radar_data(filename)

    # get all the files in the data/raw/radar/unzipped folder
    files = os.listdir(unzipped_dir)

    credentials = service_account.Credentials.from_service_account_default()
    storage_client = storage.Client(project="SmartCity", credentials=credentials)

    # put the files in the GCP bucket
    bucket_name = "meteofrancedata"
    bucket = storage_client.bucket(bucket_name)
    for file in files:
        bucket.upload_file(f"{unzipped_dir}/{file}", file)

    # remove the unzipped folder once it is not needed anymore
    shutil.rmtree(unzipped_dir)

    return {"message": "Radar data downloaded and uploaded to GCP bucket"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080)