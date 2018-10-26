from Lib.urllib.request import urlopen
from bs4 import BeautifulSoup as soup
import pandas as pd


my_url = "https://www.newegg.ca/Product/ProductList.aspx?Submit=ENE&DEPA=0&Order=BESTMATCH&Description=graphic+cards&N=-1&isNodeId=1"

# opening connection, grab the page
uClient = urlopen(my_url)
page_html = uClient.read()
uClient.close()

page_soup = soup(page_html, features="html.parser")

# grab all products on the page
containers = page_soup.find_all("div", {"class": "item-container"})

# write data into csv file
filename = "test_products.csv"
f = open(filename, "w")
headers = "brand, product_name, shipping\n"
f.write(headers)

for container in containers:
    brand = container.div.div.a.img["title"]

    title_container = container.find_all("a", attrs={"class": "item-title"})
    product_name = title_container[0].text

    shipping_container = container.find_all("li", {"class": "price-ship"})
    shipping = shipping_container[0].text.strip()

    f.write(brand + "," + product_name.replace(",", "|") + "," + shipping + "\n")

f.close()
