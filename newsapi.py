from configparser import ConfigParser
import requests
import urllib.parse
import json

config = ConfigParser()

config.read('config.ini')




def generate_api_url(base_url, query, date, sort_by, api_key):
    """
    Generate a URL-encoded API request for a given company name.
    """
    query_encoded = urllib.parse.quote(query)
    return f"{base_url}?q={query_encoded}&from={date}&sortBy={sort_by}&apiKey={api_key}"

def fetch_news_and_store(base_url, companies, date, sort_by, api_key):
    """
    Fetch news articles for each company and store the results in separate JSON files.
    """
    for company in companies:
        # Generate the API request URL
        url = generate_api_url(base_url, company, date, sort_by, api_key)
        
        # Make the API call
        response = requests.get(url)
        
        # Check if the request was successful
        if response.status_code == 200:
            # Parse the JSON response
            data = response.json()
            
            # Define the file name (replacing special characters with "_")
            file_name = company.replace(' ', '_').replace('.', '').replace(',', '').replace("'", "")

            file_name = f"{file_name}.json"
            
            # Save the JSON data to a file
            with open(file_name, 'w') as file:
                json.dump(data, file, indent=4)
                
            print(f"Saved articles for {company} in {file_name}")
        else:
            print(f"Failed to fetch articles for {company}: HTTP {response.status_code}")

# Configuration
base_url = "https://newsapi.org/v2/everything"
api_key = config['DEFAULT']['API_KEY']  # Replace with your actual API key
date = "2024-01-02"
sort_by = "publishedAt"

# List of companies
companies = [
    "3M", "Aflac"
]

# Execute
fetch_news_and_store(base_url, companies, date, sort_by, api_key)

# import requests
# import json
# import urllib
# from configparser import ConfigParser

# response = requests.get("https://newsapi.org/v2/everything?q=amazon&from=2024-01-02&sortBy=publishedAt&apiKey=d9a50e694ce64d0a9606bd3c0c1a3657")
#                         #https://newsapi.org/v2/everything?q=Amazon&from=2024-01-02&sortBy=publishedAt&apiKey=d9a50e694ce64d0a9606bd3c0c1a3657

# # if response.status_code == 200:
# #     # Parse the JSON response
# #     data = response.json()
    
# #     # Define the file name (replacing special characters with "_")
# #     file_name = "amazon"

# #     file_name = f"{file_name}.json"
    
# #     # Save the JSON data to a file
# #     with open(file_name, 'w') as file:
# #         json.dump(data, file, indent=4)
        
# #     print(f"Saved articles in {file_name}")
# # else:
# #     print(f"Failed to fetch articles: HTTP {response.status_code}")

# def generate_api_url(base_url, query, date, sort_by, api_key):
#     """
#     Generate a URL-encoded API request for a given company name.
#     """
#     query_encoded = urllib.parse.quote(query)
#     return f"{base_url}?q={query_encoded}&from={date}&sortBy={sort_by}&apiKey={api_key}"

# config = ConfigParser()

# config.read('config.ini')

# # Configuration
# base_url = "https://newsapi.org/v2/everything"
# api_key = config['DEFAULT']['API_KEY']  # Replace with your actual API key
# date = "2024-01-02"
# sort_by = "publishedAt"

# # List of companies
# companies = [
#     "Amazon"
# ]

# for company in companies:
#     url = generate_api_url(base_url, company, date, sort_by, api_key)
#     print(url)