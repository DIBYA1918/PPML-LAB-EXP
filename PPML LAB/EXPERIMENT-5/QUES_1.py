d1 = {}
d2 = {}

n = int(input("Enter number of elements in first dictionary: "))

for i in range(n):
    key = input("Enter key: ")
    value = int(input("Enter value: "))
    d1[key] = value

m = int(input("Enter number of elements in second dictionary: "))

for i in range(m):
    key = input("Enter key: ")
    value = int(input("Enter value: "))
    d2[key] = value

d1.update(d2)

print("Merged dictionary:", d1)
