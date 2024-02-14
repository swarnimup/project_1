import requests
from bs4 import BeautifulSoup
import html2text

def download_article(url, filename):
    # Send a GET request to the URL
    response = requests.get(url)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the HTML content
        soup = BeautifulSoup(response.content, 'html.parser')

        # Extract the main content
        main_content = soup.find('div', class_='article-body')  # Adjust class or tag based on website structure

        # Convert HTML to plain text
        text_content = html2text.html2text(str(main_content))

        # Save the content to a file
        with open(filename, 'w', encoding='utf-8') as file:
            file.write(text_content)

        print(f"Article from {url} downloaded successfully.")
    else:
        print(f"Failed to download article from {url}. Status code: {response.status_code}")

if __name__ == "__main__":
    urls = [
        "https://www.nbcnews.com/news/us-news/live-blog/winter-storm-live-updates-new-york-city-snow-rcna138521",
        "https://www.nbcnews.com/news/world/live-blog/israel-hamas-war-live-updates-cia-chief-gaza-cease-fire-deal-egypt-rcna138536",
        "https://www.nbcnews.com/tech/tech-news/esim-card-gaza-palestine-israel-war-hamas-rcna134498",
        "https://www.nbcnews.com/news/world/passenger-dies-9-month-royal-caribbean-cruise-world-rcna138631",
        "https://www.nbcnews.com/politics/congress/senate-passes-aid-package-ukraine-israel-future-uncertain-house-rcna138502"
    ]

    for i, url in enumerate(urls, start=1):
        filename = f"article_{i}.txt"
        download_article(url, filename)