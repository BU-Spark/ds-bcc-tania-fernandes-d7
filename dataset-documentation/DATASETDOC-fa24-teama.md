***Project Information*** 

* What is the project name?

D7 Indicators Project


* What is the link to your project’s GitHub repository?

https://github.com/BU-Spark/ds-boston-d7-indicators


* What is the link to your project’s Google Drive folder? \*\**This should be a Spark\! Owned Google Drive folder \- please contact your PM if you do not have access\*\**

https://drive.google.com/drive/u/1/folders/1fnyphU2CSEh2fDduT41LHJ1Pn1RzRHIW


* In your own words, what is this project about? What is the goal of this project?

The project aims to analyze population and economic metrics for District 7 to understand factors that directly impact the way of life and vibrancy for the people of D7, and help policymakers make decisions that can contribute towards development.


* Who is the client for the project?

Boston Councilor’s Office


* Who are the client contacts for the project?

angelique.brutus@boston.gov


* What class was this project part of?

This project was a part of the DS701: Tools for Data Science class for Fall 2024.



***Dataset Information***

* What data sets did you use in your project? Please provide a link to the data sets, this could be a link to a folder in your GitHub Repo, Spark\! owned Google Drive Folder for this project, or a path on the SCC, etc.

We worked on census data for the population metric, sourced directly from the US Census (https://www.census.gov/) which is available open source. For the Economic development data, we utilized datasets from Analyze Boston (https://data.boston.gov/).  
Link to raw datasets: https://github.com/BU-Spark/ds-boston-d7-indicators/tree/district7-fa24-team-a/fa24-team-a/Datasets
Link to processes datasets: https://github.com/BU-Spark/ds-boston-d7-indicators/tree/district7-fa24-team-a/fa24-team-a/Dashboard-data


* Please provide a link to any data dictionaries for the datasets in this project. If one does not exist, please create a data dictionary for the datasets used in this project. **(Example of data dictionary)**

Population (US Census): The data dictionary can be found in the ‘Notes’ tab for each dataset.
1. Race: https://data.census.gov/table/ACSDP5Y2022.DP05?q=demographics&g=050XX00US36103_160XX00US4159000, https://data.census.gov/table?q=demographics&g=050XX00US36103_160XX00US4159000
2. Age: https://data.census.gov/table?q=demographics&g=050XX00US36103_160XX00US4159000
3. Poverty: https://data.census.gov/table/ACSST1Y2023.S1701?q=Poverty rate&g=050XX00US36103_160XX00US4159000
4. Education Attainment: https://data.census.gov/table?q=education&t=Fertility&g=050XX00US25025
5. Median Household Income: https://data.census.gov/table?q=household income

Economic Development (Analyze Boston): The data dictionaries for all datasets are reference below.

1. Certified Businesses: https://data.boston.gov/dataset/certified-business-directory
2. Licenses: https://data.boston.gov/organization/consumer-affairs-and-licensing-department-org, https://data.boston.gov/organization/boston-licensing-board
3. BIPOC jobs: https://data.boston.gov/dataset/boston-jobs-policy-compliance-reports/resource/5ab4b4de-c970-4619-ab55-ce4338535b24


* What keywords or tags would you attach to the data set?  
  * Domain(s) of Application: Computer Vision, Object Detection, OCR, Image Classification, Image Segmentation, Facial Recognition, NLP, Topic Modeling, Sentiment Analysis, Named Entity Recognition, Text Classification, Summarization, Anomaly Detection, Other   
  * Sustainability, Health, Civic Tech, Voting, Housing, Policing, Budget, Education, Transportation, etc. 

The datasets come under Policy Making (Sustainability) along with Population and Displacement, Economic Development and Displacement.



*The following questions pertain to the datasets you used in your project.*   
*Motivation* 

* For what purpose was the dataset created? Was there a specific task in mind? Was there a specific gap that needed to be filled? Please provide a description.

The datasets were created to provide a comprehensive understanding of the population demographics, socioeconomic conditions, and economic development trends in District 7 and Boston City overall. Its primary purpose is to address critical gaps in understanding the disparities and progress between District 7 and the broader city, particularly in terms of income inequality, poverty reduction, education attainment, and business vibrancy. By capturing granular data such as race and ethnicity distributions, licensing trends, and BIPOC workforce statistics, the datasets enable targeted analysis of equity and growth within these communities. It fills gaps in understanding how demographic changes, business growth, and licensing policies influence economic outcomes and equity. The inclusion of geospatial data for businesses and events adds a layer of location-based insights, making the dataset particularly valuable for spatial analysis and resource allocation.



*Composition*

* What do the instances that comprise the dataset represent (e.g., documents, photos, people, countries)? Are there multiple types of instances (e.g., movies, users, and ratings; people and interactions between them; nodes and edges)? What is the format of the instances (e.g., image data, text data, tabular data, audio data, video data, time series, graph data, geospatial data, multimodal (please specify), etc.)? Please provide a description.

The instances in the dataset represent tabular records, with each instance capturing specific details about either population demographics or economic development data. For the population data, instances represent demographic groups or subgroups, such as age groups (e.g., residents aged 65+), racial or ethnic categories (e.g., White, Asian, Black), and socioeconomic conditions (e.g., households below the poverty line, educational attainment levels). For the economic development data, instances represent individual businesses, licenses (e.g., cannabis, alcohol), events (e.g., cultural gatherings, entertainment), or workforce statistics (e.g., number of BIPOC jobs created). The dataset includes multiple types of instances, such as population groups, business licenses, and events, but all are presented in a structured tabular format with rows corresponding to instances and columns representing attributes or features (e.g., income, license type, event name). Additionally, geospatial attributes like latitude and longitude are included for mapping purposes, making this a rich dataset for both socioeconomic and geographic analysis.


* How many instances are there in total (of each type, if appropriate)?

For each metric, these are the total number of instances - 
Population (US Census)
1. Race: 1153
2. Age: 19
3. Poverty: 1283
4. Education Attainment: 127
5. Median Household Income: 768

Economic Development (Analyze Boston)
1. Certified Businesses: 185
2. Licenses: 11550
3. BIPOC jobs: 34


* Does the dataset contain all possible instances or is it a sample (not necessarily random) of instances from a larger set? If the dataset is a sample, then what is the larger set? Is the sample representative of the larger set? If so, please describe how this representativeness was validated/verified. If it is not representative of the larger set, please describe why not (e.g., to cover a more diverse range of instances, because instances were withheld or unavailable).

The datasets contain all possible instances.


* What data does each instance consist of? “Raw” data (e.g., unprocessed text or images) or features? In either case, please provide a description.

Each instance in the dataset represents structured tabular data with processed features derived from raw data, designed to facilitate analysis and comparison. For population demographics, instances include features such as age group distributions (e.g., 0-17, 18-64, 65+) and racial/ethnic breakdowns, expressed as percentages of the total population. Socioeconomic indicators capture metrics like median household income, poverty rates, and educational attainment, aggregated and normalized from census and survey data. Licensing and event data encompass attributes like event types (e.g., special events, annual entertainment), license categories (e.g., alcohol, cannabis), and associated metadata such as issuance dates and locations. Economic development data highlights metrics such as the number of businesses registered, categorized by industry type or region. Finally, BIPOC workforce data includes features like job counts for Black, Indigenous, and People of Color, linked to development projects or initiatives. 


* Is there any information missing from individual instances? If so, please provide a description, explaining why this information is missing (e.g., because it was unavailable). This does not include intentionally removed information, but might include redacted text.

For some population metrics, the datasets have gaps for certain years. Licensing and event data occasionally lack complete details, such as addresses or business names, often because of errors or omissions during reporting. 

  
* Are there recommended data splits (e.g., training, development/validation, testing)? If so, please provide a description of these splits, explaining the rationale behind them

Not applicable to our analysis.


* Are there any errors, sources of noise, or redundancies in the dataset? If so, please provide a description.

There is always scope for human error in census and survey data, but nothing major caught our attention that could impact the analysis.


* Is the dataset self-contained, or does it link to or otherwise rely on external resources (e.g., websites, tweets, other datasets)? If it links to or relies on external resources,   
  * Are there guarantees that they will exist, and remain constant, over time;  
  * Are there official archival versions of the complete dataset (i.e., including the external resources as they existed at the time the dataset was created)?

The dataset is self contained.


  * Are there any restrictions (e.g., licenses, fees) associated with any of the external resources that might apply to a dataset consumer? Please provide descriptions of all external resources and any restrictions associated with them, as well as links or other access points as appropriate.

Not applicable, the datasets are census and survey data which is essentially collected with consent and with the intent of open source availability.



* Does the dataset contain data that might be considered confidential (e.g., data that is protected by legal privilege or by doctor-patient confidentiality, data that includes the content of individuals’ non-public communications)? If so, please provide a description.

Not applicable, the datasets are census and survey data which is essentially collected with consent and with the intent of open source availability.



* Does the dataset contain data that, if viewed directly, might be offensive, insulting, threatening, or might otherwise cause anxiety? If so, please describe why,

Not applicable to our datasets and analysis.



* Is it possible to identify individuals (i.e., one or more natural persons), either directly or indirectly (i.e., in combination with other data) from the dataset? If so, please describe how.

All population data is anonymized, so no individual can be identified directly or indirectly. However, the economic development data might aid in identification of certain individuals. (for instance, the certified businesses and some license data contains business and manager names).

  
* Dataset Snapshot, if there are multiple datasets please include multiple tables for each dataset. 
Population Data:


1. Race

| Size of dataset | 39.45 KB |
| --- | --- |
| Number of instances | 1153 |
| Number of fields | 4 |
| Labeled classes | 6 |
| Number of labels | 1153 |


2. Age

| Size of dataset | 0.916 KB |
| --- | --- |
| Number of instances | 19 |
| Number of fields | 4 |
| Labeled classes | 1 |
| Number of labels | 19 |


3. Poverty

| Size of dataset | 75.9 KB |
| --- | --- |
| Number of instances | 1283 |
| Number of fields | 5 |
| Labeled classes | 6 |
| Number of labels | 1283 |


4. Education Attainment

| Size of dataset | 8.76 KB |
| --- | --- |
| Number of instances | 127 |
| Number of fields | 8 |
| Labeled classes | 4 |
| Number of labels | 127 |


5. Median Household Income

| Size of dataset | 51.1 KB |
| --- | --- |
| Number of instances | 768 |
| Number of fields | 6 |
| Labeled classes | 6 |
| Number of labels | 768 |


Economic Development Data

1. Certified Businesses

| Size of dataset | 102 KB |
| --- | --- |
| Number of instances | 185 |
| Number of fields | 36 |
| Labeled classes | 5 |
| Number of labels | 185 |


2. Licenses

| Size of dataset | 4564.837 KB |
| --- | --- |
| Number of instances | 11550 |
| Number of fields | 5 |
| Labeled classes | - |
| Number of labels | 11550 |

3. BIPOC jobs

| Size of dataset | 1.504 KB |
| --- | --- |
| Number of instances | 34 |
| Number of fields | 5 |
| Labeled classes | -  |
| Number of labels | 34 |




*Collection Process*

* What mechanisms or procedures were used to collect the data (e.g., API, artificially generated, crowdsourced \- paid, crowdsourced \- volunteer, scraped or crawled, survey, forms, or polls, taken from other existing datasets, provided by the client, etc)? How were these mechanisms or procedures validated?

The datasets were directly sourced and downloaded from the US census and Analyze Boston websites.


* If the dataset is a sample from a larger set, what was the sampling strategy (e.g., deterministic, probabilistic with specific sampling probabilities)?

Not applicable for our analysis.


* Over what timeframe was the data collected? Does this timeframe match the creation timeframe of the data associated with the instances (e.g., recent crawl of old news articles)? If not, please describe the timeframe in which the data associated with the instances was created.

The population datasets were collected over a 10 year time frame to perform a trend analysis. The timeframe matches the creation timeframe of the data.



*Preprocessing/cleaning/labeling* 

* Was any preprocessing/cleaning/labeling of the data done (e.g., discretization or bucketing, tokenization, part-of-speech tagging, SIFT feature extraction, removal of instances, processing of missing values)? If so, please provide a description. If not, you may skip the remaining questions in this section.

Yes, the datasets were preprocessed, cleaned, and certain instances were relabeled to ensure clarity and ease of analysis. This preprocessing involved handling missing values by either imputing them with appropriate estimates or removing incomplete entries to maintain data integrity. Data cleaning steps included standardizing formats, correcting inconsistencies in categorical labels, and aligning dates and numeric values to a uniform structure. Relabeling was performed to make certain categories or groupings more intuitive, enabling better understanding and usability. For instance, demographic categories were grouped or renamed to reflect meaningful distinctions, and geographic data was harmonized for consistency. Additionally, any outliers or erroneous values were reviewed and addressed to improve the accuracy of the analyses. 

 
* Were any transformations applied to the data (e.g., cleaning mismatched values, cleaning missing values, converting data types, data aggregation, dimensionality reduction, joining input sources, redaction or anonymization, etc.)? If so, please provide a description.

Yes, several transformations were applied to the data to ensure it was suitable for comprehensive analysis. One significant transformation involved joining individual datasets spanning a 10-year period into a single consolidated dataset to facilitate longitudinal analysis. This required aligning and standardizing columns, resolving mismatched values across different datasets, and ensuring consistent formats for key variables such as years, categories, and geographic identifiers. Missing values were handled through imputation or removal, depending on the impact on the analysis, while mismatched or inconsistent values were cleaned to maintain data integrity. Data types were also adjusted where necessary—for instance, converting text-based numeric fields into appropriate integer or float types to enable statistical computations. Additionally, data aggregation was performed for specific analyses, such as calculating annual trends or summarizing data by categories like race, age groups, or license types.

   
* Was the “raw” data saved in addition to the preprocessed/cleaned/labeled data (e.g., to support unanticipated future uses)? If so, please provide a link or other access point to the “raw” data, this could be a link to a folder in your GitHub Repo, Spark\! owned Google Drive Folder for this project, or a path on the SCC, etc.

Yes, the raw datasets were saved in addition to the cleaned data and can be found here:  https://github.com/BU-Spark/ds-boston-d7-indicators/tree/district7-fa24-team-a/fa24-team-a/Datasets


* Is the code that was used to preprocess/clean the data available? If so, please provide a link to it (e.g., EDA notebook/EDA script in the GitHub repository).

Yes, the code used to preprocess the datasets can be found here: https://github.com/BU-Spark/ds-boston-d7-indicators/tree/district7-fa24-team-a/fa24-team-a/Population and Displacement, https://github.com/BU-Spark/ds-boston-d7-indicators/tree/district7-fa24-team-a/fa24-team-a/Economic Development and Displacement



*Uses* 

* What tasks has the dataset been used for so far? Please provide a description.

The datasets have been used to perform Exploratory Data Analysis and advanced analytics that were presented in a Tableau dashboard to derive impactful insights for the client.

 
* What (other) tasks could the dataset be used for?
The datasets offer immense potential for a variety of tasks beyond its current use in exploratory data analysis and dashboard creation.

It could be leveraged for predictive modeling to forecast socioeconomic trends, such as estimating future median incomes or identifying neighborhoods at risk of increased poverty. Policymakers and urban planners could use it to simulate the impact of proposed interventions, such as workforce development programs or educational initiatives, on economic and demographic outcomes. The data could also support equity and inclusion analyses by uncovering systemic disparities across racial, age, and income groups. Additionally, businesses might use the dataset to identify market opportunities, such as optimal locations for new ventures based on licensing trends or community demographics. 


* Is there anything about the composition of the dataset or the way it was collected and preprocessed/cleaned/labeled that might impact future uses?

Yes, the composition of the datasets and the methodologies employed in its collection and preprocessing can have implications for its future uses. The Population datasets were constructed by aggregating data spanning over 10 years, which ensures historical context but may introduce inconsistencies arising from changes in data collection methods or definitions of variables over time. While preprocessing steps like cleaning missing values and joining datasets improved usability, some information might have been lost or modified during these processes. For example, removing incomplete entries may lead to selection bias, and aggregating data could obscure nuances at a finer granularity.


* Are there tasks for which the dataset should not be used? If so, please provide a description.

Yes, there are tasks for which these datasets should not be used. Due to its aggregated and anonymized nature, the datasets are not suitable for individual-level analyses or micro-targeted interventions, such as predicting outcomes for specific individuals or households. As sensitive information has been anonymized or redacted, the dataset should not be used for tasks requiring detailed personal or business-level data. Additionally, the dataset focuses on District 7 and Boston City, so using it to generalize findings to other regions or cities without similar demographic and socioeconomic profiles would be inappropriate.



*Distribution*

* Based on discussions with the client, what access type should this dataset be given (eg., Internal (Restricted), External Open Access, Other)?

The datasets can be given external open access since it was sourced from the US census and Analyze Boston data, both of which are open source and publicly available.


*Maintenance* 

* If others want to extend/augment/build on/contribute to the dataset, is there a mechanism for them to do so? If so, please provide a description.

Currently, there is no formal mechanism in place for others to extend, augment, or contribute directly to the datasets. However, potential collaboration could be facilitated through data-sharing agreements or partnerships with the original data providers, such as city departments or community organizations. Interested contributors could work with these entities to propose extensions, such as incorporating additional data points or including new metrics. To ensure data integrity, any contributions should adhere to established standards for data collection, preprocessing, and anonymization. 


*Other*

* Is there any other additional information that you would like to provide that has not already been covered in other sections?

All essential information has been covered in the sections above.

