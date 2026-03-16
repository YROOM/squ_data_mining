# ======================================
# NumPy 核心知识点全量代码（超详细注释版）
# 颜色标记规则：
# 🟢 核心函数/语法（必须掌握）
# 🔵 原理说明（理解底层逻辑）
# 🟡 应用场景（数据挖掘实际用途）
# 🔴 注意事项（易出错点）
# ======================================

# 🟢 1. 导入必要库
import numpy as np  # 核心库，约定简写为np
import matplotlib.pyplot as plt  # 可视化库（随机分布用）

# 🔵 固定随机种子：保证每次运行随机数结果一致，便于课堂演示
# 原理：随机数生成器的初始值固定，后续随机操作可复现
np.random.seed(123)  

# ======================================
# 🟢 2.2 数组元素的索引、切片和选择（核心基础）
# 🔵 核心原理：NumPy数组索引从0开始，支持单索引、切片、列表索引、布尔索引
# 🟡 应用场景：数据筛选、提取指定位置元素、数据子集获取
# ======================================
print("===== 2.2 数组元素的索引、切片和选择 =====")

# 2.2.1 索引和切片（最常用的元素访问方式）
print("\n--- 2.2.1 索引和切片 ---")
# 🟢 1. 单个元素索引（一维数组）
x = np.arange(10)  # 🟢 生成0-9的一维数组，数据挖掘常用
print("原始一维数组 x:", x)

# 🟢 正索引：从数组开头开始计数，索引值=位置-1
print("x[5] (第6个元素):", x[5])  
# 🟢 负索引：从数组末尾开始计数，-1表示最后一个元素
# 🟡 应用场景：快速获取数组末尾的元素，无需计算数组长度
print("x[-2] (倒数第2个元素):", x[-2])  

# 🟢 基础切片：格式为[起始索引:终止索引]，左闭右开
# 🔵 原理：切片返回的是原数组的视图（不是拷贝），修改切片会影响原数组
print("x[2:6] (切片 2-5):", x[2:6])  
# 🟢 负索引切片
print("x[:-7] (前3个元素):", x[:-7])  
# 🟢 带步长切片：格式为[起始:终止:步长]
# 🟡 应用场景：隔行/隔列取数、数据降采样
print("x[0:10:2] (步长2):", x[0:10:2])  

# 🟢 改变数组形状：shape属性直接修改维度
# 🔵 原理：数组的shape只是维度描述，底层数据存储顺序不变
x.shape = (2, 5)  # 一维转2行5列
print("变形为2×5的x:\n", x)

# 🟢 多维数组索引：(行索引, 列索引)
print("x[(1,3)] (第2行第4列):", x[(1,3)])  

# 🟢 2. 列表索引数组（高级索引：返回拷贝）
# 🔵 原理：列表索引会生成新数组，修改不影响原数组
x = np.arange(10,1,-1)  # 生成10到2的递减数组
print("\n列表索引原数组 x:", x)
print("x[[2,2,1,6]] (重复索引):", x[[2, 2, 1, 6]])  # 允许重复索引

# 🟢 混合索引：行切片+列索引 / 行列表+列切片
y = np.arange(35).reshape(5,7)  # 🟢 生成5行7列数组
print("5×7数组 y:\n", y)
print("y[1:4, 2] (1-3行第2列):", y[1:4, 2])
print("y[[0,2,4], 1:3] (指定行+切片列):\n", y[[0,2,4], 1:3])

# 🟢 3. 布尔值索引数组（条件筛选，最常用）
# 🔵 原理：先生成布尔数组，再提取True位置的元素
y = np.arange(30)
b = y>20  # 生成布尔条件
print("\n布尔索引条件 y>20:", b)
# 🟡 应用场景：筛选成绩>60、销售额>1000等条件数据
print("y[b] (大于20的元素):", y[b])

# 2.2.2 选择数组元素的方法（专用函数）
print("\n--- 2.2.2 选择数组元素的方法 ---")
# 🟢 1. ndarray.take()：按索引提取元素
x = np.arange(0,20,2)
print("take原数组 x:", x)
print("x.take([0,2,4]):", x.take([0,2,4]))
print("x.take([[2,5],[3,6]]):\n", x.take([[2,5],[3,6]]))

# 🟢 2. ndarray.put()：按索引修改元素（原地修改）
x = np.arange(0,20,2)
x.put([0,1], [1,3])
print("\nx.put([0,1],[1,3]) 后:", x)

# 🟢 3. ndarray.searchsorted()：查找插入位置（有序数组）
# 🔵 原理：二分查找，效率远高于遍历
w = np.array([1,2,3,3,3,3,6,7,9,10,12])  # 有序数组
print("\nsearchsorted原数组 w:", w)
print("w.searchsorted(3):", w.searchsorted(3))
print("w.searchsorted(3, side='right'):", w.searchsorted(3, side='right'))

# 🟢 4. ndarray.partition()：快速分区排序
# 🟡 应用场景：快速找中位数、topN问题
x = np.array([3,4,2,1])
x.partition(3)
print("\nx.partition(3) 后:", x)

# 🟢 5. ndarray.argpartition()：返回分区索引
x = np.array([3,4,2,1])
arg_idx = x.argpartition(2)
print("x.argpartition(2):", arg_idx)
print("x[arg_idx]:", x[arg_idx])

# 🟢 6. ndarray.diagonal()：提取对角线元素
k = np.array([[0,1,2,3],[4,5,6,7],[8,9,10,11]])
print("\n对角线原数组 k:\n", k)
print("k.diagonal():", k.diagonal())

# 🟢 7. ndarray.item()：提取Python标量
a = np.arange(9).reshape(3,3)
print("\nitem原数组 a:\n", a)
print("a.item(3):", a.item(3))
print("a.item((2,2)):", a.item((2,2)))

# 🟢 8. ndarray.itemset()：修改单个元素
a.itemset(3, 33)
a.itemset((1,2), 12)
print("a.itemset后:\n", a)

# 🟢 9. ndarray.tolist()：转为Python列表
print("\na.tolist():", a.tolist())

# 🟢 10. ndarray.copy()：深拷贝（独立新数组）
# 🔴 注意：区别于视图，修改新数组不影响原数组
b = a.copy()
b[0,0] = 10
print("\na.copy() 后修改b[0,0]:", b[0,0], "a[0,0]:", a[0,0])

# 🟢 11. ndarray.fill()：填充数组
b.fill(6)
print("b.fill(6) 后:\n", b)

# 2.2.3 数组形状变换
print("\n--- 2.2.3 数组形状变换 ---")
# 🟢 1. reshape()：返回新形状视图
# 🔴 注意：修改视图会影响原数组
x = np.arange(0,12)
y = x.reshape((3,4))
y[0][0] = 20
print("reshape原数组 x:", x)

# 🟢 2. resize()：原地修改形状（无返回值）
x.resize((3,4))
print("x.resize(3,4) 后:\n", x)

# 🟢 3. transpose()：数组转置（行列互换）
x = np.arange(4).reshape(2,2)
print("\n转置原数组 x:\n", x)
print("x.transpose():\n", x.transpose())

# 🟢 4. flatten()：展平数组（返回拷贝）
x = np.arange(0,12).reshape(3,4)
y = x.flatten()
y[0] = 300
print("\nflatten原数组 x:\n", x)

# 🟢 5. ravel()：展平数组（返回视图）
# 🔴 注意：修改会影响原数组，比flatten高效
x = np.array([[1,2],[3,4]])
print("\nravel原数组 x:\n", x)
print("x.ravel() (行优先):", x.ravel())
print("x.ravel('F') (列优先):", x.ravel('F'))

# ======================================
# 🟢 2.3 随机数数组（数据挖掘测试数据生成）
# 🔵 核心原理：基于伪随机数生成器，seed固定则结果可复现
# 🟡 应用场景：模拟数据、随机采样、模型初始化
# ======================================
print("\n===== 2.3 随机数数组 =====")

# 2.3.1 简单随机数
print("\n--- 2.3.1 简单随机数 ---")
# 🟢 1. rand()：[0,1)均匀分布
print("random.rand():", np.random.rand())
print("random.rand(5):", np.random.rand(5))
print("random.rand(2,3):\n", np.random.rand(2,3))

# 🟢 2. randn()：标准正态分布（均值0，方差1）
# 🟡 应用场景：噪声添加、模型误差模拟
print("\nrandom.randn():", np.random.randn())
print("random.randn(2,3):\n", np.random.randn(2,3))

# 🟢 3. randint()：整数随机数
print("\nrandom.randint(3, size=5):", np.random.randint(3, size=5))
print("random.randint(2,6,(2,3)):\n", np.random.randint(2,6,(2,3)))

# 🟢 4. choice()：随机选择元素
# 🟡 应用场景：随机抽样、数据集划分
print("\nrandom.choice(3):", np.random.choice(3))
print("random.choice(['a','b','c','f'], (2,3)):\n", np.random.choice(['a','b','c','f'], (2,3)))

# 2.3.2 随机分布
print("\n--- 2.3.2 随机分布 ---")
# 🟢 1. binomial()：二项分布
# 🟡 应用场景：模拟抛硬币、产品合格率
n, p = 10, 0.6
print("binomial(10,0.6,size=20):", np.random.binomial(n,p,size=20))

# 🟢 2. normal()：正态分布
mu, sigma = 0, 1
s = np.random.normal(loc=mu, scale=sigma, size=1000)
# 🔵 可视化（可选运行）
# count, bins, patches = plt.hist(s, 30, density=True)
# plt.plot(bins, 1/(sigma * np.sqrt(2 * np.pi)) * np.exp(-(bins - mu)**2/(2 * sigma**2)), 'r-', linewidth=2)
# plt.title('正态分布直方图')
# plt.show()

# 🟢 3. poisson()：泊松分布
# 🟡 应用场景：模拟电话呼入、故障发生次数
s = np.random.poisson(100, 10000)

# 2.3.3 随机排列
print("\n--- 2.3.3 随机排列 ---")
# 🟢 1. shuffle()：原地打乱
arr = np.arange(10)
np.random.shuffle(arr)
print("shuffle(arr):", arr)

# 🟢 2. permutation()：返回新数组（不修改原数组）
print("\npermutation(10):", np.random.permutation(10))

# 2.3.4 随机数生成器
print("\n--- 2.3.4 随机数生成器 ---")
# 🔵 无参数seed（每次不同）
print("无参数seed:")
for i in range(2):
    np.random.seed()
    perm = np.random.permutation(5)
    print(perm)

# 🔵 固定seed（每次相同）
print("\n固定seed=10:")
for i in range(2):
    np.random.seed(10)
    perm = np.random.permutation(5)
    print(perm)

# ======================================
# 🟢 2.4 数组的运算（NumPy核心优势：向量化）
# 🔵 核心原理：C语言层面执行，比Python循环快10-100倍
# 🟡 应用场景：数据批量计算、数值分析、矩阵运算
# ======================================
print("\n===== 2.4 数组的运算 =====")

# 2.4.1 算术运算与函数运算
print("\n--- 2.4.1 算术运算与函数运算 ---")
a = np.array([[1,2,3],[4,5,6]])
b = np.array([[1,2,3],[4,5,6]])
print("原数组 a:\n", a)
# 🟢 标量运算（广播机制）
print("a+6:\n", a+6)
print("a*2:\n", a*2)

# 🟢 数组间运算（元素级）
# 🔴 注意：*是元素乘，不是矩阵乘！
print("a+b:\n", a+b)
print("a*b:\n", a*b)

# 🟢 一元函数
print("\nsqrt(a):\n", np.sqrt(a))
print("square(a):\n", np.square(a))

# 🟢 二元函数
print("\nadd(a,b):\n", np.add(a,b))
print("equal(a,b):\n", np.equal(a,b))

# 2.4.2 筛选
print("\n--- 2.4.2 筛选 ---")
a = np.array([[1,2,3],[4,5,6],[7,8,9]])
print("原数组 a:\n", a)
print("a>3:\n", a>3)
print("a[a>3]:", a[a>3])

# 🟢 np.where()：条件筛选
print("\nnp.where(a<5,-1,1):\n", np.where(a<5,-1,1))
print("np.where(a<5):", np.where(a<5))

# 2.4.2 统计计算
print("\n--- 2.4.2 统计计算 ---")
a = np.array([[2,3,4,9],[8,7,6,5],[4,3,5,8]])
print("统计原数组 a:\n", a)
print("a.max():", a.max())  # 全局最大值
print("a.max(axis=1):", a.max(axis=1))  # 每行最大值
print("a.max(axis=0):", a.max(axis=0))  # 每列最大值

# 🟢 argmax()：返回最大值索引
print("\na.argmax(axis=0):", a.argmax(axis=0))

# 🟢 ptp()：峰峰值（最大值-最小值）
print("\na.ptp(axis=1):", a.ptp(axis=1))

# 🟢 clip()：限制元素范围（异常值处理）
print("\na.clip(5,8):\n", a.clip(5,8))

# 🟢 sum/cumsum：求和/累计和
print("\na.sum(axis=1):", a.sum(axis=1))
print("a.cumsum(axis=1):\n", a.cumsum(axis=1))

# 2.4.3 线性代数运算（数据挖掘核心）
print("\n--- 2.4.3 线性代数运算 ---")
# 🟢 矩阵乘法（dot函数）
A = np.arange(1,10).reshape(3,3)
B = np.ones((3,3), dtype=int)
print("矩阵A:\n", A)
print("矩阵B:\n", B)
print("np.dot(A,B):\n", np.dot(A,B))

# 🟢 逆矩阵（仅方阵可逆）
A = np.array([[1,2,3],[1,0,-1],[0,1,1]])
B = np.linalg.inv(A)
print("\nA的逆矩阵:\n", B)

# 🟢 解线性方程组
A = np.array([[2,3,-5],[1,-2,1],[3,1,3]])
b = np.array([3,0,7])
c = np.linalg.solve(A,b)
print("\n线性方程组解:", c)

# 🟢 特征值和特征向量（PCA核心）
A = np.array([[1,2,2],[2,1,2],[2,2,1]])
eigvals, eigvecs = np.linalg.eig(A)
print("\n特征值:", eigvals)
print("特征向量:\n", eigvecs)

# 🟢 奇异值分解（SVD，推荐系统核心）
A = np.array([[0,1],[1,1],[1,0]])
U, Sigma, V = np.linalg.svd(A)
print("\nSVD分解 U:\n", U)
print("Sigma:", Sigma)

# 2.4.4 排序
print("\n--- 2.4.4 排序 ---")
# 🟢 sort()：原地排序
y = np.array([1,3,4,9,8,7,6,5,3,10,2])
y.sort()
print("y.sort() 后:", y)

# 🟢 argsort()：返回排序索引
z = np.array([1,3,4,9,8,7,6,5,3,10,2])
print("\nz.argsort():", z.argsort())

# 2.4.5 数组拼接与切分
print("\n--- 2.4.5 数组拼接与切分 ---")
# 🟢 vstack（垂直拼接）、hstack（水平拼接）
a = np.array([1,2,3])
b = np.array([2,3,4])
print("vstack(a,b):\n", np.vstack((a,b)))

# 🟢 hsplit（水平切分）、vsplit（垂直切分）
a = np.arange(16).reshape(4,4)
x,y,z = np.hsplit(a,[2,3])
print("\nhsplit(a,[2,3]) x:\n", x)
print("vsplit(a,2):\n", np.vsplit(a,2))

# ======================================
# 🟢 2.5 读写数据文件（数据持久化）
# 🔵 核心：npy/npz效率最高，txt/csv兼容性好
# ======================================
print("\n===== 2.5 读写数据文件 =====")

# 2.5.1 读写二进制文件（npy/npz）
print("\n--- 2.5.1 读写二进制文件 ---")
A = np.arange(16).reshape(2,8)
np.save("A.npy", A)  # 保存单个数组
B = np.load("A.npy")
print("读取A.npy:\n", B)

# 保存多个数组（npz）
A = np.arange(16).reshape(2,8)
B = np.arange(15).reshape(3,5)
np.savez("C.npz", A, B)
D = np.load("C.npz")
print("\n读取C.npz arr_0:\n", D['arr_0'])

# 2.5.2 读写文本文件（txt）
print("\n--- 2.5.2 读写文本文件 ---")
a = np.arange(0,10).reshape(2,5)
np.savetxt("a.txt", a)
print("读取a.txt:\n", np.loadtxt("a.txt"))

# 自定义格式（浮点型、逗号分隔）
b = np.arange(0,10,0.5).reshape(2,10)
np.savetxt("b.txt", b, fmt="%f", delimiter=",")
print("\n读取b.txt:\n", np.loadtxt("b.txt", dtype="f", delimiter=","))

print("\n=== 所有代码执行完成 ===")