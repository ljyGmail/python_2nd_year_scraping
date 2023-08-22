import pandas as pd

# CSV파일을 읽어 들인다.
df = pd.read_csv("data/ch08/test.csv")
print(df)

# 표 데이터 정보를  표시한다.
print("데이터 건수:", len(df))
print("항목명:", df.columns.values)
print("인덱스:", df.index.values)

# 1열의 데이터를 표시한다.
print("국어의 열 데이터:\n", df["국어"])

# 여러열의 데이터를 표시한다.
print("국어와 수학의 열 데이터:\n", df[["국어", "수학"]])

# 1행의 데이터를 표시한다.
print("C의 데이터:\n", df.loc[2])

# 여러행의 데이터를 표시한다.
print("C와D의 데이터:\n", df.loc[[2, 3]])

# 지정한 행의 지정한 열 데이터를 표시한다.
print("C의 국어 데이터:\n", df.loc[2]["국어"])

# 1열의 데이터를 추가한다.
df["미술"] = [68, 73, 82, 77, 94, 96]
print("열 데이터(미술)를 추가:\n", df)

# 1행의 데이터를 추가한다.
df.loc[6] = ["G", 90, 92, 94, 96, 92, 98]
print("행 데이터(G)를 추가:\n", df)

# <이름>열을 삭제한다.
print("<이름>열을 삭제:\n", df.drop("이름", axis=1))

# 인덱스가 2인 행을 삭제한다.
print("인텍스가 2인 행을 삭제:\n", df.drop(2, axis=0))
