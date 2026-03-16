import numpy as np
x = np.arange(10,1,-1) # [10  9  8  7  6  5  4  3  2]
print(x)

y = x[[2, 2, 1, 6]] # [8 8 9 4]
print(y)
y[0]=111
print(x) # [10  9  8  7  6  5  4  3  2]
print(y) # [111   8   9   4]

s = x[2]
print(s)
s[0]=123456
print(x)
print(s)


