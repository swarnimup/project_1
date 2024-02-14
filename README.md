                                                     News Article Scraper
Project Overview:
This semester-long project involves collecting and scraping news articles from a chosen news agency's website. The project follows these major steps:

Data Collection:

Choose a news agency.
Go to their website and select a category (politics, sports, entertainment, etc.).
Click on any 5 links within the chosen category.
Copy these URLs and save them in a text file.
Scraper Implementation:

Create a Python program (python_my_newss.py) to visit each URL from the text file.
Download/copy/scrape the content of each URL.
Use Python packages such as requests, BeautifulSoup, and html2text.
GitHub Repository:

Create a public GitHub repository to store project files.
Name the repository appropriately for future reference on resumes.

Documentation:

Export the Conda environment to a file (requirements.yaml) for reproducibility.
Wrote an elaborate README.md file.
Include project description, setup instructions, usage details, and information about the output files.
Emphasize the importance of documentation in software engineering.


Work:
Setting up the Conda environment and running the Python code.
Code Overview
The main Python script does the following:

Takes a list of URLs as input.
Visits each URL, extracts the main content of the news article.
Converts HTML content to plain text using html2text.
Saves each article to a separate text file.
Repository Structure
requirements.yml: Conda environment file.

Output
After running the script, find five text files (article_1.txt, article_2.txt, etc.) in the project directory, each containing the content of the respective news articles.