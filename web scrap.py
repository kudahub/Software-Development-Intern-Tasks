import requests
from bs4 import BeautifulSoup

url = "https://quotes.toscrape.com/"
page = requests.get(url)

