
CS325 Project 3: Article Summarization

The project builds upon the previous work in Project 2's repository. The task involves developing a Python program that interacts with OpenAI API  to create concise summaries of articles.

Steps

Project Setup:

Using the existing Project 2 repository, the individual should consider creating a dedicated branch for this project.
I
nstallation of Required Libraries: Ensuring the necessary libraries for making API requests and potentially text manipulation (here requests, beautifulsoup4) are installed using pip 

Obtaining an LLM API Account:
The user needs to visit OpenAI's API registration page and follow the on-screen instructions to create an account.

Generating an API Key:
Within the account settings or API management section, the user should locate the option to create or view API keys and generate a new API key or copy an existing one for authentication.

Importing Necessary Libraries: In the Python code, importing the libraries used for making API calls.
Setting Up API Endpoint: Obtaining the base URL for the LLM API's summarization endpoint, typically found in the provider's documentation.
Constructing API Request:
Creating a dictionary to store the API request parameters

prompt: The text to be processed by the LLM (the article content).
max_tokens: A parameter specifying the desired length of the concise summary (e.g., around 50 words).
n: A parameter to request multiple concise summaries (experimenting with different values).
Setting the headers dictionary in the request to include the API key as the Authorization value 
Sending API Request: Using the requests library to send a POST request to the API endpoint with the constructed parameters and headers.
Processing Response: Handling the API response appropriately, such as checking for errors and extracting the concise summary from the JSON response.

Code:

Python
import openai

openai.api_key = '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'

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

def main():
    # List of paths to your article files
    article_files = ['./article1.txt', './article2.txt']  # Add your file paths here
    
    for file_path in article_files:
        summary = summarize_article(file_path)
        summary_file_path = file_path.replace('.txt', '_summary.txt')
        
        with open(summary_file_path, 'w', encoding='utf-8') as summary_file:
            summary_file.write(summary)
        print(f'Summary saved to {summary_file_path}')

if __name__ == "__main__":
    main()

Explanation:

The code imports the openai library for accessing OpenAI's API.
It sets the API key for authentication with OpenAI's services.
The summarize_article function reads an article file, sends its content as a prompt to OpenAI for summarization, and returns the generated summary.
The main function iterates over a list of article files, calls summarize_article for each file, and saves the generated summaries to new files.
Finally, the script executes the main function when run directly.


Article Summarization Pipeline:

Reading Articles: Implementing a mechanism to read articles from text files, a database, or through ethical web scraping practices.
Summarizing Each Article: For each article:
Extracting the content (text) from the article.
Sending the extracted content to the LLM API following the steps outlined above.
Receiving and processing the concise summary from the API response.

Combining Title and Summary:
If the original article title is available, storing it along with the concise summary.
If the title is unavailable, using the LLM API to generate a title based on the concise summary (consulting the provider's documentation for title generation capabilities).
Saving Results: Writing the combined title and concise summary to a file (e.g., one file per article or a single file with all summaries).
Readme File Enhancement:


Clarity and Maintainability: Including clear and concise comments within the code to explain its purpose, functionality, and non-obvious logic.

API Interaction Details: Adding comments to document API request/response structure, error handling, and any specific configuration related to the LLM API being used.
Testing and Evaluation

