                                                      News Article Scraper

Project Overview:
This semester-long project involves collecting and scraping news articles from a chosen news agency's website. The project follows these major steps:

Data Collection:

Choosen a news agency.
Went to the news website and selected different category
Clicked on any 5 links within the chosen category.
Copied these URLs and save them in a text file.

Scraper Implementation:
Created a Python program (python_my_news.py) to visit each URL from the text file.
Download/copy/scrape the content of each URL.
Used Python packages such as BeautifulSoup, and html2text.

GitHub Repository:
Created a public GitHub repository to store project files.
Named the repository appropriately for future reference on resumes.

Documentation:
Export the Conda environment to a file (requirements.yaml) for reproducibility.
Write an elaborate README.md file.
Include project description, setup instructions, usage details, and information about the output files.
Emphasize the importance of documentation in software engineering.

The main Python script (python_my_newss.py) does the following:
Takes a list of URLs as input.
Visits each URL, extracts the main content of the news article.
Converts HTML content to plain text using html2text.
Saves each article to a separate text file.

Repository Structure
python_my_newss.py: Python script for scraping news articles.
requirements.yaml: Conda environment file.
src_links: contains all the links in the form of texts

Output
After running the script, find five text files (article_1.txt, article_2.txt, etc.) in the project directory, each containing the content of the respective news articles.