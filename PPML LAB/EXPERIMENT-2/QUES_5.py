s = input("Enter a string: ")

reverse = s[::-1]
vowels = 0
consonants = 0

for ch in s.lower():
    if ch.isalpha():
        if ch in "aeiou":
            vowels += 1
        else:
            consonants += 1

print("Reversed string:", reverse)
print("Number of vowels:", vowels)
print("Number of consonants:", consonants)
