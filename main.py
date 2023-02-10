import requests
from bs4 import BeautifulSoup

def find_cheap_items(max_price):
    URL = "https://www.ebay.com/b/Cheap-Stuff/bn_7115020275"
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, "html.parser")
    items = soup.find_all("li", class_="s-item")

    cheap_items = []
    for item in items:
        title = item.find("h3", class_="s-item__title").text
        price = item.find("span", class_="s-item__price").text

        # Extract the numeric value of the price
        price = float(price.strip("$"))

        if price <= max_price:
            cheap_items.append((title, price))

    return cheap_items

cheap_stuff = find_cheap_items(20)
for item in cheap_stuff:
    print(f"{item[0]} - ${item[1]:.2f}")
