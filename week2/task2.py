from task1 import soup

"""
Task 2: Extract Subpage Links:

Extract the links from the "popover" section under the "Arizona" and "California" states. These links represent subpages.
"""


li_links = soup.find_all('li')

for li_link in li_links:
  li_link_text = li_link.text.strip()
  print(f"all the links are {li_link_text}")

