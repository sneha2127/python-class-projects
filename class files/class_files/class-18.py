# Live Scrapping Using BeutifulSoup and requests


# Step 1: Installation
# pip install requests
# pip install bs4


# Step 2: Request a webpage

import requests
from bs4 import BeautifulSoup

url = "https://www.python.org/"
response = requests.get(url)


# Storing HTML content in the string format
web_content = response.content


# Step-3: Parsing the html code
soup = BeautifulSoup(web_content,"html.parser")

# prettify(): Represent HTML Code in a beautiful format
# print(soup.prettify())


# Step-4: Manipulate The Web Page
# web_title = soup.find("title")
# print(web_title.get_text())


# Manipulate News Section ul tag with class menu

news_container = soup.find("div",class_="blog-widget")
menu_section = news_container.find("ul",class_="menu")
news_code = menu_section.find_all("a")


for news in news_code:
    print(news.get_text())


# Event Collection - Practice Problem (https://python.org/)

# Generate a text file containing title of the even with the time or date
# File Output:
# 1. title="title", time="time"
# 2. title="title", time="time"
# 3. title="title", time="time"
# 4. title="title", time="time"
# 5. title="title", time="time"
