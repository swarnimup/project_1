
from module_1.scrapper import ArticleDownloader, ArticleProcessor
from module_2.additional_file import ArticleAnalyzer

def main():
    """
    Main program to initiate the download, processing, and analysis of articles.
    """
    urls = [
        "https://www.nbcnews.com/news/us-news/live-blog/winter-storm-live-updates-new-york-city-snow-rcna138521",
        "https://www.nbcnews.com/news/world/live-blog/israel-hamas-war-live-updates-cia-chief-gaza-cease-fire-deal-egypt-rcna138536",
        "https://www.nbcnews.com/tech/tech-news/esim-card-gaza-palestine-israel-war-hamas-rcna134498",
        "https://www.nbcnews.com/news/world/passenger-dies-9-month-royal-caribbean-cruise-world-rcna138631",
        "https://www.nbcnews.com/politics/congress/senate-passes-aid-package-ukraine-israel-future-uncertain-house-rcna138502"
    ]

    # Instantiate the downloader and processor
    downloader = ArticleDownloader()
    processor = ArticleProcessor()
    analyzer = ArticleAnalyzer()  # If analysis is needed after processing

    for i, url in enumerate(urls, start=1):
        # Download the article
        raw_content = downloader.download_article(url)
        if raw_content:
            # Process the article and save it
            processed_filename = f"processed_article{i}.txt"
            processor.process_and_save(raw_content, processed_filename)

    # After all articles have been processed, perform analysis
    analyzer.count_words_in_directory('Data/processed')

if __name__ == "__main__":
    main()
