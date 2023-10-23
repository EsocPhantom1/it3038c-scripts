import requests
from bs4 import BeautifulSoup

data = requests.get("https://www.reebok.com/c/600000048/collection-classics-basketball").content
soup = BeautifulSoup(data, 'html.parser')

# Find the title
title_span = soup.find("p", class_="tag_p--1xo5V product-card-name--9ffy7")
title = title_span.text if title_span else "Title not found"

# Find the price
price_span = soup.find("p", class_="tag_p--1xo5V product-card-regular--2tBvS")
price = price_span.text if price_span else "Price not found"

print(f"Item: {title} has price of {price}")
