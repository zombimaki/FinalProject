# Minneapolis Police Incident Analysis
The goal of this project was use crime incident data from 2010-2020 to develop machine learning models that could be used to predict crime incident rates in the future.

Analysis can be viewed by clicking [HERE](https://mrbadinger.github.io/Minority_Report/index.html)

## Models
1. b_model.ipynb<br>
a. Tests features in a naive bayes model and a deep learning neural network model<br>
2. b_prophet.ipynb<br>
a. Uses fbprophet library to analyze incident data and develop a forecast<br>
b. Outputs trend by year and by week of the year for analysis<br>
c. Outputs interactive plotly reports as html<br>
1. b_time_series_final.ipynb<br>
a. Uses simple moving average to develop trend models for weekly incident forecasts<br>
b. Evaluates total incident count, incidents by neighborhood, and incidents by offense<br>
1. b_time_series_test.ipynb<br>
a. Notebook used to test variations on simple moving average forecasting<br>
5. randomforest_abp.ipynb<br>
a. Random Forest model to predict ucrCode<br>
b. Generates a Top 10 Features barchart<br>
c. Generates a Tree Plot of the model<br>
d. Performs hyperparameter tuning using GridSearchCV.<br>
6. GJeter_RFM_highest_crime_neighborhood.ipynb<br>
a. Random forest model focused on the highest crime rate neighborhood in Minneapolis - Downtown West<br>
7. GJeter_RFM_nieghborhood.ipynb<br>
a. Random forest model to identify in which neighborhood crime is most likely to occur.<br>

## Visualizations
1. Tableau Crime Rate Story<br>
a. Visualizes crime trends for each UCR category <br>
2. Tableau Crime Heat Map<br>
a. Heat map that shows crime density by year for each UCR category<br>
3. Leaflet.js Cluster Group Map<br>
a. Loads Data from the GeoIncident.json file created by the csv_geojson.py app.<br>
b. Loads Minneapolis neighborhood shape data from the Minneapolis_Neighborhoods.geojson file which was downloaded from opendata.minneapolismn.gov.<br>
c. Creates a ClusterGroup of the incident markers<br>
d. Creates a polyline of the neighborhood markers<br>
e. Marker includes case number, neighborhood, crime, and date of incident popup.<br>

## Misc
1. incident_data/data_clean.ipynb <br>
a. Cleans the incident csv files and combines them into one csv file.<br>
2. b_eda.ipynb<br>
a. Imports incidents file for exploratory data analysis to identify trends in the data<br>
3. csv_geojson.py<br>
a. Creates a geojson file of the combined incident data.<br>
4. csv_to_html.ipynb<br>
a. Creates html files of interactive Plotly visualizations.<br>

## Links
[Open Data Minneapolis](https://opendata.minneapolismn.gov/)<br>
[Incident Analysis on Tableau Public](https://public.tableau.com/profile/michael.badinger#!/vizhome/MinorityReport_16150552609400/CrimeHeatMap)<br>

