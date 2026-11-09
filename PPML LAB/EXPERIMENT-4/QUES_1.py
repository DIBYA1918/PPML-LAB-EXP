a = []

for i in range(10):
    n = int(input("Enter a number: "))
    a.append(n)

unique = list(set(a))

if len(unique) < 2:
    print("Second largest and smallest do not exist")
else:
    largest = second_largest = float('-inf')
    smallest = second_smallest = float('inf')

    for n in unique:
        if n > largest:
            second_largest = largest
            largest = n
        elif n > second_largest:
            second_largest = n

        if n < smallest:
            second_smallest = smallest
            smallest = n
        elif n < second_smallest:
            second_smallest = n

    print("Second largest =", second_largest)
    print("Second smallest =", second_smallest)