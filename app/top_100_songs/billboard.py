import datetime

import requests
from bs4 import BeautifulSoup

url="https://www.billboard.com/charts/hot-100"
now = datetime.datetime.now()
date = input("Please enter a date in yyyy-mm-dd format:\n")
response = requests.get(f"{url}/{date}")
soup = BeautifulSoup(response.text, "html.parser")

top_100 = soup.find_all(name="h3", id="title-of-a-story", class_="a-chart-detail-open")
song_list = [n.text.strip() for n in top_100]
print(song_list)

