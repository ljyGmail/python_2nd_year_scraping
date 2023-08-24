import pandas as pd
import folium

# df = pd.read_csv("data/ch16/firehouses.csv")

# print(len(df))
# print(df.columns.values)

# 소방서가 있는 위치(위도, 경도)를 리스트로 만든다.
# fh = df[["위도", "경도"]].values
# print(len(fh))
# print(fh)

# 지도를 만들어 HTML로 저장한다.
# m = folium.Map(location=[36.5400, 127.2700], zoom_start=12)
# folium.Marker([36.5000, 127.2541]).add_to(m)
# m.save("data/ch16/sejong.html")

df = pd.read_csv("data/ch16/firehouses.csv")

fh = df[["위도", "경도"]].values

m = folium.Map(location=[36.5400, 127.2700], zoom_start=12)
for data in fh:
    folium.Marker([data[0], data[1]]).add_to(m)

m.save('data/ch16/firehouses.html')
