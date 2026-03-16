# ======================================
# NumPy 核心知识点全量代码（超详细注释版）
# 适用：《Python数据挖掘技术及应用（第2版）》第二章教学
# 核心：注释覆盖"语法+原理+应用场景"，适配新手理解
# ======================================

# 1. 导入必要库：numpy是核心，matplotlib用于随机分布可视化
import numpy as np
import matplotlib.pyplot as plt

# 固定随机种子（关键！）：保证每次运行随机数结果一致，便于课堂演示
# 原理：随机数生成器的初始值固定，后续随机操作可复现
np.random.seed(123)

# ======================================
# 2.2 数组元素的索引、切片和选择（核心基础）
# 核心原理：NumPy数组索引从0开始，支持单索引、切片、列表索引、布尔索引
# 应用场景：数据筛选、提取指定位置元素、数据子集获取
# ======================================
print("===== 2.2 数组元素的索引、切片和选择 =====")

# 2.2.1 索引和切片（最常用的元素访问方式）
print("\n--- 2.2.1 索引和切片 ---")
# 1. 单个元素索引（一维数组）
# arange(10)：生成0-9的一维数组，是NumPy创建连续整数数组的常用函数
x = np.arange(10)
print("原始一维数组 x:", x)  # 输出：[0 1 2 3 4 5 6 7 8 9]

# 正索引：从数组开头开始计数，索引值=位置-1
# 原理：数组在内存中是连续存储的，索引直接对应内存偏移量
print("x[5] (第6个元素):", x[5])          # 输出5，对应第6个元素

# 负索引：从数组末尾开始计数，-1表示最后一个元素
# 应用场景：快速获取数组末尾的元素，无需计算数组长度
print("x[-2] (倒数第2个元素):", x[-2])     # 输出8，倒数第2个元素

# 基础切片：格式为[起始索引:终止索引]，左闭右开（包含起始，不包含终止）
# 原理：切片返回的是原数组的视图（不是拷贝），修改切片会影响原数组
print("x[2:6] (切片 2-5):", x[2:6])        # 输出[2 3 4 5]，包含2不包含6

# 负索引切片：终止索引为负数时，从末尾往前数
print("x[:-7] (前3个元素):", x[:-7])       # 输出[0 1 2]，-7表示倒数第7个元素（值为3），不包含

# 带步长切片：格式为[起始:终止:步长]，步长表示每隔几个元素取一个
# 应用场景：隔行/隔列取数、数据降采样
print("x[0:10:2] (步长2):", x[0:10:2])    # 输出[0 2 4 6 8]，步长2

# 改变数组形状：shape属性直接修改数组维度，原数组内存不变
# 原理：数组的shape只是维度描述，底层数据存储顺序不变
x.shape = (2, 5)  # 把一维数组转为2行5列的二维数组
print("变形为2×5的x:\n", x)  # 输出[[0 1 2 3 4],[5 6 7 8 9]]

# 多维数组索引：格式为(行索引, 列索引)，逗号分隔不同维度
# 原理：二维数组可理解为"数组的数组"，先取行再取列
print("x[(1,3)] (第2行第4列):", x[(1,3)])  # 输出8，第2行（索引1）第4列（索引3）

# 2. 使用列表索引数组（高级索引：返回原数组的拷贝，不是视图）
# 原理：列表索引会根据列表中的索引值，逐个提取元素并生成新数组
x = np.arange(10,1,-1)  # 生成10到2的递减数组：[10 9 8 7 6 5 4 3 2]
print("\n列表索引原数组 x:", x)
# 列表[2,2,1,6]表示：取索引2、2、1、6的元素，允许重复索引
print("x[[2,2,1,6]] (重复索引):", x[[2, 2, 1, 6]])  # 输出[8 8 9 4]

# 多维数组的混合索引：行切片 + 列索引 / 行列表 + 列切片
y = np.arange(35).reshape(5,7)  # 生成0-34的5行7列数组
print("5×7数组 y:\n", y)
# 行切片（1-3行，索引1/2/3） + 列索引（第2列，索引2）
# 应用场景：提取指定行的某一列数据
print("y[1:4, 2] (1-3行第2列):", y[1:4, 2])  # 输出[9 16 23]

# 行列表（索引0/2/4） + 列切片（1-2列，索引1/2）
# 应用场景：提取不连续行的指定列数据
print("y[[0,2,4], 1:3] (指定行+切片列):\n", y[[0,2,4], 1:3])  # 输出[[1 2],[15 16],[29 30]]

# 3. 布尔值索引数组（条件筛选，最常用的数据过滤方式）
# 原理：先生成和原数组同形状的布尔数组，再提取True位置的元素
y = np.arange(30)  # 0-29的一维数组
b = y>20  # 生成布尔数组：>20的位置为True，否则为False
print("\n布尔索引条件 y>20:", b)  # 前21个False，后9个True
# 应用场景：按条件筛选数据（如筛选成绩>60的学生、销售额>1000的记录）
print("y[b] (大于20的元素):", y[b])  # 输出[21 22 23 24 25 26 27 28 29]

# 2.2.2 选择数组元素的方法（专用函数，适配复杂场景）
print("\n--- 2.2.2 选择数组元素的方法 ---")
# 1. ndarray.take()：按索引提取元素，比列表索引更灵活
# 原理：take默认将数组展平为一维后取索引，可指定axis按维度取
x = np.arange(0,20,2)  # 0,2,4,...,18
print("take原数组 x:", x)
# 基础用法：提取索引0/2/4的元素
print("x.take([0,2,4]):", x.take([0,2,4]))  # 输出[0 4 8]

# 二维索引：返回的数组形状与索引列表形状一致
print("x.take([[2,5],[3,6]]):\n", x.take([[2,5],[3,6]]))  # 输出[[4 10],[6 12]]

# 多维数组take：指定axis按行/列取
y = np.array([[0,5,10,15],[20,25,30,35],[40,45,50,55],[60,65,70,75]])
print("4×4数组 y:\n", y)
# 默认axis=None：展平为一维后取索引
print("y.take([[1,2],[2,3]]) (默认一维):\n", y.take([[1,2],[2,3]]))  # 输出[[5 10],[10 15]]

# axis=0：按行取（提取索引1/2/2/3的行）
# 原理：axis=0表示沿着行维度操作，取整行数据
print("y.take([[1,2],[2,3]], axis=0) (按行):\n", y.take([[1,2],[2,3]], axis=0))

# axis=1：按列取（提取索引1/2/2/3的列）
print("y.take([[1,2],[2,3]], axis=1) (按列):\n", y.take([[1,2],[2,3]], axis=1))

# 2. ndarray.put()：按索引修改元素值（原地修改，无返回值）
# 原理：put是take的反向操作，将指定索引位置的元素替换为新值
x = np.arange(0,20,2)
x.put([0,1], [1,3])  # 把索引0的元素改为1，索引1改为3
print("\nx.put([0,1],[1,3]) 后:", x)  # 输出[1 3 4 6 ... 18]

# 3. ndarray.searchsorted()：查找元素应插入的位置（数组需有序）
# 原理：二分查找算法，效率远高于遍历，返回第一个大于等于目标值的索引
w = np.array([1,2,3,3,3,3,6,7,9,10,12])  # 有序数组
print("\nsearchsorted原数组 w:", w)
print("w.searchsorted(3):", w.searchsorted(3))  # 输出2（第一个3的索引）
# side='right'：返回最后一个大于等于目标值的下一个索引
print("w.searchsorted(3, side='right'):", w.searchsorted(3, side='right'))  # 输出6

# 4. ndarray.partition()：快速分区排序（原地修改）
# 原理：将数组分为两部分，左边≤指定索引值，右边≥指定索引值，内部无序
# 应用场景：快速找中位数、topN问题
x = np.array([3,4,2,1])
x.partition(3)  # 以索引3为界，左边≤x[3]=1？不，是按值分区：左边≤第3小的数
print("\nx.partition(3) 后:", x)  # 输出[2 1 3 4]

# 5. ndarray.argpartition()：返回分区后的索引（不修改原数组）
# 原理：返回的是原数组元素分区后的索引，可通过索引获取分区后的数据
x = np.array([3,4,2,1])
arg_idx = x.argpartition(2)  # 按第2小的数分区
print("x.argpartition(2):", arg_idx)  # 输出[3 2 0 1]（对应值1,2,3,4）
print("x[arg_idx]:", x[arg_idx])  # 输出[1 2 3 4]

# 6. ndarray.diagonal()：提取数组对角线元素
# 原理：仅对二维数组有效，提取行索引=列索引的元素（主对角线）
k = np.array([[0,1,2,3],[4,5,6,7],[8,9,10,11]])
print("\n对角线原数组 k:\n", k)
print("k.diagonal():", k.diagonal())  # 输出[0 5 10]（主对角线）

# 7. ndarray.item()：提取单个元素并返回Python标量（不是数组元素）
# 原理：item()会拷贝元素值，脱离NumPy数组，适合单独使用元素值
a = np.arange(9).reshape(3,3)
print("\nitem原数组 a:\n", a)
print("a.item(3):", a.item(3))  # 输出3（展平后索引3的元素）
print("a.item((2,2)):", a.item((2,2)))  # 输出8（第3行第3列）

# 8. ndarray.itemset()：修改单个元素值（原地修改）
# 原理：比直接索引赋值更高效，适合批量修改单个元素
a.itemset(3, 33)  # 展平索引3改为33
a.itemset((1,2), 12)  # 第2行第3列改为12
print("a.itemset后:\n", a)  # 输出[[0 1 2],[33 4 12],[6 7 8]]

# 9. ndarray.tolist()：将数组转为Python原生列表（深拷贝）
# 原理：转换后不再受NumPy限制，可使用Python列表的所有方法
print("\na.tolist():", a.tolist())  # 输出[[0,1,2],[33,4,12],[6,7,8]]

# 10. ndarray.tostring()：将数组转为二进制字节串（底层存储格式）
# 应用场景：数据持久化、网络传输
print("a.tostring():", a.tostring())  # 输出二进制字节串

# 11. ndarray.copy()：深拷贝数组（生成独立的新数组）
# 原理：拷贝后新数组与原数组无关联，修改互不影响（区别于视图）
b = a.copy()
b[0,0] = 10  # 修改新数组
print("\na.copy() 后修改b[0,0]:", b[0,0], "a[0,0]:", a[0,0])  # 输出10 0（互不影响）

# 12. ndarray.fill()：用指定值填充整个数组（原地修改）
# 应用场景：快速初始化数组为固定值
b.fill(6)
print("b.fill(6) 后:\n", b)  # 输出全6的3×3数组

# 2.2.3 数组形状变换（核心操作，不改变数据只改变维度）
print("\n--- 2.2.3 数组形状变换 ---")
# 1. reshape()：返回新形状的视图（不是拷贝）
# 原理：reshape不改变数据存储顺序，只是改变维度描述，修改视图会影响原数组
x = np.arange(0,12)  # 0-11一维数组
y = x.reshape((3,4))  # 转为3行4列
y[0][0] = 20  # 修改视图的元素
print("reshape原数组 x:", x)  # 输出[20 1 2 ... 11]（原数组被修改）
print("y=x.reshape(3,4) 修改y[0,0]后 x:", x)

# 2. resize()：直接修改原数组的形状（无返回值）
# 区别于reshape：resize是原地修改，reshape返回新视图
x.resize((3,4))
print("x.resize(3,4) 后:\n", x)  # 输出[[20 1 2 3],[4 5 6 7],[8 9 10 11]]

# 3. transpose()：数组转置（行列互换）
# 原理：二维数组转置=交换0轴和1轴，多维数组可指定轴顺序
x = np.arange(4).reshape(2,2)
print("\n转置原数组 x:\n", x)  # 输出[[0 1],[2 3]]
print("x.transpose():\n", x.transpose())  # 输出[[0 2],[1 3]]（默认转置）
# 指定轴顺序：(1,0)表示交换0轴（行）和1轴（列）
print("x.transpose((1,0)):\n", x.transpose((1,0)))

# 4. flatten()：展平数组（返回深拷贝，修改不影响原数组）
# 应用场景：将多维数组转为一维，用于线性运算
x = np.arange(0,12).reshape(3,4)
y = x.flatten()  # 展平为一维
y[0] = 300  # 修改拷贝
print("\nflatten原数组 x:\n", x)  # 原数组不变
print("y=x.flatten() 修改y[0]后 x:\n", x)

# 5. ravel()：展平数组（返回视图，修改影响原数组）
# 区别于flatten：ravel更高效（无需拷贝），但会影响原数组
x = np.array([[1,2],[3,4]])
print("\nravel原数组 x:\n", x)
print("x.ravel() (行优先):", x.ravel())  # 输出[1 2 3 4]（C风格，行优先）
print("x.ravel('F') (列优先):", x.ravel('F'))  # 输出[1 3 2 4]（Fortran风格，列优先）

# ======================================
# 2.3 随机数数组（数据挖掘中用于生成测试数据、随机采样）
# 核心原理：基于伪随机数生成器，seed固定则结果可复现
# 应用场景：模拟数据、随机抽样、模型初始化
# ======================================
print("\n===== 2.3 随机数数组 =====")

# 2.3.1 简单随机数
print("\n--- 2.3.1 简单随机数 ---")
# 1. rand()：生成[0,1)均匀分布的随机数
# 原理：均匀分布意味着区间内每个数被选中的概率相等
print("random.rand():", np.random.rand())  # 输出0-1之间的浮点数
print("random.rand(5):", np.random.rand(5))  # 一维数组
print("random.rand(2,3):\n", np.random.rand(2,3))  # 2行3列数组

# 2. randn()：生成标准正态分布（均值0，方差1）随机数
# 应用场景：噪声添加、模型误差模拟
print("\nrandom.randn():", np.random.randn())  # 单个值
print("random.randn(2,3):\n", np.random.randn(2,3))  # 2行3列

# 3. randint()：生成指定范围的整数随机数
# 格式：randint(最小值, 最大值, 形状)，左闭右开
print("\nrandom.randint(3, size=5):", np.random.randint(3, size=5))  # 0-2的5个整数
print("random.randint(2,6,(2,3)):\n", np.random.randint(2,6,(2,3)))  # 2-5的2行3列整数

# 4. random_sample()：同rand()，只是参数格式不同
print("\nrandom.random_sample():", np.random.random_sample())
print("random.random_sample(2):", np.random.random_sample(2))
print("random.random_sample((2,3)):\n", np.random.random_sample((2,3)))

# 5. choice()：从数组/整数范围中随机选择元素
# 应用场景：随机抽样、数据集划分
print("\nrandom.choice(3):", np.random.choice(3))  # 从0-2中选1个
print("random.choice(2,2):", np.random.choice(2,2))  # 从0-1中选2个
# 从字符串数组中选，生成2行3列
print("random.choice(['a','b','c','f'], (2,3)):\n", np.random.choice(['a','b','c','f'], (2,3)))
# 指定概率：p=[0,0.5,0.5,0,0]表示1和2的概率各50%，其他为0
print("random.choice(5,3,p=[0,0.5,0.5,0,0]):", np.random.choice(5,3,p=[0,0.5,0.5,0,0]))

# 2.3.2 随机分布（模拟真实世界的数据分布）
print("\n--- 2.3.2 随机分布 ---")
# 1. binomial()：二项分布（n次独立试验，每次成功概率p）
# 应用场景：模拟抛硬币、产品合格率
n, p = 10, 0.6  # 10次试验，每次成功概率0.6
print("binomial(10,0.6,size=20):", np.random.binomial(n,p,size=20))  # 20个样本

# 2. normal()：正态分布（高斯分布）
# 应用场景：自然现象（身高、体重）、测量误差
mu, sigma = 0, 1  # 均值0，标准差1
s = np.random.normal(loc=mu, scale=sigma, size=1000)  # 1000个样本
# 绘制正态分布直方图（可选运行，取消注释即可）
# count, bins, patches = plt.hist(s, 30, density=True)  # 直方图
# # 绘制概率密度函数曲线
# plt.plot(bins, 1/(sigma * np.sqrt(2 * np.pi)) * np.exp(-(bins - mu)**2/(2 * sigma**2)), 'r-', linewidth=2)
# plt.title('正态分布直方图（均值0，标准差1）')
# plt.xlabel('值')
# plt.ylabel('概率密度')
# plt.show()

# 3. poisson()：泊松分布（单位时间内事件发生的次数）
# 应用场景：模拟电话呼入次数、故障发生次数
s = np.random.poisson(100, 10000)  # 平均100次/单位时间，10000个样本
# 绘制泊松分布直方图（可选运行）
# plt.hist(s, 100)
# plt.title('泊松分布直方图（λ=100）')
# plt.xlabel('事件发生次数')
# plt.ylabel('频次')
# plt.show()

# 2.3.3 随机排列（打乱数据顺序，用于数据集洗牌）
print("\n--- 2.3.3 随机排列 ---")
# 1. shuffle()：原地打乱数组（修改原数组）
# 原理：多维数组按第一维打乱（行打乱，列不变）
arr = np.arange(10)
np.random.shuffle(arr)
print("shuffle(arr):", arr)  # 打乱后的0-9

arr1 = np.arange(9).reshape(3,3)
np.random.shuffle(arr1)
print("shuffle(arr1) (按行打乱):\n", arr1)  # 行顺序打乱

# 2. permutation()：返回打乱后的新数组（不修改原数组）
print("\npermutation(10):", np.random.permutation(10))  # 新数组

# 2.3.4 随机数生成器（控制随机数的可复现性）
print("\n--- 2.3.4 随机数生成器 ---")
# 举例1：无参数seed（每次生成不同随机数）
print("无参数seed:")
for i in range(2):  # 简化为2次输出
    np.random.seed()  # 无参数，使用系统时间作为种子
    perm = np.random.permutation(5)  # 简化为5个元素
    print(perm)

# 举例2：固定seed=10（每次生成相同随机数）
# 核心原理：相同种子生成相同的随机数序列，便于复现实验结果
print("\n固定seed=10:")
for i in range(2):
    np.random.seed(10)  # 固定种子
    perm = np.random.permutation(5)
    print(perm)  # 两次输出相同

# ======================================
# 2.4 数组的运算（NumPy核心优势：向量化运算，无需循环）
# 核心原理：向量化运算在C语言层面执行，比Python循环快10-100倍
# 应用场景：数据批量计算、数值分析、矩阵运算
# ======================================
print("\n===== 2.4 数组的运算 =====")

# 2.4.1 算术运算与函数运算
print("\n--- 2.4.1 算术运算与函数运算 ---")
a = np.array([[1,2,3],[4,5,6]])
b = np.array([[1,2,3],[4,5,6]])
print("原数组 a:\n", a)
# 标量运算：数组与单个值运算，广播到所有元素
print("a+6:\n", a+6)  # 每个元素+6
print("a*2:\n", a*2)  # 每个元素×2

# 数组间运算：形状相同则对应元素运算（.element-wise）
# 注意：*是元素乘，不是矩阵乘！
print("a+b:\n", a+b)  # 对应元素相加
print("a*b:\n", a*b)  # 对应元素相乘
print("a/b:\n", a/b)  # 对应元素相除

# 一元函数：对每个元素单独运算
print("\n一元函数:")
print("sqrt(a):\n", np.sqrt(a))  # 平方根
print("square(a):\n", np.square(a))  # 平方

b = np.array([[1.44,4.84,9],[4,22.5,25]])
print("\nb:\n", b)
print("floor(b):\n", np.floor(b))  # 向下取整
print("ceil(b):\n", np.ceil(b))    # 向上取整
print("modf(b):\n", np.modf(b))    # 分离小数和整数部分

# 二元函数：对两个数组的对应元素运算
print("\n二元函数:")
print("add(a,b):\n", np.add(a,b))          # 相加（同a+b）
print("multiply(a,b):\n", np.multiply(a,b))# 相乘（同a*b）
print("equal(a,b):\n", np.equal(a,b))      # 判断是否相等（布尔数组）

# 2.4.2 筛选（按条件提取数据）
print("\n--- 2.4.2 筛选 ---")
a = np.array([[1,2,3],[4,5,6],[7,8,9]])
print("原数组 a:\n", a)
print("a>3:\n", a>3)  # 生成布尔数组
print("a[a>3]:", a[a>3])  # 提取True位置的元素

# where筛选：三元运算符的向量化版本
# 格式：where(条件, 满足条件的值, 不满足条件的值)
print("\nnp.where(a<5,-1,1):\n", np.where(a<5,-1,1))  # <5的改为-1，否则1
# 仅传条件：返回满足条件的元素的索引（行索引数组, 列索引数组）
print("np.where(a<5):", np.where(a<5))  # 输出(行索引, 列索引)

# 2.4.2 统计计算（数据特征分析）
print("\n--- 2.4.2 统计计算 ---")
a = np.array([[2,3,4,9],[8,7,6,5],[4,3,5,8]])
print("统计原数组 a:\n", a)
print("a.max():", a.max())  # 全局最大值
print("a.max(axis=1):", a.max(axis=1))  # 每行最大值（axis=1为行维度）
print("a.max(axis=0):", a.max(axis=0))  # 每列最大值（axis=0为列维度）

# argmax：返回最大值的索引（不是值本身）
print("\na.argmax(axis=0):", a.argmax(axis=0))  # 每列最大值的行索引
print("a.argmax(axis=1):", a.argmax(axis=1))  # 每行最大值的列索引

# ptp：峰峰值（最大值-最小值）
print("\na.ptp(axis=1):", a.ptp(axis=1))  # 每行峰峰值
print("a.ptp():", a.ptp())  # 全局峰峰值

# clip：限制元素范围（小于min设为min，大于max设为max）
# 应用场景：异常值处理（如把>100的值设为100）
print("\na.clip(5,8):\n", a.clip(5,8))  # 限制在5-8之间

# sum/cumsum：求和/累计和
print("\na.sum(axis=1):", a.sum(axis=1))  # 每行求和
print("a.cumsum(axis=1):\n", a.cumsum(axis=1))  # 每行累计和
print("a.cumprod(axis=1):\n", a.cumprod(axis=1))  # 每行累计积
print("a.all():", a.all())  # 所有元素是否为真（非0即真）

# 2.4.3 线性代数运算（数据挖掘/机器学习核心）
print("\n--- 2.4.3 线性代数运算 ---")
# 矩阵乘法（dot函数，区别于元素乘*）
# 原理：矩阵乘法规则：(m×n) × (n×p) = (m×p)
A = np.arange(1,10).reshape(3,3)
B = np.ones((3,3), dtype=int)
print("矩阵A:\n", A)
print("矩阵B:\n", B)
print("np.dot(A,B):\n", np.dot(A,B))  # 矩阵乘法

# 逆矩阵（仅方阵且可逆时存在）
# 应用场景：解线性方程组、矩阵变换
A = np.array([[1,2,3],[1,0,-1],[0,1,1]])
B = np.linalg.inv(A)  # 求逆矩阵
print("\nA的逆矩阵:\n", B)
print("A×逆矩阵:\n", np.dot(A,B))  # 结果为单位矩阵（验证）

# 解线性方程组 Ax = b
# 应用场景：多元线性回归、系统求解
A = np.array([[2,3,-5],[1,-2,1],[3,1,3]])
b = np.array([3,0,7])
c = np.linalg.solve(A,b)
print("\n线性方程组解:", c)  # 输出x/y/z的值

# 特征值和特征向量（PCA、降维的核心）
A = np.array([[1,2,2],[2,1,2],[2,2,1]])
eigvals = np.linalg.eigvals(A)  # 仅求特征值
eigvals, eigvecs = np.linalg.eig(A)  # 求特征值+特征向量
print("\n特征值:", eigvals)
print("特征向量:\n", eigvecs)

# 奇异值分解（SVD，降维、推荐系统核心）
A = np.array([[0,1],[1,1],[1,0]])
U, Sigma, V = np.linalg.svd(A)  # SVD分解
print("\nSVD分解 U:\n", U)
print("Sigma:", Sigma)  # 奇异值（一维数组）
print("V:\n", V)
print("奇异值矩阵:\n", np.diag(Sigma))  # 转为对角矩阵

# 2.4.4 排序
print("\n--- 2.4.4 排序 ---")
# sort：原地排序（修改原数组）
y = np.array([1,3,4,9,8,7,6,5,3,10,2])
y.sort()
print("y.sort() 后:", y)  # 升序排列

# 多维数组排序：默认按最后一维排序（列）
y1 = np.array([[0,15,10,5],[25,22,3,2],[55,45,59,50]])
y1.sort()
print("\ny1.sort() 后:\n", y1)  # 每行内部升序

# argsort：返回排序后的索引（不修改原数组）
# 应用场景：按某列排序整个数据集
z = np.array([1,3,4,9,8,7,6,5,3,10,2])
print("\nz.argsort():", z.argsort())  # 升序索引

# 2.4.5 数组拼接与切分（数据合并/拆分）
print("\n--- 2.4.5 数组拼接与切分 ---")
# 拼接：vstack（垂直，行增加）、hstack（水平，列增加）
a = np.array([1,2,3])
b = np.array([2,3,4])
print("vstack(a,b):\n", np.vstack((a,b)))  # 垂直拼接（2行3列）

a = np.arange(16).reshape(4,4)
b = np.arange(12).reshape(3,4)
print("\nvstack(a,b):\n", np.vstack((a,b)))  # 列数相同才能垂直拼接

a = np.array([1,2,3]).reshape(3,1)
b = np.array([4,5,6]).reshape(3,1)
print("\nhstack(a,b):\n", np.hstack((a,b)))  # 行数相同才能水平拼接

# 切分：hsplit（水平切分，按列）、vsplit（垂直切分，按行）
a = np.arange(16).reshape(4,4)
# hsplit(a,[2,3])：在列索引2和3处切分，得到3个数组
x,y,z = np.hsplit(a,[2,3])
print("\nhsplit(a,[2,3]):")
print("x:\n", x)  # 前2列
print("y:\n", y)  # 第3列
print("z:\n", z)  # 第4列

# vsplit(a,2)：垂直切分为2部分（每行2行）
print("\nvsplit(a,2):\n", np.vsplit(a,2))

# ======================================
# 2.5 读写数据文件（数据持久化）
# 核心：NumPy专用格式（npy/npz）效率最高，文本格式（txt/csv）兼容性好
# ======================================
print("\n===== 2.5 读写数据文件 =====")

# 2.5.1 读写二进制文件（npy/npz，保留数组所有信息）
print("\n--- 2.5.1 读写二进制文件 ---")
A = np.arange(16).reshape(2,8)
np.save("A.npy", A)  # 保存单个数组（自动加.npy后缀）
B = np.load("A.npy")  # 读取npy文件
print("读取A.npy:\n", B)

# 保存多个数组（npz格式，压缩存储）
A = np.arange(16).reshape(2,8)
B = np.arange(15).reshape(3,5)
np.savez("C.npz", A, B)  # 保存多个数组
D = np.load("C.npz")  # 读取npz文件
print("\n读取C.npz arr_0:\n", D['arr_0'])  # 第一个数组
print("读取C.npz arr_1:\n", D['arr_1'])  # 第二个数组

# 2.5.2 读写文本文件（txt/csv，通用格式）
print("\n--- 2.5.2 读写文本文件 ---")
a = np.arange(0,10).reshape(2,5)
np.savetxt("a.txt", a)  # 空格分隔保存
print("读取a.txt:\n", np.loadtxt("a.txt"))  # 读取文本文件

# 自定义格式：浮点型、逗号分隔
b = np.arange(0,10,0.5).reshape(2,10)
np.savetxt("b.txt", b, fmt="%f", delimiter=",")  # 浮点型，逗号分隔
# 读取时需指定分隔符和数据类型
print("\n读取b.txt:\n", np.loadtxt("b.txt", dtype="f", delimiter=","))

print("\n=== 所有代码执行完成 ===")