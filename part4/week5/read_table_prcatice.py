import pandas as pd


# 相对路径 vs 绝对路径
# 文件读取 filePath

# 相对路径
# 正则表达式
value  = pd.read_table('../1.txt',sep='\s+', engine="python")
# print(pd.read_table('2.txt'))

# 绝对路径
#print(pd.read_table('C:\\Users\\24138\\Desktop\\demo.txt'))




print(value)