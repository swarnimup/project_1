
import os
import requests
from bs4 import BeautifulSoup
import html2text

class ArticleDownloader:
    """
    Responsible for downloading articles from URLs.
    Follows the Single Responsibility Principle by focusing solely on downloading content.
    """
    def download_article(self, url):
        response = requests.get(url)
        if response.status_code == 200:
            # Save the raw HTML content
            raw_filename = f"Data/raw/raw_{os.path.basename(url)}.html"
            with open(raw_filename, 'wb') as raw_file:
                raw_file.write(response.content)
            return response.content
        else:
            print(f"Failed to download article from {url}. Status code: {response.status_code}")
            return None

class ArticleProcessor:
    """
    Takes raw HTML content, processes it to extract the main article content,
    and saves it in a more readable format.
    Follows the Single Responsibility Principle by focusing solely on processing downloaded content.
    """
    def process_and_save(self, raw_content, filename):
        soup = BeautifulSoup(raw_content, 'html.parser')
        main_content = soup.find('div', class_='article-body')  # Adjust as needed
        text_content = html2text.html2text(str(main_content))

        # Save processed text
        with open(f"Data/processed/{filename}", 'w', encoding='utf-8') as file:
            file.write(text_content)
