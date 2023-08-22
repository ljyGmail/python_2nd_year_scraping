import requests
from bs4 import BeautifulSoup

load_url = "https://news.daum.net/issue/512957"
html = requests.get(load_url)
soup = BeautifulSoup(html.content, "html.parser")

# class로 검색하고 그 안에 있는 모든a태그를 검색해 표시한다.
topic = soup.find(class_="list_newsissue")
for element in topic.find_all("a"):
    print(element.text.strip())
