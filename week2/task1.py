from bs4 import BeautifulSoup

"""
Task 1: Extract State Names:

Extract the names of the states (Arizona, California) from the "locations" section.
"""

with open ('/Users/mistarkelly/ubuntu_shared/My-Projects/ALX-ONLY/AirBnB_clone/web_static/8-index.html','r') as file_html:
    content = file_html.read()
    soup = BeautifulSoup(content, 'lxml')
    
    g