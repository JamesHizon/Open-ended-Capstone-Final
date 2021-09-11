# Data Pipeline Prototype with Classes

# Standard library imports
import os
import datetime
import logging
import zipfile

# Third party imports
from bs4 import BeautifulSoup
import requests
import boto3
import pandas as pd


class DataPipeline:
    """
    This DataPipeline class will simply be used to take an website url as a data source and
    an S3 object as a possible data storage destination. An ETL method is also created with
    description as follows.
    """

    def __init__(self, s3_obj, url):
        self.s3_obj = s3_obj
        self.url = url

    def extract_transform_load(self, use_cloud, cloud_path):
        """
        This function will take an optional parameter "use_cloud" (BOOLEAN) and "cloud_path" to store files onto AWS S3.
        If the "use_cloud" parameter is true, then we will write to cloud location "cloud_path".
        For the case of Step 5 where we do not use cloud, we will simply set "use_cloud" to
            False and "cloud_path" can just be any variable since we are not using it.

        :return: Logging statement after extracting files from website.
        """
        # Control logging levels:
        logging.basicConfig(level=logging.INFO)
        # Extract data from HTML webpage
        url = self.url
        page = requests.get(url)
        # Create BeautifulSoup object to parse through HTML document
        soup = BeautifulSoup(page.content, "html.parser")
        # Base url for file downloading
        base_url = url[:-9]

        # Current Directory -> MAY NOT USE. -> CHANGE TO S3 BUCKET AS LOCATION.
        current_directory = os.getcwd()

        # Iterate to obtain all we want to download based on "a" and "href" tags and write to CSV file
        for link in soup.find_all("a"):
            try:
                if link.has_attr("href"):
                    # Obtain file name as string object:
                    file = link.attrs["href"]
                    # Create a list of dates to control which files to download:
                    today = datetime.date.today()
                    # List of dates:
                    date_list = [today]
                    # Add other dates (within 1 week):
                    for i in range(1, 8):
                        new_day = today - datetime.timedelta(days=i)
                        date_list.append(new_day)
                    # Convert dates to string to filter file name
                    for date in date_list:
                        date = date.strftime("%Y%m%d")
                        if date in file:
                            download_url = f"{base_url}{file}"
                            # Download as zip file
                            with open(f"{file}", "wb") as zip_file:
                                response = requests.get(download_url)
                                # Write content to zip_file
                                zip_file.write(response.content)
                                # Deal with both cases (using AWS or not)
                                if use_cloud is False:
                                    logging.info("Zip file has been downloaded.")
                                    # Use after creating zipfile to unpack as a CSV
                                    with zipfile.ZipFile(f"{file}", "r") as zip_ref:
                                        zip_ref.extractall(current_directory)
                                        # LOGIC TO TRANSFORM DATA USING PANDAS:
                                        # 1) SINCE FILE IS NOW IN CURRENT DIRECTORY, LET US USE PANDAS TO READ FILE.
                                        # 2) THEN, WE PERFORM ESSENTIAL DATA TRANSFORMATION (REMOVE NULL VALUES).
                                        # 3) WRITE TO CSV FILE.
                                        file_path = current_directory + "/" + str(file)
                                        file_df = pd.read_csv(file_path)
                                        file_df = file_df.dropna()
                                        file.to_csv(f"{file}")
                                else:
                                    with zipfile.ZipFile(f"{file}", "r") as zip_ref:
                                        # TRY TO DO SAME STEPS AS BEFORE WHERE WE EXTRACT ALL OF OUR DATA INTO CURRENT DIRECTORY,
                                        # APPLY DATA TRANSFORMATIONS, AND LOAD TO CLOUD (S3).
                                        zip_ref.extractall(current_directory)
                                        file_path = current_directory + "/" + str(file)
                                        file_df = pd.read_csv(file_path)
                                        file_df = file_df.dropna()
                                        # USE CLOUD PATH TO UPLOAD DIRECTLY TO S3
                                        cloud_file_path = cloud_path + "/" + str(file)
                                        file_df.to_csv(cloud_file_path)
                            logging.info("File has been downloaded and unpacked as CSV.")
                logging.info("All files have been downloaded.")
            except Exception as e:
                logging.error(f"Error was {e}")


# Create s3 object using boto3
s3 = boto3.client('s3')

# Obtain url
website_url = "http://data.gdeltproject.org/gkg/index.html"

# Create data pipeline (use s3 object as input)
dp = DataPipeline(s3, website_url)

# Run extract_transform_load method to scrape and download the data from HTML document:
# dp.extract_transform_load(use_cloud=False, cloud_path=None)

# Next:
# 1) Update logic of code to properly deal with S3 bucket.
# 2) Update other information such as access key for S3 client.
# 3) I will work more on this later, when I am required to scale data pipeline to cloud.
