"""
Test module for the download_mf.py module
"""
from dotenv import load_dotenv

config = load_dotenv()
import download_mf_tools.download_mf as download_mf

def test_download_ground_stations_data():
    download_mf.download_ground_stations_data()

def test_download_ground_stations_data_for_station():
    download_mf.download_ground_stations_data_for_station()

def xtest_download_radar_data():
    download_mf.download_radar_data()
