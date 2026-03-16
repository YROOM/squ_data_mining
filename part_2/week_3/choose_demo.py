import numpy as np
# x = np.arange(0,20,2) #一维数组
# print(x)
#
# print(x.take([0, 2, 4]))
# print(x.take([
#     [2, 5],
#     [3, 6]
# ]))


[0,5,10,15, 20, 25, 30, 35, 40, 45, 50, 55,60, 65, 70, 75]
y=np.array([
    [0,5,10,15],
    [20, 25, 30, 35]
    [40, 45, 50, 55],
    [60, 65, 70, 75]
])
print(y.take([
    [1, 2],
    [2, 3]
]))







#
#
#
# print(x.take([
#     [2, 5],
#     [3, 6]
# ]))
#
#

#
# print(y.take([
#     [1, 2],
#     [2, 3]
# ]))
#
# # 0 1 2 3
# x = np.array([3, 4, 2, 1])
# # 2 1 3 4
# print(x)
# print(x.argpartition(3))
#
#
# w = np.array([1, 2, 3, 3, 3, 3, 6, 7, 9, 10, 12])
# w.searchsorted(3)