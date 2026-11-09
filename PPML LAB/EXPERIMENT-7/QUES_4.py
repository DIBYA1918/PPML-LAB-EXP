numbers = [1, -2, 0, 3, -4, 0, 5, -6]

positive = list(filter(lambda x: x > 0, numbers))
negative = list(filter(lambda x: x < 0, numbers))
zero = list(filter(lambda x: x == 0, numbers))

total = len(numbers)

p = len(positive) / total
n = len(negative) / total
z = len(zero) / total

print("Positive Ratio:", p)
print("Negative Ratio:", n)
print("Zero Ratio:", z)