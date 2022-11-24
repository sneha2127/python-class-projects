# List out top 100 movies on Netflix

# 1. Movie Name 
# 2. Movie Name


# Importing Modules
import requests
from bs4 import BeautifulSoup


# --------------------------------------------------

# Url Requests

url = "https://editorial.rottentomatoes.com/guide/best-netflix-movies-to-watch-right-now/"
response = requests.get(url)

web_content = response.content

# Parse the HTML
soup = BeautifulSoup(web_content,"html.parser")


# Manipulate according to requirement
headings = soup.find_all("div",class_="article_movie_title")



# Empty List to store movie name
movies = []
# --- Iterate all the elems to get link of the movie
for heading in headings:
    movie_name = heading.find("a")
    movie = movie_name.getText()
    movies.append(movie)

# Another Way optional (List Compehension)
# movies = [heading.find("a").getText() for heading in headings]



# File Generate
with open("movieList.txt","a") as f:
    for i in range(len(movies)):
        f.write(f"{i+1}: {movies[i]}\n")

    # enumerate(list)
    # for index,movie in enumerate(movies):
    #     f.write(f"{index+1}: {movie}\n")

print("You file has been generated successfully!")