import numpy as np

arr = np.array([10, 20, 30, 40, 50])

np.save("myarray.npy", arr)

print("Array Saved Successfully")

loaded_array = np.load("myarray.npy")

print("Loaded Array:", loaded_array)