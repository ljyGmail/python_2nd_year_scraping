import requests
import json
from pprint import pprint
from datetime import datetime, timedelta, timezone
import pandas as pd
import matplotlib.pyplot as plt

# 서울의 5일 동안(3시간 간격)의 날씨를 구한다.
url = "http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={key}&lang=kr&units=metric"
url = url.format(city="Seoul,KR", key="3c2f7ae11cc7fb2cf1e03805bc7e5376")

jsondata = requests.get(url).json()
# pprint(jsondata)

####################
# UTF(협정 세계시)를 KST(한국 표준시)로 변환한다.
# timestampe = 1595257200

# tz = timezone(timedelta(), 'UTC')
# utc = datetime.fromtimestamp(timestampe, tz)
# print(utc)

# tz = timezone(timedelta(hours=+9), 'KST')
# kst = datetime.fromtimestamp(timestampe, tz)
# print(kst)
# print(str(kst)[:-9])

####################
# tz = timezone(timedelta(hours=+9), 'KST')
# for dat in jsondata["list"]:
#     kst = str(datetime.fromtimestamp(dat["dt"], tz))[:-9]
#     # print("UST={ust}, KST={kst}".format(ust=dat["dt_txt"], kst=kst))
#     weather = dat["weather"][0]["description"]
#     temp = dat["main"]["temp"]
#     print("날짜: {kst}, 날씨: {w}, 기온: {t}도".format(kst=kst, w=weather, t=temp))

df = pd.DataFrame(columns=["기온"])
tz = timezone(timedelta(hours=+9), 'KST')

for dat in jsondata["list"]:
    kst = str(datetime.fromtimestamp(dat["dt"], tz))[:-9]
    temp = dat["main"]["temp"]
    df.loc[kst] = temp

# pprint(df)

df.plot(figsize=(15, 8))
plt.ylim(-10, 40)
plt.grid()
plt.show()
