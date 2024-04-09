
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

To use this tool, follow these steps:

1. Clone this repository to your local machine.
2. Navigate to the project directory in your terminal.
3. Create a virtual environment (optional but recommended).
4. Install the required dependencies using the provided `requirements.txt` file:


## Usage

1. Ensure that you have your article files ready. The articles should be in plain text format (.txt).
2. Update the `article_files` list in the `project3.py` file with the paths to your article files.
3. Run the `project3.py` script using Python 3:
4. The summaries will be generated and saved as separate files with `_summary.txt` appended to the original filenames.

## File Structure

- `project3.py`: The main Python script that orchestrates the summarization process.
- `requirements.txt`: A file containing the required Python packages for this project.
- `processed_article*.txt`: Sample article files. Replace these with your own article files.
- `venv/`: A virtual environment directory (automatically created when you create a virtual environment).

## Configuration

- `openai.api_key`: Set your OpenAI API key in the `project3.py` file to authenticate with the OpenAI API.

## Notes

- This tool uses OpenAI's ChatCompletion API to generate summaries, so a stable internet connection is required.
- Ensure that your article files are in plain text format (.txt) and are accessible from the project directory.

## Credits

This project utilizes OpenAI's GPT-3.5 model for text summarization.




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

