"""
Sports Data Aggregator:

a program that scrapes sports websites for live scores, upcoming fixtures, and player statistics. also provides a centralized hub for sports enthusiasts to stay updated.

site to scrape: 
"""
from bs4 import BeautifulSoup
import requests

html_text = requests.get('https://www.livescore.com/en/').text
soup = BeautifulSoup(html_text, 'lxml')


# filtering out more than one post from the user.
    # unfamiliar_string = input('> '): linux, devops, bash
# enumerate function