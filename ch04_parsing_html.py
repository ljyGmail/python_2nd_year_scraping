import requests
from bs4 import BeautifulSoup

# 웹 페이지를 구해 해석한다.
# load_url = "https://python.cyber.co.kr/pds/books/python2nd/test1.html"
# html = requests.get(load_url)
# soup = BeautifulSoup(html.content, "html.parser")

# HTML전체를 표시한다.
# print(soup)

# title, h2, li 태그를 검색해 표시한다.
# print(soup.find('title'))
# print(soup.find('h2'))
# print(soup.find('li'))

# title, h2, li 태그를 검색하고 문자열을 표시한다.
# print(soup.find('title').text)
# print(soup.find('h2').text)
# print(soup.find('li').text)

load_url = "https://python.cyber.co.kr/pds/books/python2nd/test2.html"
html = requests.get(load_url)
soup = BeautifulSoup(html.content, "html.parser")

# 모든 li태그를 검색하고 그문자열을 표시한다.
# for element in soup.find_all("li"):
#     print(element.text)

# ID로 검색해 그 태그의 내용을  표시한다.
chap2 = soup.find(id="chap2")
# print(chap2)
for element in chap2.find_all("li"):
    print(element.text)
