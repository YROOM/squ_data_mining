# -*- coding: utf-8 -*-
"""
Pandas 核心操作：Series & DataFrame
包含 Series/DataFrame 的创建、数据读写、修改、删除等全部核心操作
"""

# ====================== 第一步：导入依赖库 ======================
import numpy as np
import pandas as pd
import math
#
# print("="*50)
# print("Pandas 核心操作演示开始")
# print("="*50)
#
# # ====================== 3.1 Series 结构 ======================
# print("\n" + "="*30 + " 3.1 Series 结构 " + "="*30)
#
# # --------------------- 3.1.1 创建 Series ---------------------
# print("\n--- 3.1.1 创建 Series ---")
# # 1. 用 NumPy 一维数组创建
# s1 = pd.Series(np.arange(0, 5, 2), index=['a', 'b', 'c'])
# print("1. NumPy 数组创建的 Series：")
# print(s1)
# print("s1.values:", s1.values)
# print("s1.index:", s1.index)
#
# # 2. 用标量值创建
# s2 = pd.Series(25, index=['a', 'b', 'c'])
# print("\n2. 标量值创建的 Series：")
# print(s2)
#
# # 3. 用字典创建
# dict1 = {'Alice':'2341', 'Beth':'9102','Cecil':'3258'}
# sd = pd.Series(dict1)
# print("\n3. 字典创建的 Series：")
# print(sd)
#
# # 4. 用列表创建
# s3 = pd.Series(data=[90,86,95], index=['Java','C','Python'])
# print("\n4. 列表创建的 Series：")
# print(s3)
#
# # --------------------- 3.1.2 查看和修改 Series 数据 ---------------------
# print("\n--- 3.1.2 查看和修改 Series 数据 ---")
# # 1. 通过索引查看数据
# print("通过索引 'C' 查看：", s3['C'])
# print("通过默认索引 1 查看：", s3[1])
# print("通过属性 s3.C 查看：", s3.C)
#
# # 2. 切片查看多个元素
# print("\n切片 0:2 查看：")
# print(s3[0:2])
#
# # 3. 索引列表查看多个元素
# print("\n索引列表 ['Python','C','Java'] 查看：")
# print(s3[['Python','C','Java']])
#
# # 4. 筛选条件查看数据
# print("\n筛选值 >=90 的元素：")
# print(s3[s3>=90])
#
# # 5. 修改数据
# s3['C'] = 96
# print("\n修改后 s3['C']：", s3['C'])
#
# # --------------------- 3.1.3 Series 常用属性 ---------------------
# print("\n--- 3.1.3 Series 常用属性 ---")
# print("s3.shape：", s3.shape)
# print("s3.index：", s3.index)
#
# # 为 Series 和索引命名
# s3.name = 'grade'
# s3.index.name = '科目'
# print("\ns3.name：", s3.name)
# print("s3.index.name：", s3.index.name)
#
# # --------------------- 3.1.4 Series 常用方法 ---------------------
# print("\n--- 3.1.4 Series 常用方法 ---")
# # 创建含空值的 Series
# s = pd.Series(data=[90,86,np.NaN,95], index=['Java','C','Scala', 'Python'])
# print("原始 Series s：")
# print(s)
#
# # 数值计算方法
# print("\ns.sum()：", s.sum())
# print("s.var()：", s.var())
#
# # 缺失值/元素处理
# print("\ns.drop('Scala')：")
# print(s.drop('Scala'))
# print("\ns.dropna()：")
# print(s.dropna())
# print("\ns.fillna(value=100)：")
# print(s.fillna(value=100))
# print("\ns.mask(s>88,99)：")
# print(s.mask(s>88,99))
#
# # 数据转换
# print("\ns.apply(math.sqrt)：")
# print(s.apply(math.sqrt))
#
# # 排序
# print("\ns.sort_values()：")
# print(s.sort_values())
# print("\ns.sort_index()：")
# print(s.sort_index())
# print("\ns.nlargest(2)：")
# print(s.nlargest(2))
#
# # 重复值处理
# ser3 = pd.Series(data=['apple', 'banana', 'apple', 'orange', 'apple', 'orange', 'orange'])
# print("\nser3.value_counts()：")
# print(ser3.value_counts())
# print("ser3.unique()：", ser3.unique())
# print("\nser3.duplicated()：")
# print(ser3.duplicated())
# print("\nser3.drop_duplicates()：")
# print(ser3.drop_duplicates())
# print("\nser3.map({'apple':'Apple','orange':'Orange'})：")
# print(ser3.map({'apple':'Apple','orange':'Orange'}))
#
# # --------------------- 3.1.5 Series 运算 ---------------------
# print("\n--- 3.1.5 Series 运算 ---")
# # 1. 算术运算
# print("s3 + 2：")
# print(s3 + 2)
#
# # 2. Series 间运算
# s5 = pd.Series([10,20], index=['c','d'])
# s6 = pd.Series([2,4,6,8], index=['a','b','c','d'])
# print("\ns5 + s6：")
# print(s5 + s6)
#
# # ====================== 3.2 DataFrame 结构 ======================
# print("\n" + "="*30 + " 3.2 DataFrame 结构 " + "="*30)
#
# # --------------------- 3.2.1 创建 DataFrame ---------------------
# print("\n--- 3.2.1 创建 DataFrame ---")
# # 1. 使用值为列表的字典创建
# data = {'C':[86,90,87,95],'Python':[92,89,89,96],'DataMining': [90,91,89,86]}
# studentDF = pd.DataFrame(data, index=['LiQian','WangLi','YangXue', 'LiuTao'])
# print("1. 列表字典创建的 studentDF：")
# print(studentDF)
#
# studentDF1 = pd.DataFrame(data, columns=['C','DataMining'])
# print("\n指定列的 studentDF1：")
# print(studentDF1)

# 2. 使用嵌套列表创建
# studentDF2 = pd.DataFrame([[78,82,93],[85,86,97],[90,92,81]],
#                           ['ZhangSan','LiHua','WangQiang'],
#                           ['Python','Java','C'])
# print("\n2. 嵌套列表创建的 studentDF2：")
# print(studentDF2)

# studentDF3 = pd.DataFrame([[78,82,93],[85,86,97],[90,92,81]])
# print("\n默认索引的 studentDF3：")
# print(studentDF3)
#
# # 3. 使用字典的字典创建
# data_dict = {
#     "name":{'one':"Jack",'two':"Mary",'three':"John",'four':"Alice"},
#     "age":{'one':10,'two':20,'three':30,'four':40},
#     "weight":{'one':30,'two':40,'three':50,'four':65}
# }
# df2 = pd.DataFrame(data_dict)
# print("\n3. 字典的字典创建的 df2：")
# print(df2)
#
# # 4. 使用字典列表创建
# data2 = [{'Name':'李华','Age':18},{'Name':'李强','Age':19},{'Name':'李涛','Age':20}]
# df5 = pd.DataFrame(data2, index=['ID1','ID2','ID3'])
# print("\n4. 字典列表创建的 df5：")
# print(df5)
#
# # --------------------- 3.2.2 DataFrame 常用属性 ---------------------
# print("\n--- 3.2.2 DataFrame 常用属性 ---")
# print("studentDF.values：")
# print(studentDF.values)
# print("\nstudentDF['Python']：")
# print(studentDF['Python'])
# print("\nstudentDF.Python：")
# print(studentDF.Python)
# print("\nstudentDF.loc['YangXue']：")
# print(studentDF.loc['YangXue'])
# print("\nstudentDF.loc[['YangXue','LiuTao']]：")
# print(studentDF.loc[['YangXue','LiuTao']])
# print("\nstudentDF.iloc[0:2,:2]：")
# print(studentDF.iloc[0:2,:2])
#
# # ====================== 3.3 读取、修改和删除 DataFrame 数据 ======================
# print("\n" + "="*30 + " 3.3 读写改删 DataFrame " + "="*30)
#
# # --------------------- 3.3.1 读取 DataFrame 数据 ---------------------
# print("\n--- 3.3.1 读取 DataFrame 数据 ---")
# data_read = {
#     "name":["Jack","Mary","John","Alice"],
#     "age":[10,20,30,40],
#     "weight":[30,40,55,65]
# }
# df = pd.DataFrame(data_read)
# print("原始 df：")
# print(df)
#
# print("\ndf['age'][1]：", df['age'][1])
# print("\ndf[df.weight>35]（weight>35 的行）：")
# print(df[df.weight>35])
# print("\ndf[df>35]（值>35 的元素）：")
# print(df[df>35])
#
# # --------------------- 3.3.2 修改 DataFrame 数据 ---------------------
# print("\n--- 3.3.2 修改 DataFrame 数据 ---")
# # 命名行列索引
# df.index.name = 'id'
# df.columns.name = 'item'
# print("命名行列后的 df：")
# print(df)
#
# # 添加新列
# df['new'] = 10
# print("\n添加 new 列后的 df：")
# print(df)
#
# # 更新列值
# df['new'] = [11,12,13,14]
# print("\n更新 new 列后的 df：")
# print(df)
#
# # 修改单个元素
# df['weight'][0] = 25
# print("\n修改 weight[0] 后的 df：")
# print(df)
#
# # 添加新行
# df1 = pd.DataFrame([[1, 2], [3, 4]], columns=['a','b'])
# df2_temp = pd.DataFrame([[5, 6], [7, 8]], columns=['a','b'])
# df3 = df1._append(df2_temp)  # 兼容新版 pandas（append 已弃用）
# print("\ndf1 添加 df2_temp 后的 df3：")
# print(df3)
#
# # --------------------- 3.3.3 删除 DataFrame 数据 ---------------------
# print("\n--- 3.3.3 删除 DataFrame 数据 ---")
# # 重置 df_del 避免前面修改影响
# df_del = pd.DataFrame({
#     "name":["Jack","Mary","John","Alice"],
#     "age":[10,20,30,40],
#     "weight":[30,40,55,65]
# })
# print("原始 df_del：")
# print(df_del)
#
# # 删除行
# print("\n删除行索引 0：")
# print(df_del.drop(labels=0, axis=0))
# print("\n删除行索引 0、1：")
# print(df_del.drop(index=[0,1]))
# print("\n删除 age=40 的行：")
# print(df_del.drop(df_del[df_del['age']==40].index))
#
# # 删除列
# print("\n删除 age 列（drop(columns)）：")
# print(df_del.drop(columns='age'))
# del df_del['age']
# print("\ndel 删除 age 列后：")
# print(df_del)
#
# # ====================== 3.4 检查 DataFrame 是否包含指定值 ======================
# print("\n" + "="*30 + " 3.4 检查指定值 " + "="*30)
# df_check = pd.DataFrame({
#     "name":["Jack","Mary","John","Alice"],
#     "age":[10,20,30,40],
#     "weight":[30,40,55,65]
# })
# print("原始 df_check：")
# print(df_check)
#
# print("\ndf_check.isin(['Jack',30])：")
# print(df_check.isin(['Jack',30]))
# print("\ndf_check[df_check.isin(['Jack',30])]：")
# print(df_check[df_check.isin(['Jack',30])])
#
# print("\ndf_check['name'].isin(['Jack','John'])：")
# print(df_check['name'].isin(['Jack','John']))
# print("\n筛选 name 为 Jack/John 的行：")
# print(df_check[df_check['name'].isin(['Jack','John'])])
#
# # 取反筛选
# filt = ~df_check['name'].isin(['Jack','John'])
# print("\n筛选 name 非 Jack/John 的行：")
# print(df_check[filt])
#
# print("\n" + "="*50)
# print("Pandas 核心操作演示结束")
# print("="*50)