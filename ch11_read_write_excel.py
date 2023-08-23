import pandas as pd
import openpyxl

df = pd.read_csv("data/ch11/test.csv")

# 국어 점수가 높은 순으로 정렬한다.
kor = df.sort_values("국어", ascending=False)

# 엑셀 파일로 출력한다.
kor.to_excel("data/ch11/csv_to_excel1.xlsx")

# 인덱스 제외하고, 시트명을 지정한다.
kor.to_excel("data/ch11/csv_to_excel2.xlsx", index=False, sheet_name="국어로 정렬")

# 하나의 엑셀 파일에 여러 개의 시트를 출력한다.
with pd.ExcelWriter("data/ch11/csv_to_excel3.xlsx") as writer:
    df.to_excel(writer, index=False, sheet_name="원본 데이터")
    kor.to_excel(writer, index=False, sheet_name="국어로 정렬")

# 엑셀 파일을 읽어 들인다.
df = pd.read_excel("data/ch11/csv_to_excel2.xlsx")
print(df)

# 엑셀 파일에 시트가 여러개 있는 경우, 시트명을 지정해서 읽어 들인다.
df = pd.read_excel("data/ch11/csv_to_excel3.xlsx")
print(df)
df = pd.read_excel("data/ch11/csv_to_excel3.xlsx", sheet_name="국어로 정렬")
print(df)
