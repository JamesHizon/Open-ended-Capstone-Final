# AWS End-to-end Data Pipeline Open-ended Capstone Final Presentation


![image](https://user-images.githubusercontent.com/52821013/132917375-06c643fc-8487-4168-88dd-8388d6fd117d.png)

![image](https://user-images.githubusercontent.com/52821013/132917661-669cdeab-31d3-4525-904b-5970d48a0dc1.png)



### Steps of Capstone Project
1. Project Ideas
2. Project Proposal
3. Data Collection
4. Data Exploration
5. Prototyping My Data Pipeline
6. Scaling My Data Pipeline
7. Create The Deployment Architecture
8. Deploy My Code for Testing
9. Deploy My Code and Process the Dataset
10. Build a Monitoring Dashboard

### Attached Files
Inside this repository, one can find various Python scripts and Jupyter Notebook files. I realized I ended up using different naming conventions, so here is the order of files:
  1. Project_Data_Collection.py
  2. Capstone Project - Data Exploration.ipynb
  3. Step5_Capstone_Project.py
  4. Test_S3_Upload.ipynb
  5. OEC_Unit_Test_JNB.ipynb
  6. New_ELT_Notebook.ipynb


### AWS CloudFormation Template
The following showcases my AWS CloudFormation template. It basically includes the various cloud resources that I used, such as the need to set up an S3 bucket, multiple EMR Clusters needed to process my dataset, CloudWatch Dashboard, AWS Glue and AWS Quicksight dashboard. This was my original plan when developing my CloudWatch template, which would be used to automatically set up and launch cloud resources vs. spending time doing it manually. In the real-world, I need to pay extra attention to the properties tab and figure out how to properly set up my cluster configuration settings.

![image](https://user-images.githubusercontent.com/52821013/132917819-f5efb059-5001-4525-854b-31e758cb7cd0.png)


### Dataset Description
The dataset I chose to work with is from the GDELT Project website. Given that the project requires the need to process nearly 100s of GBs of data, I chose to deal with a simple dataset from here.

- Q: What is the GDELT Project?
  - It is an initiative to construct a catalog of human societal-scale behavior and beliefs across all countries of the word, connecting every person, organization, location, count, theme, news source and event across the planet into a single massive network that captures what's happening around the world, what its context is and who's involved, and how the world is feeling about it, every single day.

- Q: How much data is available on the website?
  - All of the underlying records are in CSV format, where a single year of the GDELT GKG totals 2.5 TB.

- Q: What is the GDELT 1.0 Global Knowledge Graph (GKG)?
  - One of the available datasets, and consists of two parallel data streams such that one encodes the entire knowledge graph with all of its fields and the other encodes only the subset of the graph that records counts of a set of predefined categories like number of protesters, number killed, or number displaced or sickened.
  - File Names: "YYYYMMDD.gkg.csv.zip", "YYYYMMDD.gkgcounts.csv.zip"
  - Each of the files are posted by 6AM EST every morning, seven days a week, implying that the dataset is near real-time streaming data.


### Final Components of My Data Pipeline and Rationale Behind Choosing Them
The final components of my data pipeline include integration of AWS S3, EMR, Athena and Glue, and CloudWatch. I was introduced to Athena and Glue earlier on via mentor, and so decided to stick to using it to automatically learn the schema from the two data streams with Glue and have fast querying with Athena. This was a great option especially after using EMR Notebook to run Spark job to transform data and load into the two separate file folders and the datasets that exist inside the two folders all share the same schema (columns and data types). An alternative would have been to work with AWS Redshift, yet I was not able to use it since I was not provided access via AWS Student account. AWS Redshift is notable for its' performance and scalability vs. Athena which is better in terms of portability and cost.

When thinking about other alternative approaches, I could have tried to integrate Airflow and EMR Notebooks, yet there were some technical difficulties which prevented me from setting up an AWS Access and Secret Access Key to SSH into EMR and allow me to automatically orchestrate running multiple EMR Notebooks. I had to manually launch and terminate multiple EMR Notebooks given that the cluster configuration settings did not allow me to fully process and transform data with Spark. In the future, it would be good to keep in mind the need to edit cluster configuration settings to be able to handle large datasets or even try to use Airflow with multiple EMR Notebooks.

### Project Ideation and Proposal
Prior to main steps, I needed to brainstorm in regards to how I wanted to develop my data pipeline from end-to-end. I first had to explore various websites to find a dataset that is nearly 100s of GBs of data. Ideas stemmed from aggregating and pulling data from multiple sources to simply finding a dataset that already was in the range of hundreds of GBs of data. I researched and asked myself, "what type of data would involve hundreds of GBs?" Then, I thought about maybe trying to deal with data from a global scale, and found the GDELT via searching on Google. 

Then, I began with working with Draw.io to create and propose a plan for developing my data pipeline from end-to-end using various AWS resources.

### Description of Each Step of My Data Pipeline (Acquisition, Cleaning, Transforming of Data, etc.)


1. Acquisition:
- In regards to the extraction step of my data pipeline, I wrote a Python script to download a sample of 10 CSV files using the ```bs4``` (BeautifulSoup) and ```requests``` package.


2. Exploratory Data Analysis
- In order to see what data transformations are necessary, I ended up using ```pandas``` in Python to create a dataframe as follows:
 ```df = pd.read_csv(<FILENAME.csv>)```

- Then, I performed the following to see the first five rows of the dataframe vs. needing to visualize with matplotlib: ```df.head(5)```


3. Transforming:
- While continuing to work with ```pandas```, I basically tried to merely drop null values and then write back to the same CSV file so I would get a glimpse of how data transformations would look like with a larger dataset. The main code snippet is as follows: ```df.dropna(axis=1)```

- Above, we see that an "axis" argument can be used to determine if one should drop values on rows or columns. I specified that I should drop the whole column is there are null values, but in later steps, decided to drop data based on other conditions.


4. Prototyping:
- In my data pipeline prototype, I basically created a Python OOP Class, called "DataPipeline", where I create a method to automatically extract, transform and load data into an S3 bucket using Python packages like ```bs4```, ```requests```, ```pandas```, and ```boto3```. The ```boto3``` package was used to integrate Python with AWS services.

5. Scaling Prototype:
- In order to scale my data pipeline prototype, I needed to update my class to automatically extract and load data into an S3 bucket, used PySpark API to read and transform the data, and then loaded the data into two separate file folders so that I could integrate Athena and Glue. In addition, I added other methods to remove and delete unnecessary data to save space.


6. Unit Testing:
- To apply unit testing, I worked with the ```unittest``` package. Unit testing within creation of data pipelines is a crucial step to ensure that all the data transformations meet the desired expectations. I was also tasked to deal with code coverage, where the ```coverage``` package would be needed to test to see how much of my code is covered by unit tests. Since my AWS Student account was not sufficient, I simply dealt with simple unit tests and explored possibility of the given package.


7. Redeployment of Code to New AWS Cloud Resources:
- After my unit testing step, I needed to make some updates to my data transformations like ensuring that I dropped the desired columns and figure out whether it was necessary to do data type conversion if I could just use a ```CAST()``` function or integrate AWS Glue to automatically detect schema. Then, I recreated another S3 bucket, launched various EMR Clusters to process data inside EMR Notebook, and then integrated AWS Glue and Athena to automatically detect the schema and figure out how to query data from two data stream tables.


### Entity-Relationship Diagram for Data Model from Step 4

![alt text](https://github.com/JamesHizon/Open-ended-Capstone-Final/blob/main/Step_4_Data_Model.drawio.png)

### Diagram Representing Data Flow from One Component to Another via AWS Resources

The following includes the flow of data via architecture diagram created through Draw.io:


![alt text](https://github.com/JamesHizon/Open-ended-Capstone-Final/blob/main/OE_Capstone_Step_7.drawio.png)

Above, we can see that I planned to use Redshift, and imagined how the end user would deal with the data. One can create a dashboard via AWS Quicksight or even try to build a predictive model via AWS SageMaker. Yet, based on AWS Educate account, I was limited to only deal with AWS S3, but could still interact with Glue and Athena for cost-effective querying of data.

### Athena and Glue

The following is a screenshot after automating schema creation and querying 10 rows of data from 1 table created from the 2 File Folders based on two separate file streams:

![alt text](https://github.com/JamesHizon/Open-ended-Capstone-Step-9/blob/main/Screen%20Shot%202021-08-09%20at%2012.40.51%20PM.png)

After reviewing the data as shown above, we can think about what types of queries can be made based on the structure of the data. For example, the themes column has multiple records. One way to deal with this is to apply normalization, where I end up creating multiple tables as a result of this column. Another way is to keep the data as is, and simply apply a wildcard operator within the ```WHERE``` clause, i.e. ```SELECT COUNT(*) FROM "datastreams"."data_stream_1" WHERE themes LIKE "%ENVIRONMENT%";``` to count how many records are related to environmental impact.

### Other Relevant Information
I worked with AWS Educate account to work on my data pipeline project, where I was able to work with most of the key important services for data engineering. Yet, I was still limited due to the availability of resources on the account.

In addition, it may beneficial to observe other repositories for further explanation of steps described.

### Real-Time Analytics Dashboard
The following dashboard include mainly two metrics for analysis which are the EMR YarnMemoryAvailable statistic as well as S3 BucketSizeBytes. Other notable metrics that I could've added, but was not available, are billing metrics such as the total cost for AWS Services for a given day. In addition, AWS EMR has built-in metrics via tab, so I decided to include the "YARNMemoryAvailable" metric within EMR, as it shows how much memory is available to YARN inside EMR Cluster and YARN essential for orchestrating the flow of Spark jobs.

In the real-world, I can think about other use cases of CloudWatch including having various metrics for various services alongside the billings metrics to understand which services tend to contribute the most to higher AWS cost.

![alt text](https://github.com/JamesHizon/Open-ended-Capstone-Final/blob/main/Screen%20Shot%202021-09-10%20at%204.28.57%20PM.png)

Link to AWS CloudWatch Dashboard:
https://cloudwatch.amazonaws.com/dashboard.html?dashboard=Capstone_Dashboard&context=eyJSIjoidXMtZWFzdC0xIiwiRCI6ImN3LWRiLTcwNDQwOTE4MjcyOCIsIlUiOiJ1cy1lYXN0LTFfSHl0VG05cW5mIiwiQyI6IjFoMHR1YmFzZGltMTlnaGtmbms3MWFwMWttIiwiSSI6InVzLWVhc3QtMToyYWFmOGRmMS04ODA4LTRhMzYtODRlNS05ODA2ZjdjYmNhYjciLCJNIjoiUHVibGljIn0%3D


### Main Takeaways
Working on this data pipeline capstone project required lots of time and effort. I took what I learned from the course material to practice. Originally, I the data pipeline guidance is for data pipeline development taught in Azure, but I took those concepts and applied it as I finished my end-to-end project in AWS. After dealing with this data pipeline project alongside other mini-projects, I feel more confident that I will be able to complete end-to-end data pipeline projects in the real-world, knowing I will end up dealing with massive amounts of messy data.
