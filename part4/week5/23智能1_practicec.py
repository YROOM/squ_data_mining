import pandas as pd

# csvframe= pd.read_csv('student.csv')
#
# print(csvframe.head(4))

date_range = pd.date_range(start="20180801", periods=4)
# 创建DataFrame
df = pd.DataFrame({
    'book': [12, 13, 15, 22],
    'box': [3, 8, 13, 18],
    'pen': [5, 7, 12, 15]
}, index=date_range)
print("原始数据：")
print(df)

# 写入csv（带索引和列名）
# df.to_csv('bbp.csv')
# print("已写入：bbp.csv")