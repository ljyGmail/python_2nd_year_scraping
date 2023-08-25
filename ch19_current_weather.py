import requests
import json
from pprint import pprint

# ans = "오늘은{key1}입니다.내일은{key2}입니다."
# print(ans)

# ans = ans.format(key1="맑음", key2="흐림")
# print(ans)

# 제주의 현재 날찌를 구한다.
url = "http://api.openweathermap.org/data/2.5/weather?q={city}&appid={key}&lang=kr&units=metric"
url = url.format(city="Jeju,KR", key="3c2f7ae11cc7fb2cf1e03805bc7e5376")

jsondata = requests.get(url).json()
# print(jsondata)

# with open("data/ch19/test2.json", mode="r") as f:
#     jsondata = json.loads(f.read())
#     pprint(jsondata)
#     print("첫번쨰 오브젝트:", jsondata[0])
#     print("도시명:", jsondata[0]["name"])
#     print("위도:", jsondata[0]["coord"]["lat"])
#     print("경도:", jsondata[0]["coord"]["lon"])

# pprint(jsondata)

print("도시명:", jsondata["name"])
print("기온:", jsondata["main"]["temp"])
print("날씨:", jsondata["weather"][0]["main"])
print("상세 날씨:", jsondata["weather"][0]["description"])

url = "http://api.openweathermap.org/data/2.5/weather?q={city}&appid={key}&lang=kr&units=metric"
url = url.format(city="New York,US", key="3c2f7ae11cc7fb2cf1e03805bc7e5376")
jsondata = requests.get(url).json()
print("도시명:", jsondata["name"])
print("기온:", jsondata["main"]["temp"])
print("날씨:", jsondata["weather"][0]["main"])
print("상세 날씨:", jsondata["weather"][0]["description"])

url = "http://api.openweathermap.org/data/2.5/weather?q={city}&appid={key}&lang=kr&units=metric"
url = url.format(city="London,UK", key="3c2f7ae11cc7fb2cf1e03805bc7e5376")
jsondata = requests.get(url).json()
print("도시명:", jsondata["name"])
print("기온:", jsondata["main"]["temp"])
print("날씨:", jsondata["weather"][0]["main"])
print("상세 날씨:", jsondata["weather"][0]["description"])

# 우편번호로 날씨를 구한다.
url = "http://api.openweathermap.org/data/2.5/weather?zip={zipcode}&appid={key}&lang=kr&units=metric"
url = url.format(zipcode="10029,US", key="3c2f7ae11cc7fb2cf1e03805bc7e5376")
jsondata = requests.get(url).json()
print("도시명:", jsondata["name"])
print("기온:", jsondata["main"]["temp"])
print("날씨:", jsondata["weather"][0]["main"])
print("상세 날씨:", jsondata["weather"][0]["description"])
