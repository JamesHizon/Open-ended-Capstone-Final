# Web Scraping using Python to scrape data from website:

# Standard library imports
import os
import datetime
import logging
import zipfile

# Third party imports
from bs4 import BeautifulSoup
import requests

# Control logging levels:
logging.basicConfig(level=logging.INFO)

# Extract data from HTML webpage
URL = "http://data.gdeltproject.org/gkg/index.html"
page = requests.get(URL)

# Create BeautifulSoup object to parse through HTML document
soup = BeautifulSoup(page.content, "html.parser")

# Base url for file downloading
base_url = "http://data.gdeltproject.org/gkg/"

# Current Directory
current_directory = os.getcwd()

if __name__ == "__main__":

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
                        # Try to remove zip, unzip.
                        # Also, try to write response straight to CSV file for efficiency gains.
                        with open(f"{file}", "wb") as zip_file:
                            response = requests.get(download_url)
                            zip_file.write(response.content)
                        logging.info("Zip file has been downloaded.")
                        # Use after creating zipfile to unpack as a CSV
                        with zipfile.ZipFile(f"{file}", "r") as zip_ref:
                            zip_ref.extractall(current_directory)
                        logging.info("File has been downloaded and unpacked as CSV.")
            logging.info("All files have been downloaded.")
        except Exception as e:
            logging.error(f"Error was {e}")

