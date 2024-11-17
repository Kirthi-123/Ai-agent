# Ai-agent
An AI agent that reads through a dataset (CSV or Google Sheets) and performs a web search to retrieve specific information for each entity in a chosen column.

AI-Agent-Project/
│
├── main.py                  # Main Streamlit app file
├── utils.py                 # Helper functions for web search and Groq processing
├── config.py                # Stores API keys and credentials
├── requirements.txt         # Lists required Python libraries
|__ README.md                # Project documentation

# AI Agent for Automated Information Retrieval

## Overview




This project is a Streamlit-based application that enables users to retrieve and process information from uploaded CSV files or Google Sheets. It performs the following tasks:

1. Upload and preview data from a CSV or Google Sheet.
2. Select a main column to process.
3. Define a custom prompt to retrieve specific information for each entity.
4. Perform a web search using SerpAPI and process the results using Groq's API for natural language processing.
5. Display and download the extracted information in a CSV format.

## Features

- **CSV and Google Sheets Support**: Upload a CSV or connect to a Google Sheet for data input.
- **Custom Prompt Input**: Define a dynamic prompt for each entity (e.g., "Find the contact email for {company}").
- **Automated Web Search**: Use SerpAPI to fetch web search results for each entity.
- **Groq API Integration**: Process search results to extract specific information using Groq’s natural language processing capabilities.
- **User-Friendly Interface**: Streamlit-based interface for ease of use.
- **Downloadable Results**: Download the processed data as a CSV file.

---

## Setup Instructions

### Prerequisites

- Python 3.7 or higher
- API keys for:
  - [SerpAPI](https://serpapi.com/)
  - [Groq](https://www.groq.com/)
  - [Google Cloud Console](https://console.cloud.google.com/) (for Google Sheets integration)

### Installation

1. **Clone the Repository**:
 git clone https://github.com/your-repo/ai-agent.git
 cd ai-agent
   
2. **Create a Virtual Environment**:
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`

3. **Install Dependencies**:
pip install -r requirements.txt

4. **Set Up API Keys**:
Open config.py and add your API keys:
SERPAPI_API_KEY = "your_serpapi_api_key"
GROQ_API_KEY = "your_groq_api_key"
GOOGLE_SHEETS_CREDENTIALS = {
    ###Paste your Google Service Account JSON key contents here
}

Run the Streamlit App:
streamlit run main.py

Upload a CSV or Enter Google Sheets URL:
Upload a CSV file containing entities or connect to a Google Sheet by entering its URL.

Select a Main Column:
Choose the column containing the entities (e.g., company names) you want to process.

Define a Custom Prompt:
Enter a prompt such as "Find the contact email for {company}". Use {company} as a placeholder for entities.

Start Processing:
Click the "Start Processing" button to fetch and process data.

View and Download Results:
The extracted information will be displayed in a table. Download it as a CSV file.
