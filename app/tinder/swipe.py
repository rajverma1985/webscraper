import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from dotenv import load_dotenv
from time import sleep

load_dotenv()
email = os.environ.get('EMAIL')
password = os.environ.get('PASSWORD')
url = "https://tinder.com/"
# get the email and password from environment variables
Email = os.environ.get("TINDER_EMAIL")
Password = os.environ.get("TINDER_PASS")
Phone = os.environ.get("PHONE")
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get(url)
# get the window handle context
driver.maximize_window()
sleep(2)
# accept cookies
driver.find_element(By.XPATH, '//*[@id="q798806120"]/div/div[2]/div/div/div[1]/div[1]/button/div[2]').click()
# login
driver.find_element(By.LINK_TEXT, 'Log in').click()
sleep(2)
# login with gmail
driver.find_element(By.XPATH, '//*[@id="q-929574956"]/main/div/div[1]/div/div/div[3]/span/div/div').click()
sleep(5)
# use the second window /pop up to login
driver.switch_to.window(driver.window_handles[1])
sleep(2)
driver.find_element(By.XPATH, '//*[@id="identifierId"]').send_keys(Email)
driver.find_element(By.XPATH, '//*[@id="identifierNext"]/div/button/span').click()
sleep(2)
driver.find_element(By.XPATH, '//*[@id="password"]/div[1]/div/div[1]/input').send_keys(Password)
sleep(5)
