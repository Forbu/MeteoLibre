import cdsapi

dataset = "reanalysis-era5-pressure-levels"
request = {
    "product_type": ["reanalysis"],
    "variable": [
        "fraction_of_cloud_cover",
        "potential_vorticity",
        "relative_humidity",
        "specific_humidity",
        "specific_rain_water_content",
        "temperature",
        "v_component_of_wind",
        "vorticity"
    ],
    "year": [
        "2015", "2016", "2017",
        "2018", "2019", "2020",
        "2021", "2022"
    ],
    "month": [
        "01", "02", "03",
        "04", "05", "06",
        "07", "08", "09",
        "10", "11", "12"
    ],
    "day": [
        "01", "02", "03",
        "04", "05", "06",
        "07", "08", "09",
        "10", "11", "12",
        "13", "14", "15",
        "16", "17", "18",
        "19", "20", "21",
        "22", "23", "24",
        "25", "26", "27",
        "28", "29", "30",
        "31"
    ],
    "time": ["00:00"],
    "pressure_level": ["1000"],
    "data_format": "grib",
    "download_format": "zip",
    "area": [51, -5, 42, 9]
}

client = cdsapi.Client()
client.retrieve(dataset, request).download()