import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


BEST_PLACES_LITTLE_INDIA = 'https://www.yelp.com/search?find_desc=&find_loc=Little+India%2C+Singapore'

def get_driver():
  chrome_options = Options()
  chrome_options.add_argument('--no-sandbox')
  chrome_options.add_argument('--headless')
  chrome_options.add_argument('--disable-dev-shm-usage')
  driver = webdriver.Chrome(options=chrome_options)
  return driver

def get_infos(driver):
  INFO_DIV_CLASS = 'container__09f24__mpR8_'
  driver.get(BEST_PLACES_LITTLE_INDIA)
  infos = driver.find_elements(By.CLASS_NAME,INFO_DIV_CLASS )
  return infos

def parse_info(info):
  infos
  title_tag = info.find_element(By.CLASS_NAME , 'css-1m051bw')
  title = title_tag.text
  
  url = title_tag.get_attribute('href')

  thumbnail_tag = info.find_element(By.TAG_NAME , 'img')
  thumbnail_url = thumbnail_tag.get_attribute('src')

  cusine_type = info.find_element(By.CLASS_NAME , 'css-epvm6').text.split(",")
  
  description = info.find_element(By.CLASS_NAME , 'css-16lklrv').text
  
  return {
    'title' : title,
    'url' : url,
    'thumbnail_url' : thumbnail_url,
    'cusine_type' : cusine_type,
    'description' : description
  }

if __name__ == "__main__":
  print("Creating driver")
  driver = get_driver()

  print("Fetching Best Places")
  infos = get_infos(driver) 
  
  print(f'Found {len(infos)} infos')

  print('Parsing top 10 Best places')
  places_data = [parse_info(info) for info in infos[:10]]
# title,url, thumbnail url , ratings , description

  print(places_data[3])


print('Save the Data to a CSV')
places_df = pd.DataFrame(places_data)
print(places_df)
places_df.to_csv('best_places.csv', index=None)