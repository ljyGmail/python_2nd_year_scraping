import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc

# 한글 깨지는 문제 해결
font_location = "C:/Windows/Fonts/malgun.ttf"
font_name = font_manager.FontProperties(fname=font_location).get_name()
rc('font', family=font_name)

# df1 = pd.read_csv("data/ch15/Sample_1.csv", index_col="일시")
# df2 = pd.read_csv("data/ch15/Sample_2.csv", index_col="일시")
# df3 = pd.read_csv("data/ch15/Sample_3.csv", index_col="일시")

# print(df1.columns.values)
# print(df2.columns.values)
# print(df3.columns.values)

# df1 = pd.read_csv("data/ch15/Sample_1.csv", index_col="일시")

# 평균기온으로 꺾은선 그래프를 표시한다.
# df1["평균기온(°C)"].plot()
# plt.ylim(-10, 40)
# plt.show()

df1 = pd.read_csv("data/ch15/Sample_1.csv", index_col="일시")
df2 = pd.read_csv("data/ch15/Sample_2.csv", index_col="일시")
df3 = pd.read_csv("data/ch15/Sample_3.csv", index_col="일시")

# 3개의 그래프를 겹쳐 표시한다.
df1["평균기온(°C)"].plot()
df2["최고기온(°C)"].plot()
df3["최저기온(°C)"].plot()
plt.ylim(-40, 50)
plt.legend(loc="lower right")
plt.show()
