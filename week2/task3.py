from task1 import soup
import re
"""
Task 3: Extract Place Information:

Extract information about each place, including the place name, price per night, maximum guests, number of rooms, number of bathrooms, owner, and description.
"""

places = soup.find_all('article')

# for place in places:
#     place_name = place.find('h2').text.strip()
#     price_by_night = place.find('div', class_='price_by_night').text.strip()
#     maximum_guest = place.find('div', class_='max_guest').text.strip()
#     no_of_rooms = place.find('div', class_='number_rooms').text.strip()
#     no_of_bathrooms = place.find('div', class_='number_bathrooms').text.strip()
#     owner = place.find('div', class_='owner').find('p').text
#     description = place.find('div', class_='description').find('p').text.strip()
#     # description = re.sub(r'\s+', ' ', description)
#     print(f"{owner}\nPlace-name:{place_name}\nprice-by-night:{price_by_night}\nmax-guest{maximum_guest}\nno-rooms: {no_of_rooms}\nno-bathrooms:{no_of_bathrooms}\ndescription:{description}")
#     print()

i = 0
classes = ['price_by_night', 'max-guest', 'number_rooms', 'number_bathrooms', 'owner', 'description']
storage = []
for place in places:
    classes[i] = place.find('div', place).text
    

    # place_name =  place.find('div', classes[i])
    # price_by_night = place.find('div', classes[i])
    # max_guest =  place.find('div', classes[i])
    i+=1
    print(classes)
   

