s = input("Enter a string: ")

mid = len(s) // 2

if len(s) % 2 == 0:
    first = s[:mid]
    second = s[mid:]
else:
    first = s[:mid]
    second = s[mid+1:]

if first == second:
    print("Symmetrical")
else:
    print("Not Symmetrical")

if s == s[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")