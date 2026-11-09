d = {'A': 10, 'B': 20, 'C': 10, 'D': 30, 'E': 20}

new = {}

for key, value in d.items():
    if value not in new.values():
        new[key] = value

print("Original dictionary:", d)
print("Dictionary after removing duplicates:", new)
