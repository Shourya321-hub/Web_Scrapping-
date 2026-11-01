 Web Scraping Project

 Exploratory Web Scraping and Dataset Creation


1. Project Overview

This project demonstrates the process of extracting structured information from a public webpage using Python.

The project uses the Quotes to Scrape website, which is designed for web-scraping practice.

The extracted information includes:

- Quotes
- Authors
- Tags

The scraped information is converted into a structured CSV dataset and then analyzed using Exploratory Data Analysis (EDA).


 2. Project Objectives

The main objectives are:

- Learn the fundamentals of web scraping.
- Understand HTML structure.
- Extract relevant information from webpages.
- Navigate multiple webpages.
- Create a custom dataset.
- Clean and validate scraped data.
- Perform exploratory data analysis.
- Generate useful visualizations.
- Save the final dataset as CSV.



 3. Technologies Used

- Python
- Requests
- BeautifulSoup
- Pandas
- Matplotlib
- Seaborn



 4. Project Structure

```text
project_Web_Scraping/
│
├── data/
│
├── src/
│   ├── scraper.py
│   ├── data_cleaning.py
│   └── eda.py
│
├── output/
│   ├── quotes.csv
│   ├── quotes_cleaned.csv
│   ├── top_authors.png
│   └── top_tags.png
│
└── README.md
