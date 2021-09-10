# Open-ended Capstone Final Presentation


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
1. Include EDA on Jupyter.
2. Include EMR Notebooks.


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

In regards to thinking about other alternative approaches, I could have tried to integrate Airflow and EMR Notebooks, yet there were some technical difficulties which prevented me from setting up an AWS Access and Secret Access Key to SSH into EMR and allow me to automatically orchestrate running multiple EMR Notebooks. I had to manually launch and terminate multiple EMR Notebooks given that the cluster configuration settings did not allow me to fully process and transform data with Spark. In the future, it would be good to keep in mind the need to edit cluster configuration settings to be able to handle large datasets or even try to use Airflow with multiple EMR Notebooks.


### Description of Each Step of My Data Pipeline (Acquisition, Cleaning, Transforming of Data, etc.)
1. Acquisition
2. Transforming
3. Prototyping
4. Scaling Prototype
5. Unit Testing
6. Redeployment

### Entity-Relationship Diagram for Data Model from Step 4


### Diagram Representing Data Flow from One Component to Another via AWS Resources


### Other Relevant Information


### Real-Time Analytics Dashboard



### Note to self/whoever is reading
- I need to make sure to include necessary photos inside this Github page.
- I am still finishing up this document.
