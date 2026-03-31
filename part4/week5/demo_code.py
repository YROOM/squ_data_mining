# -*- coding: utf-8 -*-
"""
第4章 pandas数据读写与可视化
教材对应内容：
4.1 读写csv文件
4.2 读取txt文件
4.3 读写Excel文件
4.4 pandas数据可视化
所有代码均来自教材，已完整整理 + 详细注释 + 可直接运行
"""

# ===================== 导入需要的库 =====================
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# ---------------- 解决matplotlib中文乱码（必须加） ----------------
plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False    # 用来正常显示负号


# ==============================================
# 4.1 pandas 读写 csv 文件
# ==============================================
print("=" * 50)
print("4.1 读写 csv 文件")
print("=" * 50)

# ---------------- 4.1.1 读取 csv 文件 ----------------
# 读取 student.csv（文件需放在代码同一目录）
# 文件内容：
# Name,Math,Physics,Chemistry
# WangLi,93,88,90
# ZhangHua,97,86,92
# LiMing,84,72,77
# ZhouBin,97,94,80
csvframe = pd.read_csv('student.csv')
print("【默认读取csv文件】")
print(csvframe)
print("数据类型：", type(csvframe))

# read_table 读取 csv（必须指定分隔符 sep=','）
print("\n【read_table 读取 csv】")
print(pd.read_table('student.csv', sep=','))

# header=[0,2]：指定多行作为列名
print("\n【header=[0,2] 多级列名】")
csvframe2 = pd.read_csv('student.csv', header=[0, 2])
print(csvframe2)

# usecols=[1,2]：只读取第2、3列
print("\n【usecols 读取指定列】")
print(pd.read_csv('student.csv', usecols=[1, 2]))

# 自定义列名
print("\n【自定义列名】")
print(pd.read_csv('student.csv', header=0, names=['name', 'maths', 'physical', 'chemistry']))

# index_col=[0,1]：指定前两列为行索引
print("\n【指定前两列为行索引】")
print(pd.read_csv('student.csv', index_col=[0, 1]))

# ---------------- 4.1.2 写入 csv 文件 ----------------
print("\n【写入 csv 文件】")
# 生成时间索引
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
df.to_csv('bbp.csv')
print("已写入：bbp.csv")

# 写入csv（不带索引、不带列名）
df.to_csv('bbp1.csv', index=False, header=False)
print("已写入：bbp1.csv")

# 写入csv（给行索引添加列名）
df.to_csv("bbp2.csv", index_label="index_label")
print("已写入：bbp2.csv")


# ==============================================
# 4.2 读取 txt 文件
# ==============================================
print("\n" + "=" * 50)
print("4.2 读取 txt 文件")
print("=" * 50)

# 1.txt 内容：
# C  Python Java
# 1  4      5
# 3  3      4
# 4  2      3
# 2  1      1

# 直接读取（数据不整齐）
print("【直接读取txt（不整齐）】")
print(pd.read_table('1.txt'))

# sep='\s+'：匹配多个空格/制表符（数据整齐）
print("\n【正则分隔符读取（整齐）】")
print(pd.read_table('1.txt', sep='\s+', engine="python"))

# skiprows 跳过行 + nrows 读取行数
print("\n【跳过指定行 + 读取指定行数】")
print(pd.read_table('1.txt', sep='\s+', skiprows=[1, 3], nrows=2))

# 2.txt：0BEGIN11NEXT22A32  提取数字
# sep='\D+'：匹配非数字字符
print("\n【从混合文本提取数字】")
print(pd.read_table('2.txt', sep='\D+', header=None, engine='python'))


# ==============================================
# 4.3 读写 Excel 文件
# 需安装：pip install openpyxl
# ==============================================
print("\n" + "=" * 50)
print("4.3 读写 Excel 文件")
print("=" * 50)

# ---------------- 4.3.1 读取 Excel ----------------
# 读取默认工作表
print("【读取默认Excel】")
excel_df = pd.read_excel('chengji.xlsx')
print(excel_df.head())

# header=None：不把第一行当作列名
print("\n【header=None】")
print(pd.read_excel('chengji.xlsx', header=None).head())

# skiprows 跳过指定行
print("\n【跳过行】")
print(pd.read_excel('chengji.xlsx', skiprows=[1, 2, 3, 5]).head())

# skipfooter 跳过末尾行
print("\n【跳过末尾行】")
print(pd.read_excel('chengji.xlsx', skipfooter=6))

# index_col 指定行索引
print("\n【指定ID列为行索引】")
print(pd.read_excel('chengji.xlsx', skipfooter=5, index_col="ID").head())

# names 重命名列
print("\n【重命名列】")
print(pd.read_excel('chengji.xlsx', skipfooter=6, names=["a", "b", "c", "d", "e", "f"]))

# 读取多个工作表
print("\n【读取多个工作表】")
excel_dict = pd.read_excel('chengji.xlsx', skipfooter=6, sheet_name=[0, 1])
print("工作表0：")
print(excel_dict[0].head())
print("工作表1：")
print(excel_dict[1].head())

# ---------------- 4.3.2 写入 Excel ----------------
print("\n【写入 Excel】")
df_excel = pd.DataFrame({
    'course': ['C', 'Java', 'Python', 'Hadoop'],
    'scores': [82, 96, 92, 88],
    'grade': ['B', 'A', 'A', 'B']
})
print("写入数据：")
print(df_excel)

# 写入Excel，只输出指定列，保存到 sheet2
df_excel.to_excel(
    excel_writer='cgs.xlsx',
    sheet_name="sheet2",
    columns=["course", "grade"],
    index=False
)
print("已写入：cgs.xlsx")


# ==============================================
# 4.4 pandas 数据可视化
# ==============================================
print("\n" + "=" * 50)
print("4.4 数据可视化（所有图表）")
print("=" * 50)

# 读取Excel数据（用于绘图）
studf = pd.read_excel('chengji.xlsx', sheet_name=1, index_col="ID")
print("绘图数据源：")
print(studf.head())

# ---------------- 4.4.1 折线图 ----------------
print("\n【绘制折线图】")
ax = studf.plot(
    kind='line',
    figsize=[5, 5],
    legend=True,
    title='scores',
    style=['-', '--', '-.']
)
ax.set_ylabel('fenshu')
plt.show()

# 只绘制两列
studf[['C', 'Java']].plot(
    kind='line',
    figsize=[5, 5],
    legend=True,
    title='scores',
    style=['-', '--']
)
plt.show()

# ---------------- 4.4.2 条形图 ----------------
print("\n【绘制条形图】")
studf.plot(
    kind='bar',
    figsize=(10, 6),
    fontsize=15,
    rot=45
)
plt.xlabel('StuID', fontsize=15)
plt.ylabel('scores', fontsize=15)
plt.title('Bar', fontsize=15)
plt.show()

# 水平条形图
studf.plot(
    kind='barh',
    figsize=(10, 6),
    fontsize=15
)
plt.xlabel('scores', fontsize=15)
plt.ylabel('StuID', fontsize=15)
plt.title('BarH', fontsize=15)
plt.show()

# 堆积条形图
studf.plot(
    kind='bar',
    stacked=True,
    figsize=(10, 6),
    fontsize=15,
    rot=45
)
plt.title('Stacked Bar', fontsize=15)
plt.show()

# ---------------- 4.4.3 直方图 ----------------
print("\n【绘制直方图】")
df_hist = pd.DataFrame({
    'name': ['LiHua', 'WangMing', 'ZhengLi', 'SunFei', 'ZhangFei'],
    'maths': [82, 85, 88, 92, 94],
    'physics': [89, 75, 83, 82, 86],
    'chemistry': [86, 87, 80, 82, 92]
})
df_hist.plot(
    kind='hist',
    figsize=(10, 6),
    bins=10,
    alpha=0.8,
    stacked=True,
    color=['coral', 'darkslateblue', 'mediumseagreen']
)
plt.title('Histogram of score')
plt.xlabel('score')
plt.show()

# 多子图直方图
df_subhist = pd.DataFrame({
    'a': np.random.randn(1000) + 2,
    'b': np.random.randn(1000) + 1,
    'c': np.random.randn(1000),
    'd': np.random.randn(1000) - 1
})
df_subhist.hist(bins=20, figsize=(10, 8))
plt.show()

# ---------------- 4.4.4 饼图 ----------------
print("\n【绘制饼图】")
studf['C'].plot(
    kind='pie',
    figsize=(5, 6),
    autopct='%1.f%%',
    startangle=90,
    shadow=True
)
plt.title('C语言成绩占比')
plt.show()

# ---------------- 4.4.5 箱线图 ----------------
print("\n【绘制箱线图】")
df_subhist.plot(kind="box", figsize=(10, 6))
plt.title('箱线图')
plt.show()

# ---------------- 4.4.6 区域图 ----------------
print("\n【绘制区域图】")
fig, (ax1, ax2) = plt.subplots(2, figsize=(8, 8))
studf[['C', 'Java']].plot(kind='area', stacked=False, ax=ax1, title='非堆积')
studf[['C', 'Java']].plot(kind='area', ax=ax2, title='堆积')
plt.tight_layout()
plt.show()

# ---------------- 4.4.7 散点图 ----------------
print("\n【绘制散点图】")
df_scatter = pd.DataFrame(np.random.rand(300, 2), columns=['A', 'B'])
df_scatter.plot(kind='scatter', x='A', y='B', figsize=(8, 6), title='散点图')
plt.show()

print("\n✅ 第4章所有代码运行完成！")