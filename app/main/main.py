import requests
from bs4 import BeautifulSoup

response = requests.get("https://news.ycombinator.com/")
soup = BeautifulSoup(response.text, "html.parser")
news = soup.find_all(name="span", class_="titleline")

link = []
title = []
score_list = []

for article in news:
    link.append(article.find(name="a").get("href"))
    title.append(article.find(name="a").getText())
print(link)
print(title)

scores = soup.find_all(class_="score")
for score in scores:
    score_list.append(score.getText())

print(score_list)






