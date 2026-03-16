import numpy as np

x = np.array([1,3,2,3,3,3,6,7,8,9])
print(x.searchsorted(3,side='left'))
