import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc

# 한글 깨지는 문제 해결
font_location = "C:/Windows/Fonts/malgun.ttf"
font_name = font_manager.FontProperties(fname=font_location).get_name()
rc('font', family=font_name)

df = pd.read_csv("data/ch14/stat_100701.csv", index_col="전국 지역별")
# print(len(df))
# print(df.columns.values)

# print(df["2018년"])
# 2018년 열 데이터로 막대 그래프를 만들어 표시한다.
# df["2018년"].plot.bar() # no numeric data to plot
# df["2018년"] = pd.to_numeric(df["2018년"].str.replace(",", ""))
# print(df["2018년"])
# df["2018년"].plot.bar()
# plt.show()

# df = df.drop("전국", axis=0)
# df["2018년"] = pd.to_numeric(df["2018년"].str.replace(",", ""))
# 인구가 많은 순으로 정렬한다.
# df = df.sort_values("2018년", ascending=False)
# df["2018년"].plot.bar(figsize=(10, 6))
# plt.show()

df = df.drop("전국", axis=0)
df["2017년"] = pd.to_numeric(df["2017년"].str.replace(",", ""))
df["2018년"] = pd.to_numeric(df["2018년"].str.replace(",", ""))
df["인구 증감"] = df["2018년"] - df["2017년"]
df = df.sort_values("인구 증감", ascending=False)
df["인구 증감"].plot.bar(figsize=(10,  6))
# 세로축의 스케일을 저정한다.
plt.ylim(-40, 13000)
plt.show()
