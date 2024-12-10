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
`housing`

   |- `data`: contains the datasets and shapefiles used in this project
         |- `Data folders`: datasets that are put into different files by the distributors are put in folders
         |- `Data files`: datasets that are contain in individual files
   |- `notebooks`: jupyter notebooks for data cleaning, analysis, visualizations, and insights. Each dataset will have its own                     notebooks.

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
