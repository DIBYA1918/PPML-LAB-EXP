import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [10, 25, 15, 30, 20]

plt.figure(figsize=(10, 4))

plt.subplot(1, 2, 1)
plt.scatter(x, y)
plt.title("Scatter Plot")
plt.xlabel("X Axis")
plt.ylabel("Y Axis")

plt.subplot(1, 2, 2)
plt.bar(x, y)
plt.title("Bar Plot")
plt.xlabel("X Axis")
plt.ylabel("Y Axis")

plt.tight_layout()
plt.show()