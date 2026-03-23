import  numpy as np

y = np.arange(30)
b = y>20 # bool 类型的数组
print(b)
print(y[b])