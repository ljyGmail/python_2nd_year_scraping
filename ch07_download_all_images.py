import requests
from bs4 import BeautifulSoup
from pathlib import Path
import urllib
import time

# image_url = "http://python.cyber.co.kr/pds/books/python2nd/sample1.png"
# imgdata = requests.get(image_url)

# URL에서 마지막에 있는 파일명을 추출한다.
# filename = "data/ch07/" + image_url.split("/")[-1]

# 이미지 데이터를 파일에 쓴다.
# with open(filename, mode="wb") as f:
#     f.write((imgdata.content))

############################################################
# 저장용 폴더를 만든다.
# out_folder = Path("data/ch07")
# out_folder.mkdir(exist_ok=True)

# 이미지 파일을 구한다.
# image_url = "http://python.cyber.co.kr/pds/books/python2nd/sample1.png"
# imgdata = requests.get(image_url)

# URL에서 마지막에 있는 파일명을 추출하고 저장 폴더명과 연결한다.
# filename = image_url.split("/")[-1]
# out_path = out_folder.joinpath(filename)

# 이미지 데이터를 파일에 쓴다.
# with open(out_path, mode="wb") as f:
#     f.write(imgdata.content)

############################################################
# load_url = "http://python.cyber.co.kr/pds/books/python2nd/test2.html"
# html = requests.get(load_url)
# soup = BeautifulSoup(html.content, "html.parser")

# # 모든img태그를 검색해 링크를 구한다.
# for element in soup.find_all("img"):
#     src = element.get("src")

#     # 절대URL과 파일을 표시한다.
#     image_url = urllib.parse.urljoin(load_url, src)
#     filename = image_url.split("/")[-1]
#     print(image_url, ">>", filename)

############################################################
load_url = "http://python.cyber.co.kr/pds/books/python2nd/test2.html"
html = requests.get(load_url)
soup = BeautifulSoup(html.content, "html.parser")

out_folder = Path("data/ch07")
out_folder.mkdir(exist_ok=True)

for element in soup.findAll("img"):
    src = element.get("src")

    image_url = urllib.parse.urljoin(load_url, src)
    imgdata = requests.get(image_url)

    filename = image_url.split("/")[-1]
    out_path = out_folder.joinpath(filename)

    # 이미지 데이터를 파일에 쓴다.
    with open(out_path, mode="wb") as f:
        f.write(imgdata.content)

    # 한번 액세스했으므로 1초 기다린다
    time.sleep(1)
