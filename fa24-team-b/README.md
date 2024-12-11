# District 7 Housing Indicators

![image](https://github.com/user-attachments/assets/d8a4d7fb-f9ae-4599-b70d-f63d7177de4f)

## Overview

The primary objective is to generate actionable insights for District 7 to drive impactful policies for D7. This includes understanding which residents are experiencing improvements in their quality of life, what specific areas are improving, and how these trends compare to other Boston districts and the city as a whole.

## Goal

This project focuses on analyzing the the housing performance in District 7 (D7) compared to rest of the city. Our analysis will help the district shape the "District 7 Action Plan," a data-driven initiative to address economic and social challenges in the district.

## Key Features

- Tabular Data Analysis: Employs tabular data to obtain insights from trends in the data
- Time-Series Analysis: Shows changes over time to identify long-term patterns and shifts
- Housing Market Assessment: Evaluates affordability, availability, rent, violations, and constructions

Our aim is to create a tool helps the district address economic and social challenges in housing, contributing to better housing outcomes for District 7 residents.

## Datasets

### U.S. Census Bureau: ACS Demographic and Housing Estimates

The American Community Survey (ACS) helps local officials, community leaders, and businesses understand the changes taking place in their communities. It is the premier source for detailed population and housing information about our nation.

More info can be found here: [link](https://data.census.gov/table?q=demographics&g=050XX00US36103_160XX00US4159000)

### U.S. Census Bureau: ACS Selected Housing Characteristics

More specifically, we referred to the DP04 Selected Housing Characteristics Table, where we filtered out Place > Massachussetts > Boston City to get information for Boston, and selected the relevant census tracts to get information for District 7. This table contained information for The Total Housing Units
More info can be found here: [link](https://data.census.gov/table/ACSDP5Y2022.DP04?q=housing%20tenure&t=Housing%20Units&g=1400000US25025010206,25025010300,25025010403,25025010404,25025010405,25025010500,25025010600,25025010701,25025070502,25025070600,25025070700,25025070801,25025070802,25025070901,25025070902,25025071101,25025080100,25025080300,25025080401,25025080601,25025080801,25025081301,25025081302,25025081400,25025081500,25025081700,25025081800,25025081900,25025082000,25025082100,25025090300,25025090400,25025090600,25025091300,25025091400,25025120201,25025120301,25025980300&moe=false)

### Property Assessment

Gives property, or parcel, ownership together with value information, which ensures fair assessment of Boston taxable and non-taxable property of all types and classifications.
More info can be found here: [link](https://data.boston.gov/dataset/property-assessment)

### Income-Restricted Housing Inventory

This data, maintained by the Mayor’s Office of Housing (MOH), is an inventory of all income-restricted units in the city. This data includes public housing owned by the Boston Housing Authority (BHA), privately- owned housing built with funding from DND and/or on land that was formerly City-owned, and privately-owned housing built without any City subsidy, e.g., created using Low-Income Housing Tax Credits (LIHTC) or as part of the Inclusionary Development Policy (IDP).
More info can be found here: [link](https://data.boston.gov/dataset/income-restricted-housing)

### RentSmart

RentSmart Boston compiles data from BOS:311 and the City's Inspectional Services Division to give prospective tenants a more complete picture of the homes and apartments they are considering renting, assisting them in understanding any previous issues with the property, including: housing violations, building violations, enforcement violations, housing complaints, sanitation requests, and/or civic maintenance requests.
More info can be found here: [link](https://data.boston.gov/dataset/rentsmart)

### Approved Building Permit

Building permits help to establish compliance of construction work with the minimum standards of safety established by the State Building Code to ensure public health and safety for everyone. A building permit is required before beginning most construction, demolition, modification and repair work. The Inspectional Services Department offers permitting processes tailored for a wide variety of projects, from home repairs to building demolition.
More info can be found here: [link](https://data.boston.gov/dataset/approved-building-permits)

### Boston SAM

City of Boston’s Street Address Management (SAM) system containing Boston addresses and their coordinates.
More info can be found here: [link](https://data.boston.gov/dataset/approved-building-permits)

### 2020 Census Tract in Boston

This is a shapefile that contains the polygons that draw geographical boundaries for 2020 census tracts in Boston as defined by the United States Census Bureau.
More info can be found here: [link](https://hub.arcgis.com/datasets/boston::2020-census-tracts-in-boston/about)

### BPDA Neighborhood Boundaries

This is a shapefile that contains the polygons that draw geographical boundaries for neighborhoods in Boston as defined by Boston Planning & Development Agency (BPDA).
More info can be found here: [link](https://data.boston.gov/dataset/bpda-neighborhood-boundaries)

### City Council District

This is a shapefile that contains the polygons that draw geographical boundaries for city council districts for 2023-2031 municipal elections in Boston as passed by the City Council on May 24th, 2023.
More info can be found here: [link](https://data.boston.gov/dataset/city-council-districts-2023-2032)

### D7 Catchment Area

This is a shapefile that is converted from a KML file given to us by the client in order to break down District 7 into smaller residential areas such as neighborhood associations.

### Household Pulse Survey

The Household Pulse Survey is a 20-minute online survey that measures how emergent social and economic issues are impacting households across the country. Among these questions are questions about eviction, foreclosure, whether the surveyee owns or rents their property, and whether the surveyee is behind on rent and mortgage.
More info can be found here: [link](https://www.census.gov/programs-surveys/household-pulse-survey/data/datasets.html)

### ZIP Codes

This shapefile contains ZIP codes within the City of Boston. This data does not include every ZIP code in Boston as some ZIP codes don't have geography. For example 02201 (City Hall).
More info can be found here: [link](https://data.boston.gov/dataset/zip-codes)

These datasets enable a thorough and nuanced analysis of District 7's unique challenges and opportunities, particularly in the areas of housing, economic development, and community demographics.

## Quick Start

### Requirements

We recommend setting up a virtual environment with all the necessary packages. Run the following command in the terminal:

```
# Create and activate a virtual environment.
python3 -m venv .venv
source .venv/bin/activate
pip install --upgrade pip

# Install all required dependencies
pip install -r requirements.txt
```

## Modules Overview

<pre>
`housing`
   |
   |- `data`: contains the datasets and shapefiles used in this project
   |    |
   |    |- `Data folders`: datasets that are put into different files by the distributors are put in folders
   |    |   
   |    |- `Data files`: datasets that are contain in individual files
   |
   |- `notebooks`: jupyter notebooks for data cleaning, analysis, visualizations, and insights. Each dataset will have its own                     notebooks.
</pre>

## Project Timeline

### Key Steps and Deliverables:

1. **Define District Boundaries:**

   - Establish D7 boundaries using a shapefile and map census tracts/block groups to D7.

2. **Initial Data Collection and Indicator Selection:**

   - Choose key indicators for housing, focusing on home values, home ownership vs. rent, rent burden, housing violations/complaints/requests, and new housing permits.

3. **Prototype and Initial Analysis:**

   - Create a subset of data for 1–2 indicators (such as median household income) to present as a prototype to the client. Get feedback on the presentation format and indicators. Identify the client's priority for the deliverable.

4. **Iterative Analysis and Client Feedback:**

   - Present findings periodically, adjusting based on client feedback. Focus on highlighting trends over time (ideally the last 10 years) and comparisons between D7 and Boston.

5. **Final Deliverable:**
   - A dashboard showing current and historical data across various indicators along with conparison against Boston city, with a focus on housing.
   - Documentation of all steps in data collection and analysis for reproducibility.

## Tools and Platforms:

- Analysis: Pandas, GeoPandas, Matplotlib.
- Visualization: Google LookerStudio.

## Challenges

- Absence of a specific client or clear expectations, which made it difficult to tailor the analysis to meet stakeholder needs.
- Ambiguous definition of District 7’s geographic boundaries complicate efforts to isolate data specific to this area. Many datasets lacked detailed spatial information, such as precise geolocation or neighborhood identifiers, reducing our ability to conduct in-depth geographic analysis, especially for Income-Restricted Housing dataset which does not contain street address or significant geographical information that can be used to look for coordinates. We overcomes this chalenge by using shapefiles, a file format commonly used for geographic information system data. By joining geographical columns such as coordinates with the City Council District shapefile, we can label each address as either in District 7 or otherwise. However, not all datasets contained coordinates that could be plotted against the shapefile. We joined these datasets with Boston’s Live Street Address Management dataset, which contains a growing list of known addresses in Boston, to obtain the necessary coordinates before joining the coordinates with the City Council District shapefile.
- Creating a dashboard using Looker Studio posed limitations, as its data manipulation capabilities were insufficient for creating more advanced and interactive visualizations.

## Recommendations for Next Steps

To overcome challenges and enhance future analyses, several steps are recommended. First, clearly defining the scope of the project by engaging stakeholders early on will help align objectives and deliverables with their expectations. Additionally, sourcing more comprehensive datasets, particularly those with robust spatial and temporal information, will fill critical gaps in the analysis. Collaborating with local authorities or using GIS tools to clarify District 7’s geographic boundaries will also improve the precision of location-specific insights. To address visualization challenges, migrating to more advanced tools such as Tableau is strongly recommended. This would allow for the creation of a unified dashboard that explores key characteristics, such as median rent, racial and age group diversity, and the availability of income-restricted housing, while comparing District 7 metrics against Boston averages. Including markers for such comparisons will provide valuable context and insights for stakeholders. Finally, ensuring proper documentation of processes will improve reproducibility and serve as a foundation for future projects.
