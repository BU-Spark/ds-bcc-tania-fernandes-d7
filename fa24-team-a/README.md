# **BOSTON DISTRICT 7 INDICATORS: TEAM A**  

## **About the Project**  

Our project, in collaboration with Boston Councilor's Office, focuses on analyzing population and economic development data for District 7 in Boston. The primary aim is to identify trends and disparities, particularly among marginalized groups, and to assist in data-driven decision-making.  

### **Scope of the Analysis**  
Our analysis centers around two key areas:  
1. **Population Displacement:**  
   - Examining demographic trends, including race, ethnicity, age distribution, and education levels.  
   - Investigating patterns of displacement and population changes over the past 10 years.  

2. **Economic Development:**  
   - Analyzing metrics such as median household income, poverty analysis, the number of registered businesses, and job creation data for BIPOC workers.  
   - Identifying trends in business vibrancy, licensing, and workforce diversity within District 7.  

### **Methodology**  
- We utilized datasets from various public sources, covering a 10-year period to track changes in District 7 and compare them to citywide averages and, where applicable, other districts.  
- Data analysis was structured into two main areas of focus, with files and outputs categorized accordingly.  
- Following the analysis, we leveraged the finalized datasets to create an interactive dashboard in Tableau, providing clear and actionable visual insights.  

### **Final Deliverables**  
Our final deliverables include:  
- **Raw Datasets:** Unprocessed datasets used during the initial stages of analysis.  
- **Processed Datasets:** Cleaned and analyzed datasets, prepared for visualization and further exploration.
- **Python Notebook Files:** Jupyter notebooks containing the code and analysis workflows for both population displacement and economic development metrics. These files document the step-by-step approach used for data preprocessing, analysis, and visualization.
- **Interactive Dashboard:** A Tableau dashboard summarizing key findings, designed to facilitate quick and effective decision-making.  

These resources provide Councilor Anderson with a comprehensive understanding of District 7's demographic and economic landscape, highlighting areas of improvement and ongoing challenges.  

---

## **Roadmap to the Repository**  

### **Repository Structure**  
The repository is organized to facilitate ease of navigation and access to resources:  

1. **`fa24-team-a` Folder**  
   This is the main project folder, containing all the work and analyses. Inside, you will find:  

   - **`Census Tracts`:**  
     - Contains geographic and demographic data at the census tract level, focusing on spatial patterns in population and economic metrics.
    
   - **`Dashboard-data`:**  
     - Includes the processed datasets used to create the Tableau dashboard.
     - Contains individual Tableau workbooks for the different metrics analyzed in the project.
    
   - **`Datasets`:**  
     - Raw datasets sourced from public repositories, used for the initial stages of analysis.

   - **`Population and Displacement`:**  
     - Includes files related to the analysis of population dynamics, displacement trends, and demographic changes over the past 10 years.  

   - **`Economic Development and Displacement`:**  
     - Contains analysis files and results focused on economic trends, including household income, business registrations, and job creation for BIPOC workers.

   - **`README.md`:**  
     - This file, providing an overview of the project and a guide to navigating the repository.  

### **Dashboard**  
The Tableau dashboard is a central deliverable of the project, offering a visual summary of key insights. It includes:  
- Trends in population demographics and displacement.  
- Economic indicators and business vibrancy in District 7.  
- Comparisons to Boston city averages, allowing for clear identification of disparities and progress.  

The dashboard is based on the processed datasets available in the repository and is designed to be intuitive and actionable.  

---

## **Usage and Collaboration**  

- All data and resources in this repository adhere to public data-sharing protocols, ensuring compliance with privacy and ethical standards.  
- We welcome feedback from Boston Councilor's Office and stakeholders to refine and expand the analyses as needed.  

Let us know if you have additional suggestions for improvement or require access to specific files.  
=======
# Project Early Insights - 

The project documentation and requirements can be found here -  https://docs.google.com/document/d/1Uaog4rmR8DzWeZN0JLJAwmLfHwiJQqNYFkOJNKGbli0/edit. 


For the first two weeks, we were working with very limited and unclear data from the client. The problem statement was not clearly defined, which made it difficult to make significant progress. Ziba was making continuous changes to the project documentation, and has iterated upon the datasets that we need to work upon after consulting with the client. Since this was done after the project early insights work, we were only able to analyze one dataset during this period to get started with as per the suggestions of our PM and TPM. With the new direction in place, we have started working on the additional datasets. 

With that being said, we are currently facing a challenge in our project flow. Although we have received updated data links from the client, we are still having trouble filtering out the specific data for District 7. The provided datasets do not have the right filters to extract the data we need for our analysis. We have raised this concern with our project manager, technical program manager, and the client through Slack, and we are currently awaiting their response. Based on the clarifications, we will proceed with our project as usual.


## Initial Analysis - 311 Service Requests Dataset


Based on the available data from our first team meeting, we picked up the 311 service requests dataset to get started and performed a preliminary analysis on it. In the subsequent sprints, we will have a merged dataset after completing data review for all categories and metrics. The analysis notebook can be found in the *311_requests* folder.

### Dataset Description -

The dataset contains records of 311 service requests made by residents in District 7. Each record contains fields such as the Case ID, type of service requested, location, status of the request, address from where the request was made and source of the request. The dataset is rich for analysis and also includes geospatial information like the latitudes and longitudes of neighborhoods and districts, allowing scope for spatial analysis.

### What questions were answered by analyzing the data?

We were able to analyze datasets with records from the years 2023 and 2024, and the following questions can be answered based on the insights:
1. Number of outstanding and completed requests
2. Identifying the sources of service requests
3. Number of D7 app downloads vs newsletter subscription
4. Spatial Analysis of open and closed requests via a Heatmap

### What questions could not be answered with the given data?
Specific Causes for service requests could not be determined with the given data. For instance, if we have a spike in garbage removal requests in a certain area, identifying the cause behind it is not feasible with the data. In terms of understanding civic engagement, direct feedback from the residents for each case would help assess their satisfaction levels better. Including this type of data could provoke a deeper level analysis of resident welfare in District 7.

### What other data sources are required according to the project description?
Earlier, we were required to analyze data across four broad categories - Education, Public Health, Public Safety and Environmental Justice. After surpassing the project early insights task, our project requirement was redefined and the target data metrics were reduced to - 1) Population and Displacement and 2) Economic development and displacement. We are now in the process of accessing the data according to the updateed requirements of the client, and will be working on further analysis and developement in the coming weeks.
