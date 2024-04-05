import openai

#setting up the API key
openai.api_key = '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'

#defining the 'summarize_article' function
def summarize_article(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        article_content = file.read()
    
    # Call the GPT-3.5 model to summarize the article
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=f"Summarize this article:\n\n{article_content}",
        max_tokens=150
    )
    
    summary = response['choices'][0]['text']
    return summary

#defining the 'main' function
def main():
    # List of paths to your article files
    article_files = ['./article1.txt', './article2.txt']  # Add your file paths here
    
    for file_path in article_files:
        summary = summarize_article(file_path)
        summary_file_path = file_path.replace('.txt', '_summary.txt')
        
        with open(summary_file_path, 'w', encoding='utf-8') as summary_file:
            summary_file.write(summary)
        print(f'Summary saved to {summary_file_path}')

#executing the script
if __name__ == "__main__":
    main()
