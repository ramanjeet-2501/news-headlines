# news-headlines
A) Project Description
This Python script scrapes top headlines from news websites and saves them to a text file. 
It demonstrates web scraping fundamentals using Python's requests and BeautifulSoup libraries.

B) Key Features
Website Fetching: Uses requests to download HTML content from news websites
HTML Parsing: Extracts headlines using BeautifulSoup by searching for heading tags (h1-h4)
Data Cleaning: Processes scraped text to remove extra whitespace and empty entries
File Output: Saves results in an organized text file with numbered headlines

C) Technical Implementation
The script:
Sends HTTP requests with custom headers to mimic browser behavior
Parses HTML content looking for heading elements
Implements fallback selectors if primary scraping fails
Handles common errors gracefully (network issues, missing elements)
Generates clean output with proper formatting
Usage Instructions
Install requirements: pip install requests beautifulsoup4
Run script: python news_scraper.py
Customize the target URL in the script if needed

