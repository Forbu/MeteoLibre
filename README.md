# MeteoLibre

Une version open source d'un modèle météo basée sur les données de météo France

## Data part

All code element of the data part are in the `meteodata` folder.

The first element of the project will be to handle the different data sources.
We currently have mainly 3 sources of data:

- radar data coming from meteo france API (BUFR files and HDF5 files)
Those are images files that we can convert to numpy arrays

- Ground station data coming from meteo france API (CSV files)
Those are CSV files that we can convert to pandas dataframes

- ERA5 data coming from ECMWF API (NetCDF files)
Those are NetCDF files that we can convert to xarray dataarrays

- (POSSIBLY) satellite data coming from EUMETSAT API (NetCDF files)
But currently I'm not sure of the availability of this data

#### Data part : download the data every day to create a database

The key idea is to use machine learning to predict the weather a few hours / days in advance.
So we need to download the data every day to create a database (no existant yet).

### Global Planning

1. Check / visual / preprocess radar data to see what's going on (valuable data ?)
H5 data is OK
BUFR FILE OK
First step is OK
2. Create the pipeline to download the data every days to create a historical dataset
Airflow ? simple API call with openAPI ?
- [x] Make the function to call the MF API, save only france data (2 files so for radar and record for ground station data)
- [x] Put those function in a airflow to automate the process (in a dags)
	- [x] Download and preprocess
	- [x] Add push to bucket (digital ocean)
- [x] Debug the whole thing locally
- [x] Put the docker in the registery and test the thing with scheduler to automate the downloading
	- [x] Add the container image in the registery
	- [x] Create the GCP cloud run
	- [x] Create the scheduler
	- [ ]
- [ ] Wait 2 months to get the data
- [ ] Create the pipeline to preprocess the whole dataset (in order to create a dataset element in HF)






