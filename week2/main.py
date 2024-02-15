from bs4 import BeautifulSoup

with open('/Users/mistarkelly/ubuntu_shared/My-Projects/ALX-ONLY/AirBnB_clone/web_static/8-index.html', 'r') as file_html:
    content = file_html.read()        
    soup = BeautifulSoup(content, 'lxml')
    all_h1_tag = soup.find_all('h2')

    for i in all_h1_tag:
        print(i.text)
        
    # print(all_h1_tag)

# create an instance of soup


