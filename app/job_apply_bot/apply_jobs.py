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
Email = os.environ.get("EMAIL")
Password = os.environ.get("PASSWORD")
Phone = os.environ.get("PHONE")
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://www.linkedin.com/jobs/search/?f_LF=f_AL&geoId=102257491&keywords=python%20developer&location"
           "=London%2C%20England%2C%20United%20Kingdom&redirect=false&position=1&pageNum=0")

# Send info to LinkedIn to login first and then apply to the jobs
driver.maximize_window()
driver.find_element(By.LINK_TEXT, "Sign in").click()
user_name = driver.find_element(By.ID, "username")
user_name.send_keys(Email)
password = driver.find_element(By.ID, "password")
password.send_keys(Password)
password.send_keys(Keys.ENTER)

driver.find_element(By.CLASS_NAME, "jobs-apply-button--top-card").click()
phone_entry = driver.find_element(By.CLASS_NAME, "fb-single-line-text__input")
if phone_entry.text == "":
    phone_entry.send_keys(Phone)

driver.find_element(By.CSS_SELECTOR, "footer button").click()

# Todo: add functionality to apply to a job with relevant job type/description

driver.find_element(By.CSS_SELECTOR, ".justify-flex-end .artdeco-button--primary").click()
driver.find_element(By.XPATH, '/html/body/div[3]/div/div/div[2]/div/div[2]/div/footer/div[1]/label').click()

time.sleep(5)
driver.close()
