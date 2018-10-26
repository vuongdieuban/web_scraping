from Lib.urllib import request
from bs4 import BeautifulSoup
import pandas as pd

desired_width=320
pd.set_option('display.width', desired_width)
pd.set_option('display.max_columns',10)

cities = "https://simple.wikipedia.org/wiki/Provinces_and_territories_of_Canada"
page = request.urlopen(cities)
soup = BeautifulSoup(page, features="html.parser")

city_table = soup.find('table', class_='wikitable')

province = []
abbreviation = []
capitalCity = []
largestCity = []
category = set()

for row in city_table.find_all('tr'):
    cell = row.find_all('td')
    header = row.find_all('th')
    if len(header) is not 0:
        for i in header:
            category.add(i.get_text())
    if len(cell) is not 0:
        province.append(cell[0].get_text())
        abbreviation.append(cell[1].get_text())
        capitalCity.append(cell[2].get_text())
        largestCity.append(cell[3].get_text())

category = list(category)

df = pd.DataFrame()
df['Province'] = province
df['Abbreviation'] = abbreviation
df['Capital city'] = capitalCity
df['Largest city'] = largestCity


print(df)









