def even_values(a):
    even = []

    for n in a:
        if n % 2 == 0:
            even.append(n)

    return even

a = [10, 15, 20, 25, 30, 35, 40, 45]

result = even_values(a)

print("Original list:", a)
print("Even values:", result)
