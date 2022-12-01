import requests
from bs4 import BeautifulSoup

BEST_PLACES_LITTLE_INDIA = 'https://www.yelp.com/search?find_desc=&find_loc=Little+India%2C+Singapore'



response = requests.get(BEST_PLACES_LITTLE_INDIA)
print('Status Code', response.status_code)
with open('best places.html', 'w') as f:
  f.write(response.text)

doc = BeautifulSoup(response.text, 'html.parser')

print('Page title:', doc.title)

info_divs = doc.find_all('div',class_ = ' padding-t3__09f24__TMrIW padding-r3__09f24__eaF7p padding-b3__09f24__S8R2d padding-l3__09f24__IOjKY border-color--default__09f24__NPAKY')

print(f'Found {len(info_divs)} info')