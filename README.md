# Eureka

This is a command-line-based YouTube video search engine that allows users to search for videos based on a brief description. The search engine ranks videos by relevance using advanced natural language processing (NLP) techniques and provides a similarity score to indicate how closely each video matches the user's query.

## Features

- **Natural Language Processing (NLP):** Utilizes state-of-the-art NLP models to process user input and video metadata.
- **Similarity Scoring:** Ranks search results based on a similarity score that reflects how closely each video matches the query.
- **Multi-Factor Ranking:** Combines text similarity with other factors such as video popularity, recency, and channel authority.
- **Customizable Output:** Allows users to specify the number of search results to display.


## Installation

### Prerequisites

- Python 3.8 or higher
- A YouTube Data API key (public data access)

### Clone the Repository

```bash
git clone hhttps://github.com/Spandan7724/Eureka.git
cd Eureka
```
## Install Dependencies

Install the required packages using the requirements.txt file:

```bash
pip install -r requirements.txt
```

## Set Up the API Key

Create a .env file in the root directory and add your YouTube Data API key:

```bash
YOUTUBE_API_KEY=your_youtube_api_key_here
```

# Usage

## Running the Search Engine

To search for videos, use the command:

```bash
python main.py "your search description here" --num_results <number_of_results>
```

For example:
```bash
python main.py "a video about the kryptos cipher by lemmino" --num_results 5
 <number_of_results>
```
This will display the top 5 video results based on your search query.

## Acknowledgements

- **Hugging Face:** For providing the NLP models used in this project.

- **YouTube Data API:** For enabling access to video metadata.

## License
This project is licensed under the MIT License.