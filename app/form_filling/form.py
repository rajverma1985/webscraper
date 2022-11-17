from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("http://secure-retreat-92358.herokuapp.com/")
# sequence of search class(event-widget)>>time element which gives the value
first_name = driver.find_element(By.NAME, "fName")
first_name.send_keys("Raj")
last_name = driver.find_element(By.NAME, "lName")
last_name.send_keys("Verma")
email = driver.find_element(By.NAME, "email")
email.send_keys("rverma@test.com")
submit = driver.find_element(By.CSS_SELECTOR, "button")
submit.click()
