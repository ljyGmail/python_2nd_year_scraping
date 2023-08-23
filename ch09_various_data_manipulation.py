import pandas as pd

df = pd.read_csv("data/ch09/test.csv")

# 조건에 맞는 데이터를 추출한다.
data_s = df[df["국어"] >= 90]
print("국어가 90점 이상:\n", data_s)

data_c = df[df["수학"] < 70]
print("수학이 70점 미만:\n", data_c)

# 집계(최댓값, 최솟값, 평균값, 중앙값, 합계값 등)를 해 표시한다.
print("수학의 최고점:", df["수학"].max())
print("수학의 최저점:", df["수학"].min())
print("수학의 평균값:", df["수학"].mean())
print("수학의 중앙값:", df["수학"].median())
print("수학의 점수 합계:", df["수학"].sum())

# 정렬해 표시한다.
kor = df.sort_values("국어", ascending=False)
print("국어 점수가 높은 순으로 정렬:\n", kor)

# 행과 열을 바꾼다.
print("행과 열을 바꾼다:\n", df.T)

# 데이터를 리스트로 만든다.
print("Python의 리스트 데이터화:\n", df.values)

# CSV파일로 출력한다.
kor.to_csv("data/ch09/export1.csv")

# CSV파일로 출력한다(인덱스 삭제).
kor.to_csv("data/ch09/export2.csv", index=False)

# CSV파일로 출력한다(인덱스와 헤더 삭제).
kor.to_csv("data/ch09/export3.csv", index=False, header=False)
