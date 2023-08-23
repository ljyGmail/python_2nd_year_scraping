import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc

# 한글 깨지는 문제 해결
font_location = "C:/Windows/Fonts/malgun.ttf"
font_name = font_manager.FontProperties(fname=font_location).get_name()
rc('font', family=font_name)

# df = pd.read_csv("data/ch10/test.csv")

# 파일을 읽어 들인다.
# df.plot()
# plt.show()

# 막대 그래프를 만들어 표시한다.
# df.plot.bar()
# plt.legend(loc="lower right")
# plt.show()

# 막대 그래프(수평)를 만들어 표시한다.
# df.plot.barh()
# plt.legend(loc="lower left")
# plt.show()

# 누적 막대 그래프를 만들어 표시한다.
# df.plot.bar(stacked=True)
# plt.legend(loc="lower right")
# plt.show()

# 상자 수염 그래프를 만들어 표시한다.
# df.plot.box()
# plt.show()

# 면적 그래프를 만들어 표시한다.
# df.plot.area()
# plt.legend(loc="lower right")
# plt.show()

# CSV파일을 읽어 들인다(이름 열을 인덱스로 한다).
df = pd.read_csv("data/ch10/test.csv", index_col=0)

# 국어에 대한 막대 그래프를 만들어 표시한다.
df["국어"].plot.barh()
plt.legend(loc="lower left")
plt.show()

# 국어와 수학에 대한 막대 그래프를 만들어 표시한다.
df[["국어", "수학"]].plot.barh()
plt.legend(loc="lower left")
plt.show()

# C군에 대한 막대 그래프를 만들어 표시한다.
df.loc["C"].plot.barh()
plt.legend(loc="lower left")
plt.show()

# C군에 대한 원 그래프를 만들어 표시한다.
df.loc["C"].plot.pie(labeldistance=0.6)
plt.legend(loc="lower left")
plt.show()

# 막대 그래프를 만들어 이미지 파일로 출력한다.
df.T.plot.bar()
plt.legend(loc="lower right")
plt.show()

# 막대 그래프의 색을 지정한다.
colorlist = ["skyblue", "steelblue", "tomato", "cadetblue", "orange", "sienna"]
df.T.plot.bar(color=colorlist)
plt.legend(loc="lower right")
# plt.show()

# 그래프를 이미지 파일로 저장한다.
plt.savefig("data/ch10/bargraph.png")
