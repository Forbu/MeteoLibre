"""
Simple functions for downloading files from a remote server
"""

import requests
import os
from dotenv import load_dotenv
import argparse
import csv

config = load_dotenv()

TOKEN_API_DOWNLOAD = config.get("TOKEN_API_DOWNLOAD")

def download_stations_list():
    """
    Download the stations list from the remote server https://public-api.meteofrance.fr/public/DPObs/liste-stations
    and put the data in the data/stations_list.csv file
    """
    url = "https://public-api.meteofrance.fr/public/DPObs/liste-stations"
    headers = {
        "Authorization": f"Bearer {TOKEN_API_DOWNLOAD}"
    }
    response = requests.get(url, headers=headers)
    data = response.json()
    with open("data/stations_list.csv", "w") as file:
        writer = csv.writer(file)
        writer.writerow(data)
        

    
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--stations_list", action="store_true", help="Download the stations list")
    args = parser.parse_args()
    if args.stations_list:
        download_stations_list()
    
