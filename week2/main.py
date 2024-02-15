from bs4 import BeautifulSoup
import requests

# with open('/Users/mistarkelly/ubuntu_shared/My-Projects/ALX-ONLY/AirBnB_clone/web_static/8-index.html', 'r') as file_html:
#     content = file_html.read()        
#     soup = BeautifulSoup(content, 'lxml')
#     articles  = soup.find_all('article')


#     for article in articles:
#         hotel_name = article.find('h2').text.strip()
#         price_by_night = article.find('div', class_='price_by_night').text.strip()
#         print(f"<{hotel_name}> at night costs {price_by_night}")


html_text = requests.get('https://www.linkedin.com/').text.strip()
soup = BeautifulSoup(html_text, 'lxml')
all_div = soup.find('li', class_='language-selector__item').find('button').text.strip()
# print(all_p)
print(all_div)

# soup = BeautifulSoup(html_text, 'lxml')

# python_course = soup.find('div', class_='popper-module--popper--2BpLn')
# print(python_course)


        


