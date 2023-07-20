# Web Scraper in Python
This project aims to develop a versatile web scraper in Python, capable of extracting data from various websites and web pages. The web scraper utilizes the powerful libraries and tools available in Python to automate the process of data extraction, enabling users to gather relevant information efficiently.
# Features
Flexible URL handling: The web scraper supports parsing URLs from different sources, such as a predefined list, CSV file, or command-line input, making it adaptable to various use cases.
Configurable data extraction: Users can easily define the data they want to extract by specifying the desired HTML elements, attributes, and filters. This allows for targeted scraping of specific content.
Robust web crawling: The scraper incorporates intelligent web crawling techniques, ensuring efficient and responsible scraping by respecting website policies, handling pagination, and managing rate limits.
Data storage options: Extracted data can be saved in various formats, including CSV, JSON, or a database, providing flexibility for further analysis and processing.
Logging and error handling: The scraper implements a logging system to track scraping activities and handle errors gracefully, improving reliability and troubleshooting.
# Usage
To use the web scraper, follow these steps:

1. Clone the repository: git clone https://github.com/your-username/web-scraper-python.git
2. Install the required dependencies: pip install -r requirements.txt
3. Modify the configuration file (config.ini) to specify the URLs to scrape and the desired data extraction settings.
4. Run the scraper: Pass link to desired reddit/subreddit page as first command line argument. Pass number of desired reddit pages to scrape as second command line argument
    
example command to run
/bin/python3 /home/spumel/web-scraper-python/materials-web-scraping-tutorial/scrape_selenium.py https://old.reddit.com/ 100
