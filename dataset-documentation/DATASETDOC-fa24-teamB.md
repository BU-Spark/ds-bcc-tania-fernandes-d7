**_Project Information_**

- What is the project name?

  Boston D7 Indicators - Housing

- What is the link to your project’s GitHub repository?

  https://github.com/BU-Spark/ds-boston-d7-indicators/tree/district7_teamB

- What is the link to your project’s Google Drive folder? \*\*\*This should be a Spark\! Owned Google Drive folder \- please contact your PM if you do not have access\*\*\*

https://drive.google.com/drive/u/1/folders/1fnyphU2CSEh2fDduT41LHJ1Pn1RzRHIW

- In your own words, what is this project about? What is the goal of this project?

  This project focuses on analyzing the the housing performance in District 7 (D7) compared to rest of the city. Our analysis will help the district shape the "District 7 Action Plan," a data-driven initiative to address economic and social challenges in the district.

- Who is the client for the project?

  Boston Councilor’s Office

- Who are the client contacts for the project?

  angelique.brutus@boston.gov

- What class was this project part of?

  DS701: Tools for Data Science, Fall 2024

**_Dataset Information_**

- What data sets did you use in your project? Please provide a link to the data sets, this could be a link to a folder in your GitHub Repo, Spark\! owned Google Drive Folder for this project, or a path on the SCC, etc.

  https://github.com/BU-Spark/ds-boston-d7-indicators/tree/district7_teamB/fa24-team-b/housing/data

- Please provide a link to any data dictionaries for the datasets in this project. If one does not exist, please create a data dictionary for the datasets used in this project.

U.S. Census Bureau: ACS Demographic and Housing Estimates: [link](https://data.census.gov/table?q=demographics&g=050XX00US36103_160XX00US4159000) (in the Note tab)

U.S. Census Bureau: ACS Selected Housing Characteristics: [link](https://data.census.gov/table/ACSDP5Y2022.DP04?q=housing%20tenure&t=Housing%20Units&g=1400000US25025010206,25025010300,25025010403,25025010404,25025010405,25025010500,25025010600,25025010701,25025070502,25025070600,25025070700,25025070801,25025070802,25025070901,25025070902,25025071101,25025080100,25025080300,25025080401,25025080601,25025080801,25025081301,25025081302,25025081400,25025081500,25025081700,25025081800,25025081900,25025082000,25025082100,25025090300,25025090400,25025090600,25025091300,25025091400,25025120201,25025120301,25025980300&moe=false)

Property Assesment: [link](https://data.boston.gov/dataset/property-assessment)

Income-Restricted Housing: [link](https://data.boston.gov/dataset/income-restricted-housing)

2020 Census Tracts in Boston: [link](https://hub.arcgis.com/datasets/boston::2020-census-tracts-in-boston/about)

The following dataset does not provide a data dictionary. We will describe them by providing a dictionary on relevant columns that are used as a part of the analysis.

**RentSmart**
| Column Name | Data Type | Description |
|---|---|---|
| `date` | Date | The date when the violation occurred or was recorded. |
| `violation_type` | String | The type of violation reported (e.g., violations, complaints, requests). |
| `description` | String | Detailed description of the violation or issue. |
| `address` | String | The street address and ZIP code of the property where the violation occurred. |
| `neighborhood` | String | The neighborhood where the property is located. |
| `property_type` | String | The type of property (e.g., residential, commercial, mixed-use). |
| `latitude` | Float | The latitude coordinate of the property's location. |
| `longitude` | Float | The longitude coordinate of the property's location. |

**Live Street Address Management (SAM) Addresses**
| Column Name | Data Type | Description |
|---|---|---|
| `FULL_ADDRESS` | String | The complete address, including street number, street name, and unit number. |
| `FULL_STREET_NAME` | String | The full name of the street, including any prefixes or suffixes. |
| `STREET_BODY` | String | The main portion of the street name, excluding prefixes or suffixes. |
| `POINT_X` | Float | The X coordinate (longitude) of the address location in the spatial reference system. |
| `POINT_Y` | Float | The Y coordinate (latitude) of the address location in the spatial reference system. |

- What keywords or tags would you attach to the data set?

  - Domain(s) of Application: Computer Vision, Object Detection, OCR, Image Classification, Image Segmentation, Facial Recognition, NLP, Topic Modeling, Sentiment Analysis, Named Entity Recognition, Text Classification, Summarization, Anomaly Detection, Other

  - Sustainability, Health, Civic Tech, Voting, Housing, Policing, Budget, Education, Transportation, etc.

boston housing, housing violations, 311 service request, inspectional service, spatial analysis, policy-making

_The following questions pertain to the datasets you used in your project._  
_Motivation_

- For what purpose was the dataset created? Was there a specific task in mind? Was there a specific gap that needed to be filled? Please provide a description.

The ACS datasets by U.S. Census Bureau are created for the purpose of tracking changes taking place in American cumminuties. Datasets on Boston housings are published for transparency in fair assessment of property values and taxes, establish compliance of construction work, and give prospective tenants a more complete picture of the homes and apartments they are considering renting.

_Composition_

- What do the instances that comprise the dataset represent (e.g., documents, photos, people, countries)? Are there multiple types of instances (e.g., movies, users, and ratings; people and interactions between them; nodes and edges)? What is the format of the instances (e.g., image data, text data, tabular data, audio data, video data, time series, graph data, geospatial data, multimodal (please specify), etc.)? Please provide a description.

All our datasets are tabular data, geospatial data, or survey data, which is divided into 3 categories:

- Housing: Properties, addresses, violations, housing units, housing restrictions, building permits.
- Geospatial: Census tracts, neighborhood boundaries, council districts.
- Community: Demographic surveys.

- How many instances are there in total (of each type, if appropriate)?

We have more than 1 million instances of tabular data points and around hundreds of geospatial data points.

- Does the dataset contain all possible instances or is it a sample (not necessarily random) of instances from a larger set? If the dataset is a sample, then what is the larger set? Is the sample representative of the larger set? If so, please describe how this representativeness was validated/verified. If it is not representative of the larger set, please describe why not (e.g., to cover a more diverse range of instances, because instances were withheld or unavailable).

The datasets contain all possible instances known to the distributor.

- What data does each instance consist of? “Raw” data (e.g., unprocessed text or images) or features? In either case, please provide a description.

Housing data consists of a mix of raw data, such as address, number of rooms, property values, and violations, while ACS datasets consists of features as the field values have already been aggregated to show the count of survey answers.

- Is there any information missing from individual instances? If so, please provide a description, explaining why this information is missing (e.g., because it was unavailable). This does not include intentionally removed information, but might include redacted text.

Some datasets that span multiple years, such as RentSmart, contain very few data points in 2019 because it is the first year when the collection happens and therefore have not seenmuch data collected. Income-Reistricted Housing Inventory dataset doesn't provide the data from 2019.

- Are there recommended data splits (e.g., training, development/validation, testing)? If so, please provide a description of these splits, explaining the rationale behind them

No applicable to our project since we're only analysis the data.

- Are there any errors, sources of noise, or redundancies in the dataset? If so, please provide a description.

We noticed that the tax value in Property Assessment from 2019 is not properly formatted, so it is showing improper amount that sometimes exceed the total property values. We manually verify the values of some data points and discover that the column is simply missing a demical dot.

- Is the dataset self-contained, or does it link to or otherwise rely on external resources (e.g., websites, tweets, other datasets)? If it links to or relies on external resources,
  - Are there guarantees that they will exist, and remain constant, over time;
  - Are there official archival versions of the complete dataset (i.e., including the external resources as they existed at the time the dataset was created)?
  - Are there any restrictions (e.g., licenses, fees) associated with any of the external resources that might apply to a dataset consumer? Please provide descriptions of all external resources and any restrictions associated with them, as well as links or other access points as appropriate.

The dataset is self-contained. Since effort has been put to regularly update the dataset and other authoritative web applications hosted on Boston city's website also use the same datasets, we expect that the dataset will exist for a long time since effort has been put to regularly update the dataset.

- Does the dataset contain data that might be considered confidential (e.g., data that is protected by legal privilege or by doctor-patient confidentiality, data that includes the content of individuals’ non-public communications)? If so, please provide a description.

All data are made public and with no license.

- Does the dataset contain data that, if viewed directly, might be offensive, insulting, threatening, or might otherwise cause anxiety? If so, please describe why.

No.

- Is it possible to identify individuals (i.e., one or more natural persons), either directly or indirectly (i.e., in combination with other data) from the dataset? If so, please describe how.

Yes. Some datasets for housings contain the name of property owner and the address where they can be contacted, however, we did not include such information in our analysis or dashboard.

- Dataset Snapshot, if there are multiple datasets please include multiple tables for each dataset.

1. RentSmart
   | Size of dataset | 79.7 M |
   | :------------------ | :-- |
   | Number of instances | 344553 |
   | Number of fields | 13 |
   | Labeled classes | 5 |
   | Number of labels | 431 |

2. 2020 Census Tracts in Boston
   | Size of dataset | 398 KB |
   | :------------------ | :-- |
   | Number of instances | 206 |
   | Number of fields | 14 |
   | Labeled classes | 4 |
   | Number of labels | 4 |

3. BDPA Neighborhood Boundary
   | Size of dataset | 561 KB |
   | :------------------ | :-- |
   | Number of instances | 26 |
   | Number of fields | 8 |
   | Labeled classes | 0 |
   | Number of labels | 0 |

4. City Council District
   | Size of dataset | 131 KB |
   | :------------------ | :-- |
   | Number of instances | 9 |
   | Number of fields | 15 |
   | Labeled classes | 0 |
   | Number of labels | 0 |

5. D7 Catchment Area
   | Size of dataset | 106 KB |
   | :------------------ | :-- |
   | Number of instances | 27 |
   | Number of fields | 4 |
   | Labeled classes | 0 |
   | Number of labels | 0 |

6. Household Pulse Survey
   | Size of dataset | 2.23 GB |
   | :------------------ | :-- |
   | Number of instances | 2837902 |
   | Number of fields | 661 |
   | Labeled classes | 557 |
   | Number of labels | 7757 |

7. ZIP Code
   | Size of dataset | 299 KB |
   | :------------------ | :-- |
   | Number of instances | 43 |
   | Number of fields | 5 |
   | Labeled classes | 0 |
   | Number of labels | 0 |

8. Boston Street Address Management (SAM) Addresses
   | Size of dataset | 119.2 MB |
   | :------------------ | :-- |
   | Number of instances | 400196 |
   | Number of fields | 32 |
   | Labeled classes | 4 |
   | Number of labels | 335 |

_Collection Process_

- What mechanisms or procedures were used to collect the data (e.g., API, artificially generated, crowdsourced \- paid, crowdsourced \- volunteer, scraped or crawled, survey, forms, or polls, taken from other existing datasets, provided by the client, etc)? How were these mechanisms or procedures validated?

With the exeption of D7 Catchment Area, all datasets are directly sourced and downloaded from U.S. Census Bureau and Analyze Boston. D7 Catchment Area is a Google Map link with geometry overlay provided to us by the client.

- If the dataset is a sample from a larger set, what was the sampling strategy (e.g., deterministic, probabilistic with specific sampling probabilities)?

Not applicable to our project.

- Over what timeframe was the data collected? Does this timeframe match the creation timeframe of the data associated with the instances (e.g., recent crawl of old news articles)? If not, please describe the timeframe in which the data associated with the instances was created.

The datasets are collected over the time period of 2014 - 2024, with the starting year varied by dataset.

_Preprocessing/cleaning/labeling_

- Was any preprocessing/cleaning/labeling of the data done (e.g., discretization or bucketing, tokenization, part-of-speech tagging, SIFT feature extraction, removal of instances, processing of missing values)? If so, please provide a description. If not, you may skip the remaining questions in this section.

We rename columns from the same dataset collected over different years because the source data rename columns multiple times. We also impute missing geographical field by joining the address with Boston SAM to get the coordinate, which is then used to plot against City Council District shapefile to determine District 7.

- Were any transformations applied to the data (e.g., cleaning mismatched values, cleaning missing values, converting data types, data aggregation, dimensionality reduction, joining input sources, redaction or anonymization, etc.)? If so, please provide a description.

We convert data types, especially those that stems from loading CSV data. For example, ZIP code is being loaded as a numeric value, which we convert to strings. All step regarding data cleaning is explained in detail in each notebook.

- Was the “raw” data saved in addition to the preprocessed/cleaned/labeled data (e.g., to support unanticipated future uses)? If so, please provide a link or other access point to the “raw” data, this could be a link to a folder in your GitHub Repo, Spark\! owned Google Drive Folder for this project, or a path on the SCC, etc.

The raw data is provided in: [link](https://github.com/BU-Spark/ds-boston-d7-indicators/tree/district7_teamB/fa24-team-b/housing/data). Datasets that are exported to a file as a result of cleaning the raw dataset is in the format `*-cleaned.csv`

- Is the code that was used to preprocess/clean the data available? If so, please provide a link to it (e.g., EDA notebook/EDA script in the GitHub repository).

Some preprocessing are done in separate notebooks instead of inside EDA notebook if the process is extensive.
**Approved Building Permit**: [link](https://github.com/BU-Spark/ds-boston-d7-indicators/blob/district7_teamB/fa24-team-b/housing/notebooks/approved-building-permit-cleaning.ipynb)
**Property Assessment**: [link](https://github.com/BU-Spark/ds-boston-d7-indicators/blob/district7_teamB/fa24-team-b/housing/notebooks/property-dataset-cleaning.ipynb)

All other preprocessing are in EDA notebooks in `notebooks` directory: [link](https://github.com/BU-Spark/ds-boston-d7-indicators/tree/district7_teamB/fa24-team-b/housing/notebooks).

_Uses_

- What tasks has the dataset been used for so far? Please provide a description.

The datasets have been used to provide insights in housing dempgraphics, property value, rent burden, housing violations, and housing construction in District 7. The cleaned datasets are also used to visualize the dashboard.

- What (other) tasks could the dataset be used for?

Public policy evaluation and advocacy can benefit from insights into eviction risks, housing instability, and the impact of policy changes. Advanced machine learning models can predict violations, classify neighborhoods, and cluster areas based on socio-economic factors. Additionally, the dataset supports academic research in urban sociology and environmental justice, while enabling businesses to identify investment opportunities and optimal locations. Overall, it provides a robust foundation for diverse analytical, predictive, and decision-making tasks.

- Is there anything about the composition of the dataset or the way it was collected and preprocessed/cleaned/labeled that might impact future uses?

Some property are dropped from the table if coordinates cannot be found from Boston SAM because we cannot know for sure if they are in District 7.

- Are there tasks for which the dataset should not be used? If so, please provide a description.

The dataset should not be used for tasks that could breach privacy, perpetuate biases, or lead to unethical outcomes. It is unsuitable for identifying or profiling individuals, surveillance, predictive policing, or drawing conclusions about populations outside Boston District 7. Additionally, it should not be applied to health-related research, financial or credit assessments, or predictions of criminal behavior, as it lacks the necessary data and context. Using the dataset for punitive enforcement without considering socio-economic factors could harm vulnerable populations. Responsible use within its intended scope is essential to avoid misuse or harm.

_Distribution_

- Based on discussions with the client, what access type should this dataset be given (eg., Internal (Restricted), External Open Access, Other)?

The dataset used are all public, and the client expresses interest in including our dashboard in their website, which will be public. We believe that the dataset included, aside from the D7 Catchment Area, which was provided by the client themselves, can be public.

_Maintenance_

- If others want to extend/augment/build on/contribute to the dataset, is there a mechanism for them to do so? If so, please provide a description.

Our datasets are available in the `data` folder of our GitHib.

_Other_

- Is there any other additional information that you would like to provide that has not already been covered in other sections?

No.
