
import os

class ArticleAnalyzer:
    """
    Provides functionalities for analyzing processed articles.
    Renamed class to ArticleAnalyzer for clarity and to avoid naming conflicts.
    """

    def count_words_in_article(self, article_path):
        """
        Count the number of words in a single article.

        :param article_path: The path to the article file.
        :return: Number of words in the article.
        """
        try:
            with open(article_path, 'r', encoding='utf-8') as file:
                content = file.read()
                return len(content.split())
        except FileNotFoundError:
            print(f"File not found: {article_path}")
            return 0

    def count_words_in_directory(self, processed_directory):
        """
        Count the number of words in each processed article within a directory and print the results.

        :param processed_directory: The directory containing processed articles.
        """
        try:
            for filename in os.listdir(processed_directory):
                if filename.endswith(".txt"):
                    full_path = os.path.join(processed_directory, filename)
                    word_count = self.count_words_in_article(full_path)
                    print(f"Article {filename}: Word Count - {word_count}")
        except Exception as e:
            print(f"An error occurred while processing the directory {processed_directory}: {e}")

