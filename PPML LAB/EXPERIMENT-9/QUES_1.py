import pandas as pd

data = [10, 20, 30, 40, 50]

s = pd.Series(data)

print("Pandas Series:")
print(s)

print("First Element:", s[0])
print("Last Element:", s[4])
print("Index:", s.index)
print("Values:", s.values)
print("Mean:", s.mean())
print("Maximum:", s.max())
print("Minimum:", s.min())