import pandas as pd

#
# # 绝对路径 和 相对路径
# studDf = pd.read_csv('student.csv')
# # 相对路径
#
# # 绝对路径
# studDF3 = pd.read_csv('D:\\备课\\sj\\dm_code\\part4\\test.csv')
#
# print(studDF3)


# value = pd.read_table('student.csv',sep=',')
# print(value)
# studDf = pd.read_csv('student.csv')
# value = pd.read_csv('student.csv',header=[0,2])
# print(studDf)
# print(value)
#
# print(pd.read_csv('student.csv', usecols=[1, 2]))
#
# print(pd.read_csv('student.csv', header=0, names=['name', 'math', 'physics', 'chemistry']))
#


#     0       1       2
#      Name  Math  Physics  Chemistry      0
# 0    WangLi    93       88         90    1
# 1  ZhangHua    97       86         92    2
# 2    LiMing    84       72         77    3
# 3   ZhouBin    97       94         80    4
# value = pd.read_excel('chengji.xlsx',sheet_name=[0,1])
# print(value)
df=pd.DataFrame({'course':['C','Java','Python','Hadoop'],
                 'scores':[82,96,92,88],
                 'grade':['B','A','A','B']})
df.to_excel(excel_writer='chengji.xlsx',sheet_name='Sheet2',columns=['course','grade'])














