import numpy as np

a = np.array([10, 20, 30])
b = np.array([1.5, 2.5, 3.5])
c = np.array([1, 2, 3], dtype=complex)

print("Integer Array:", a)
print("Data Type:", a.dtype)

print("Float Array:", b)
print("Data Type:", b.dtype)

print("Complex Array:", c)
print("Data Type:", c.dtype)

print("1D Array:", np.array([1, 2, 3]))
print("2D Array:", np.array([[1, 2], [3, 4]]))
print("3D Array:", np.array([[[1, 2], [3, 4]]]))