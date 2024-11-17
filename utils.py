import requests
from config import SERPAPI_API_KEY, GROQ_API_KEY

def search_web(entity, prompt_template):
    query = prompt_template.format(company=entity)
    url = f"https://serpapi.com/search?q={query}&api_key={SERPAPI_API_KEY}"
    response = requests.get(url)
    print("Search Results:", response.json())  # For debugging, can remove in production
    return response.json() if response.status_code == 200 else None

def parse_results_with_groq(results, prompt_template):
    prompt = f"Extract the needed information based on: {prompt_template}. Here are the results: {results}"

    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json"
    }

    # Replace with actual Groq endpoint if different
    groq_endpoint_url = "https://api.groq.com/v1/parse"

    # Payload for the Groq API request
    data = {
        "prompt": prompt,
        "max_tokens": 150  # Adjust tokens based on your requirement
    }

    try:
        response = requests.post(groq_endpoint_url, headers=headers, json=data)
        response.raise_for_status()  # Check for HTTP request errors
        return response.json().get('text', "No data found").strip()
    except requests.exceptions.RequestException as e:
        print(f"Error with Groq API: {e}")
        return "No data found"
