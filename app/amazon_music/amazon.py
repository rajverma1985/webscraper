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
url = "https://music.amazon.in/"
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get(url)
time.sleep(3)
# sign in
driver.find_element(By.XPATH, '//*[@id="music-navbar"]/ul/li[5]').click()
driver.find_element(By.ID, 'signInButton').click()
driver.find_element(By.ID, 'ap_email').send_keys(Amazon_email)
driver.find_element(By.ID, 'ap_password').send_keys(Amazon_pass)
driver.find_element(By.ID, 'signInSubmit').click()
time.sleep(5)
