"""
scraper_jobs.py

This is a Python web scraping program designed to scrape static websites.

Author: Martin Breuss
Date: 7/5/2023

Description:
This program utilizes Python's web scraping libraries to extract data from static websites. 
It can navigate through web pages, retrieve HTML content, parse the data, and extract 
desired information using techniques like XPath or CSS selectors. The scraped data 
can be further processed, stored, or used for analysis as per your requirements.

Usage:
1. Customize the program to suit your specific scraping needs.
2. Run the script using the Python interpreter: `python scraper.py`.
3. Adjust the settings and parameters as desired to scrape different websites or 
modify the scraping behavior.

Note: This program is designed for scraping static websites. If you intend to scrape dynamic websites or websites that employ anti-scraping measures, additional techniques and libraries may be necessary.
"""

# comes with built-in capacity to handle authentication FYI
import requests
from bs4 import BeautifulSoup


URL = "https://realpython.github.io/fake-jobs/"
# retrieves HTML data that the server sends back and stores in Python object
page = requests.get(URL)
# we now have access to site's HTML from within this Python script
# an HTML formatter to clean up
# please NOTE: every website will look different, inspect page beforehand

# the second parameter makes sure you use the appropriate parser for HTML content
soup = BeautifulSoup(page.content, "html.parser")
# upon inspecting the page, the "ResultsContainer" contains all job postings
# BeautifulSoup allows you to find a specific HTML element by its ID
results = soup.find(id="ResultsContainer")
# print(results.prettify())

# look for Python jobs
print("PYTHON JOBS\n==============================\n")
# passing an anonymous function to the string= argument
# the lambda function looks at the text of each <h2> element, converts to lowercase,
# and checks whether "python" is found anywhere
python_jobs = results.find_all(
    "h2", string=lambda text: "python" in text.lower()
)
python_job_elements = [
    h2_element.parent.parent.parent for h2_element in python_jobs
]

# each job_element is another BeautifulSoup object
for job_element in python_job_elements:
    title_element = job_element.find("h2", class_="title")
    company_element = job_element.find("h3", class_="company")
    location_element = job_element.find("p", class_="location")
    # you can add .text to return only the text content of the HTML elements
    # that an object contains
    print(title_element.text.strip())
    print(company_element.text.strip())
    print(location_element.text.strip())
    link_url = job_element.find_all("a")[1]["href"]
    print(f"Apply here: {link_url}\n")
    print()
