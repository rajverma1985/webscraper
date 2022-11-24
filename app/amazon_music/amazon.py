import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from dotenv import load_dotenv

load_dotenv()
# get the email and password from environment variables
Amazon_email = os.environ.get("EMAIL")
Amazon_pass = os.environ.get("PASSWORD")
url = "https://music.amazon.in/user-playlists/b85f7027a8bf4ff6badc334f4e93dd8bi8n0?marketplaceId=A3K6Y4MI8GDYMT" \
      "&musicTerritory=IN&ref=dm_sh_HFphAKldu6jIILo9VAGcs7aPa "
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get(url)
driver.maximize_window()
time.sleep(2)
scroll_pause_time = .5 # You can set your own pause time. My laptop is a bit slow so I use 1 sec
screen_height = driver.execute_script("return window.screen.height;")   # get the screen height of the web
i = 1
playlist = []
while True:
    # scroll one screen height each time
    for song in driver.find_elements(By.CSS_SELECTOR,
                                     '._3yhmPlrZ9kJ1NcTx4yoBLu ._3bX1IY2t1o6SakF2rd-yk_ .content .col1'):
        playlist.append(song.text)
    time.sleep(2)
    driver.execute_script("window.scrollTo(0, {screen_height}*{i});".format(screen_height=screen_height, i=i))
    i += 1
    time.sleep(scroll_pause_time)
    # update scroll height each time after scrolled, as the scroll height can change after we scrolled the page
    scroll_height = driver.execute_script("return document.body.scrollHeight;")
    # Break the loop when the height we need to scroll to is larger than the total scroll height
    if screen_height * i > scroll_height:
        break


for song in playlist:
    print(song)


