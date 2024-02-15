from bs4 import BeautifulSoup

with open('/Users/mistarkelly/ubuntu_shared/My-Projects/ALX-ONLY/AirBnB_clone/web_static/8-index.html', 'r') as file_html:
    content = file_html.read()        
    soup = BeautifulSoup(content, 'lxml')
    articles  = soup.find_all('article')


    for article in articles:
        hotel_name = article.find('h2').text.strip()
        price_by_night = article.find('div', class_='price_by_night').text.strip()
        print(f"<{hotel_name}> at night costs {price_by_night}")

        
