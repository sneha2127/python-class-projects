import requests
from bs4 import BeautifulSoup

url = "https://www.chosic.com/playlist-generator/?track=7eQl3Yqv35ioqUfveKHitE"

response = requests.get(url, verify=False)

content = response.content

soap = BeautifulSoup(content,"html.parser")

all_suggests = soap.find_all("div",class_="track-list-item")
# print(all_suggests.prettify())
for item in all_suggests:
    print(item.find("h3").find("a").getText())
