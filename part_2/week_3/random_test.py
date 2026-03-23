from numpy import random
import numpy as np

# print("random.rand():", random.rand())
# print("random.rand(5):", random.rand(5))
# print("random.rand(2,3):\n", random.rand(2,3))

for i in range(5):
    np.random.seed(10) # 设置随机数种子
    perm = np.random.permutation(10)
    print(perm)





