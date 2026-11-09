n = input("Enter a 5-digit number: ")

if len(n) == 5 and n.isdigit():
    print("Digits at odd locations are:")
    print(n[0], n[2], n[4])
else:
    print("Please enter a valid 5-digit number.")
