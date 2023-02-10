# Cheap Ebay Parser

Here's a basic implementation of a Python parser that can scrape the eBay website and find items that are priced cheaply.

This script uses the requests library to get the HTML content of the eBay page and BeautifulSoup to parse it and extract information about each item. It find all items with the class s-item and then check if the price is less than or equal to the max_price argument. If it is, the item is added to the list of cheap items. Finally, the last of cheap items is returned and printed to the console.

Note that web scraping can be against the terms of service of websites and can change frequently, so this code may not work in the future.
