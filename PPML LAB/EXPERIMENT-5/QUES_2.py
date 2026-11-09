d = {'A': 50, 'B': 80, 'C': 30, 'D': 90, 'E': 60}

key = max(d, key=d.get)

print("Dictionary:", d)
print("Key with maximum value:", key)
print("Maximum value:", d[key])
