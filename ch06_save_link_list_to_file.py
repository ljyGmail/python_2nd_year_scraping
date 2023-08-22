import requests
from bs4 import BeautifulSoup
import urllib

load_url = "https://python.cyber.co.kr/pds/books/python2nd/test2.html"
html = requests.get(load_url)
soup = BeautifulSoup(html.content, "html.parser")

# 모든a태그를 검색하고 링크를 표시한다.
# for element in soup.find_all("a"):
# print(element.text)
# url = element.get("href") # href속성값이 절대경로일 수도 있고, 상대경로일 수도 있다
# print(url)
# url = element.get("href")
# link_url = urllib.parse.urljoin(load_url, url)
# print(link_url)

# 파일을 쓰기 모드로 연다.
filename = "data/ch06/linklist.txt"
with open(filename, "w", encoding="utf-8") as f:
    # 모든a태그를 검색하고 링크를 절대 URL로 표시한다.
    for element in soup.find_all("a"):
        url = element.get("href")
        link_url = urllib.parse.urljoin(load_url, url)
        f.write(element.text + "\n")
        f.write(link_url + "\n")
        f.write("\n")
