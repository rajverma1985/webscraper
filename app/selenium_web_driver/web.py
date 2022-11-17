from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://www.python.org/")
# sequence of search class(event-widget)>>time element which gives the value
event_times = driver.find_elements(By.CLASS_NAME, "event-widget time")
# sequence of search class>>li>>anchor_tag, which gives the value
event_names = driver.find_elements(By.CLASS_NAME, "event-widget li a")

events = {}

for n in range(len(event_times)):
    events[f"event_{n+1}"] = {
        "time": event_times[n].text,
        "topic": event_names[n].text
    }

print(events)



