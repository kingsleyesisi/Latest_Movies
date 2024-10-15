from django.test import TestCase

# Create your tests here.
import requests
from bs4 import BeautifulSoup

# List to store movie data
latest_movies = []


# Extracting movie data from Rotten Tomatoes
for no in range(1,4):
    url = f"https://www.rottentomatoes.com/browse/movies_in_theaters/sort:newest?page={no}"
    response = requests.get(url)
    response = response.content
    soup = BeautifulSoup(response, 'html.parser')
    container = soup.find_all('div', class_ = 'flex-container')
    
for movie in container:
    Title = movie.find('span', class_='p--small').text.strip()
    release = movie.find('span', class_='smaller').text.strip()
    image_tag = movie.find('rt-img', class_='posterImage')
    if image_tag:
        image = image_tag['src']

    latest_movies.append([Title, release, image])  # Append image along with title and release


data = {'Title': [movie[0] for movie in latest_movies],
         'Release_Date': [movie[1] for movie in latest_movies],
        'image': [movie[2] for movie in latest_movies],
        }
