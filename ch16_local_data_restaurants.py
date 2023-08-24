import pandas as pd
import folium

df = pd.read_csv("data/ch16/restaurants.csv")

# print(len(df))
# print(df.columns.values)

# 식당이 있는 위치(위도, 경도)를 리스트로 만든다.
store = df[["위도", "경도", "업소명"]].values
# print(len(store))
# print(store)

# 지도를 만들어 HTML로 저장한다.
m = folium.Map(location=[33.3530, 126.5159], zoom_start=11)
for data in store:
    folium.Marker([data[0], data[1]], tooltip=data[2]).add_to(m)
m.save("data/ch16/store.html")
