from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://en.wikipedia.org/wiki/Main_Page")
# sequence of search class(event-widget)>>time element which gives the value
event_times = driver.find_element(By.CSS_SELECTOR, "#articlecount a")
print(event_times.text)
