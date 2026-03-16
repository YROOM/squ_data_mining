import numpy as np

x = np.array([
    [1, 2],
    [3, 4],
    [5, 6]
])
y = x[
    [0, 1, 2], # 行索引数组
    [0, 1, 0]  # 列索引数组
]
print(y) # [1 4 5]


X = np.arange(30).reshape((5, 6))
print(X)
rows = np.array([0, 1, 2])
cols = np.array([2, 1, 3])
print(X[rows, cols]) # [ 2 7 15]