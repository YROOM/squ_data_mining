import numpy as np

# Python列表切片：拷贝
lst = [1,2,3,4,5]
lst_slice = lst[1:4]
lst_slice[0] = 0
print(lst)  # [1,2,3,4,5]，原列表不变

# NumPy数组切片：视图
arr = np.array([1,2,3,4,5])
arr_slice = arr[1:4]

arr_slice[0] = 0
print(arr)  # [1,0,3,4,5]，原数组被修改


arr_slice_2 = arr[1:4].copy()
print("-------------0000")
print(arr_slice_2)
arr_slice_2[0] = 789
print(arr_slice_2)

print("-------------")
print(arr) # [1,2,3,4,5],原数组未被修改

arr[2]=456
print(arr_slice_2)