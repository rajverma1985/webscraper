import requests
from bs4 import BeautifulSoup

#<h3 class="jsx-4245974604">99) Groundhog Day</h3>

response = requests.get("https://www.empireonline.com/movies/features/best-movies-2")
soup = BeautifulSoup(response.text, "html.parser")
movies = soup.find_all(class_='jsx-3821216435 listicle-item')
print(movies)

## TODO issues with the site structure, need to use selenium for scraping.

