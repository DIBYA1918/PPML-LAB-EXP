import matplotlib.pyplot as plt
import numpy as np

plt.figure(figsize=(10, 4))

plt.subplot(1, 2, 1)

subjects = ['Python', 'Java', 'C', 'C++']
marks = [30, 25, 20, 25]

plt.pie(marks, labels=subjects, autopct='%1.1f%%')
plt.title("Pie Chart")

plt.subplot(1, 2, 2)

x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)

X, Y = np.meshgrid(x, y)
Z = X**2 + Y**2

plt.contour(X, Y, Z)
plt.title("Contour Plot")
plt.xlabel("X Axis")
plt.ylabel("Y Axis")

plt.tight_layout()
plt.show()