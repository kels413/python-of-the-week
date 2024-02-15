from bs4 import BeautifulSoup

with open('/Users/mistarkelly/ubuntu_shared/My-Projects/ALX-ONLY/AirBnB_clone/web_static/8-index.html') as file_html:
    content = file_html.read()
    print(content)