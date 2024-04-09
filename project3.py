import openai

# Setting up the API key
openai.api_key = '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'

# Cache dictionary to store summaries
summaries_cache = {}

def summarize_article(file_path):
    # Check if the summary is already in the cache
    if file_path in summaries_cache:
        return summaries_cache[file_path]
    
    with open(file_path, 'r', encoding='utf-8') as file:
        article_content = file.read()

    # The maximum number of tokens that can be sent in the messages parameter
    # We set some room for the system and user messages
    max_length = 16385 - 100
    
    # If the article content is too long, truncate it
    if len(article_content) > max_length:
        article_content = article_content[:max_length]

    # Call the OpenAI API to summarize the article
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are an assistant who summarizes articles."},
            {"role": "user", "content": article_content}
        ]
    )
    
    # Extract the summary from the response
    summary = response.choices[0].message['content'].strip()
    
    # Save the summary to the cache
    summaries_cache[file_path] = summary
    
    return summary

def main():
    # List of paths to your article files
    article_files = ['processed_article2.txt']  # Extend this list as needed
    for file_path in article_files:
        summary = summarize_article(file_path)
        summary_file_path = file_path.replace('.txt', '_summary.txt')

        with open(summary_file_path, 'w', encoding='utf-8') as summary_file:
            summary_file.write(summary)
        print(f"Summary saved to {summary_file_path}")

    

if __name__ == "__main__":
    main()
