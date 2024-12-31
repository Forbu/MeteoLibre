"""
In this file, we download the data from the meteo france API.
We will download two main types of data:
- radar data (BUFR files)
- ground station data (CSV files)
"""

import requests
from dotenv import dotenv_values
import gzip
import csv
import datetime

config = dict(dotenv_values())


def download_radar_data():
    
    url = config["URL_MOSAIC_RADAR_DATA"]
    token = config["TOKEN_RADAR_DATA"]

    # Define the headers
    headers = {
        "accept": "application/gzip",
        "Authorization": f"Bearer {token}"
    }
    
    # we want to download the files and put them in the folder data/raw/radar
    response = requests.get(url, headers=headers)

    # we want to named the gzip file with the date and the time of the file
    date = datetime.datetime.now().strftime("%Y%m%d")
    time = datetime.datetime.now().strftime("%H%M%S")
    filename = f"{date}_{time}.gzip"
    with open(f"data/raw/radar/{filename}", "wb") as f:
        f.write(response.content)

    return filename


def download_ground_stations_data():
    """
    Download the stations list from the remote server https://public-api.meteofrance.fr/public/DPObs/liste-stations
    and put the data in the data/stations_list.csv file
    """
    url = config["URL_GROUND_STATIONS_DATA"]
    token = config["TOKEN_GROUND_STATIONS_DATA"]
    
    headers = {
        "accept": "*/*",
        "apikey": f"{token}"
    }
    response = requests.get(url, headers=headers)
    
    filename = "data/raw/ground_stations/stations_list.csv"
    with open(filename, "wb") as file:
        file.write(response.content)

def download_ground_stations_data_for_station(id_station="08244001"):
    # Define the API endpoint URL
    url = config["URL_GROUND_STATIONS_DATA_FOR_STATION"]
    token = config["TOKEN_GROUND_STATIONS_DATA"]

    # Define the query parameters
    params = {
        "id_station": id_station,
        "format": "csv"
    }

    # Define the headers
    headers = {
        "accept": "*/*",
        "apikey": f"{token}"
    }

    try:
        # Send a GET request
        response = requests.get(url, params=params, headers=headers)
        
        # Check if the request was successful
        if response.status_code == 200:
            
            filename = f"data/raw/ground_stations/{id_station}.csv"
            
            # Save the response data to a CSV file
            with open(filename, 'wb') as file:
                file.write(response.content)
            print(f"Data saved to {filename}")
        else:
            print(f"Request failed with status code {response.status_code}")
            print(response.text)
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    download_radar_data()
    download_ground_stations_data()
    download_ground_stations_data_for_station()


