n = int(input("Enter a number: "))

sum = 0

for i in range(1, n):
    if n > 0 and n % i == 0:
        sum = sum + i

if n > 0 and sum == n:
    print("Perfect number")
else:
    print("Not a perfect number")
