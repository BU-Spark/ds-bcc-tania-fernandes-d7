# Data Analysis Notebooks

This folder contains Jupyter notebooks utilized for comprehensive data analysis. Each notebook is designed to address specific aspects of the analysis process and provide insights based on the data. Below is a brief description of each notebook included in this folder:

## Notebook Descriptions

- **approved-building-permit-cleaning.ipynb**: Use address fields, such as street number, street name, street suffixes, and other measures to join
  the Boston SAM dataset to produce coordinates that can be used to plot against a shapefile for determining whether an approved permit is for a property
  in District 7. This file export a ready-to-use dataset called `approved-building-permit-cleaned.csv` to the `data` folder.

- **approved-building-permits.ipynb**: Analyzes building permits data, including data cleaning, preprocessing, exploratory data analysis, and the trends of permit work types and occupancy types.

- **census-data.ipynb**: This is the preliminary file that worked with the Census datasets. It contained some initial preprocessing of the datasets. d7-CensusData.ipynb is a more current version that contains preprocessing along with early analysis.

- **demographic-breakdown-boston-city.ipynb**: Downloads, cleans and aggregates the demographic wise disaggregated information for Boston owned vs. rented housing units. Prepared a final file to upload to LookerStudio for visualizations.

- **demographic-breakdown-district-7.ipynb**: Downloads, cleans and aggregates the demographic wise disaggregated information for District 7 owned vs. rented housing units. Prepared a final file to upload to LookerStudio for visualizations.

- **income-restricted-housing.ipynb**: Analyzes income-restricted housing. Covers data cleaning, evaluates housing availability and growth, and examines the impact of Section 8 benefits.

- **property-dataset-cleaning.ipynb**: Find coordinate for the property by matching the address fields to Boston SAM dataset and Boston ZIP Code shapefile. This file export a ready-to-use dataset called `property-cleaned.csv` in the `data` folder.

- **property.ipynb**: Analyzes property data. Includes data preprocessing, exploratory data analysis (EDA), and examines property prices and property taxes trends.

- **pulse-survey.ipynb**: Data from Household Pulse Survey (HPS) collected by census.gov that provides insight into property tenure, rent or mortgage on-time or late payment, eviction, and foreclosure, filtered only for surveys answered by Massachusetts' residents. The priority for this analysis has been downgraded due to recommendation from Spark and is not included in the visualization.

- **rentsmart.ipynb**: Analyzes inspectional services data, including data cleaning, preprocessing, exploratory data analysis, and the patterns of violations and properties.

- **selected-housing-characteristics**: Contains a Boston vs. District 7 comparison for selecting housing characteristics like median rent.
