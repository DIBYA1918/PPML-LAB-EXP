import matplotlib.pyplot as plt

data = [10, 20, 20, 30, 30, 30, 40, 40, 50, 60]

plt.figure(figsize=(10, 4))

plt.subplot(1, 2, 1)
plt.hist(data, bins=5)
plt.title("Histogram")
plt.xlabel("Values")
plt.ylabel("Frequency")

plt.subplot(1, 2, 2)
plt.boxplot(data)
plt.title("Box Plot")
plt.ylabel("Values")

plt.tight_layout()
plt.show()