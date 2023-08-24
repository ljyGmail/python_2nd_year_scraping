import pandas as pd

df = pd.read_csv("data/ch13/20200602_SEOUL.csv", header=None)
print(len(df))
print(df.columns.values)

# '0'열이 '02561'인 주소를 추출해 표시한다.
results = df[df[0] == 2561]
print(results[[0, 1, 2, 3, 4]])

# '3'열이 '개포로'인 주소를 추출해 표시한다.
results = df[df[3] == "개포로"]
print(results[[0, 1, 2, 3, 4]])

results = df[df[3].str.contains("개포로")]
print(results[[0, 1, 2, 3, 4]])
