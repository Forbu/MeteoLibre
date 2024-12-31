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






