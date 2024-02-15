from task1 import soup
"""
Task 3: Extract Place Information:

Extract information about each place, including the place name, price per night, maximum guests, number of rooms, number of bathrooms, owner, and description.
"""

places = soup.find_all('article')


for place in places:
    place_name = place.find('h2').text.strip()
    price_by_night = place.find('div', class_='price_by_night')
    print(price_by_night)

    
    print(place_name)
