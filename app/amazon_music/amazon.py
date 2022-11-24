import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from dotenv import load_dotenv
from selenium.webdriver.common.keys import Keys

load_dotenv()
# get the email and password from environment variables
Amazon_email = os.environ.get("EMAIL")
Amazon_pass = os.environ.get("PASSWORD")
url = "https://music.amazon.in/user-playlists/b85f7027a8bf4ff6badc334f4e93dd8bi8n0?marketplaceId=A3K6Y4MI8GDYMT" \
      "&musicTerritory=IN&ref=dm_sh_HFphAKldu6jIILo9VAGcs7aPa "
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get(url)
driver.maximize_window()
time.sleep(5)
playlist = driver.find_elements(By.CSS_SELECTOR, '._3bX1IY2t1o6SakF2rd-yk_ .content .col1')
time.sleep(5)
print([p.text for p in playlist])



