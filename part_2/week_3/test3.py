import numpy as np
#             0 1 2 3
x = np.array([3,4,2,1])
#   2 1 3 4 值
x.partition(3)
print("\nx.partition(3) 后:", x)