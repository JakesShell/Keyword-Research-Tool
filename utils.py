# app/utils.py
import requests
from bs4 import BeautifulSoup

def get_keywords(seed_keyword):
    # This function would normally call an external API or scrape a website
    # For demonstration, we'll return mock data
    return [
        {"keyword": f"{seed_keyword} example 1", "volume": 1000, "competition": 0.5},
        {"keyword": f"{seed_keyword} example 2", "volume": 500, "competition": 0.3},
        {"keyword": f"{seed_keyword} example 3", "volume": 2000, "competition": 0.7},
    ]
