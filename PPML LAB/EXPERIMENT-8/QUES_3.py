import numpy as np

arr = np.array([[10, 20, 30], [40, 50, 60]])

print("Array:", arr)
print("Number of Dimensions:", arr.ndim)
print("Shape:", arr.shape)
print("Size:", arr.size)
print("Data Type:", arr.dtype)
print("Item Size:", arr.itemsize)
print("Total Bytes:", arr.nbytes)

print("Maximum Element:", np.max(arr))
print("Minimum Element:", np.min(arr))
print("Sum:", np.sum(arr))