from bs4 import BeautifulSoup
import requests, html5lib

html_doc = requests.get("https://www.test.com")
soup = BeautifulSoup(html_doc.content, 'html5lib')


print(soup.title)