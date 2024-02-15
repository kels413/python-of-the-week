from task1 import soup
import re
"""
Task 3: Extract Place Information:

Extract information about each place, including the place name, price per night, maximum guests, number of rooms, number of bathrooms, owner, and description.
"""

places = soup.find_all('article')


for place in places:
    place_name = place.find('h2').text.strip()
    print(place_name)
    price_by_night = place.find('div', class_='price_by_night').text.strip()
    print(price_by_night)
    maximum_guest = place.find('div', class_='max_guest').text.strip()
    print(maximum_guest)
    no_of_rooms = place.find('div', class_='number_rooms').text.strip()
    print(no_of_rooms)
    no_of_bathrooms = place.find('div', class_='number_bathrooms').text.strip()
    print(no_of_bathrooms)
    owner = place.find('div', class_='owner').find('p').text
    print(owner)
    
    description = place.find('div', class_='description').find('p').text.strip()
    description = re.sub(r'\s+', '', description)

    print(description)
