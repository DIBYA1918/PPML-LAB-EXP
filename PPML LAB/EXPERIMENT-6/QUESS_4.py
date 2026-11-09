f = open("sample.txt", "w")

f.write("Hello Python\n")
f.write("File Handling")

f.close()

f = open("sample.txt", "r")

print("File Content:")
print(f.read())

f.seek(0)

print("File Pointer Position:", f.tell())

f.close()