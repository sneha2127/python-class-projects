import requests
from bs4 import BeautifulSoup

url = "https://www.python.org/"
response = requests.get(url)

content = response.content

soup = BeautifulSoup(content,'html.parser')

events_container = soup.find("div",class_="event-widget")
items = events_container.find("div",class_="shrubbery")
menu = items.find("ul",class_="menu")

list_items = menu.find_all("li")

events = [item.find("a").getText() for item in list_items]
times = [item.time["datetime"].split("T")[1].split("+")[0] for item in list_items]

# print(events)
# print(times)
with open("EventsList.txt","a") as f:
    for i in range(1,len(events)):
        f.write(f"{i}. Title = {events[i]}, Time = {times[i]}\n")

