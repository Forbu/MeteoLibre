"""
Test module for the download_mf.py module
"""

import download_mf_tools.download_mf as download_mf

def test_download_ground_stations_data():
    download_mf.download_ground_stations_data()

def test_download_ground_stations_data_for_station():
    download_mf.download_ground_stations_data_for_station()

def xtest_download_radar_data():
    download_mf.download_radar_data()

def test_preprocess_radar_data():
    import os

    directory = "data/raw/radar/zipped"

    for file in os.listdir(directory):
        if file.endswith(".tar"):
            print(f"Processing file {file}")
            download_mf.preprocess_radar_data(f"{directory}/{file}")

    

