n = int(input("Enter N: "))

for i in range(2, n + 1):
    c1 = 0
    for j in range(1, i + 1):
        if i % j == 0:
            c1 += 1

    if c1 == 2:
        c2 = 0
        for j in range(1, i + 3):
            if (i + 2) % j == 0:
                c2 += 1

        if c2 == 2:
            print(i, i + 2)