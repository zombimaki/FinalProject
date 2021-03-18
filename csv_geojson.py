import pandas as pd
from collections import OrderedDict 
import json
from geojson import Feature, FeatureCollection, Point

# define the path to the combined incident csv
all_incidents_csv = "incident_data/yearly_incident_data/all_incidents.csv"

# Import the csv file into data frame
all_incidents_df = pd.read_csv(all_incidents_csv, encoding="utf-8",low_memory=False)

all_incidents_df = all_incidents_df.fillna('')

def load_mpls_incidents():
# create a list to hold the geo data dictionaries
    geoList = []

    # loop through the df to create the list dictionaries to be added to our list
    for index, row in all_incidents_df.iterrows():
        lat = row[6]
        lon = row[7]
        caseNumber = row[1]
        description = row[4]
        neighborhood = row[8]
        incidentDate = row[9]

        latitude, longitude = map(float, (lat, lon))
        geoList.append(
            Feature(
                geometry = Point((lon, lat)),
                properties = {
                    'caseNumber': caseNumber,
                    'description': description,
                    'neighborhood':neighborhood,
                    'incidentDate': incidentDate
                }
            )
        )

    collection = FeatureCollection(geoList)

    #export to the yearly incident data folder
    with open('Resources/GeoIncident.json', 'w') as f:
                f.write('%s' % collection)

   # return geoList
