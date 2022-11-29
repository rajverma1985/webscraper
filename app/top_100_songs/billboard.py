import datetime
import requests
from bs4 import BeautifulSoup

url = "https://www.billboard.com/charts/hot-100"
now = datetime.datetime.now()
date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")
response = requests.get(f"{url}/{date}")
soup = BeautifulSoup(response.text, "html.parser")
songs_100 = soup.find_all("h3", id="title-of-a-story", class_="lrv-u-font-size-16")
song_list = [song.getText().strip() for song in songs_100]
print(song_list)