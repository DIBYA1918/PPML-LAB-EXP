import math

a = float(input("Enter coefficient a: "))
b = float(input("Enter coefficient b: "))
c = float(input("Enter coefficient c: "))

if a == 0:
    print("It is not a quadratic equation.")
else:
    d = b**2 - 4*a*c

    if d > 0:
        r1 = (-b + math.sqrt(d)) / (2*a)
        r2 = (-b - math.sqrt(d)) / (2*a)
        print("Root 1 =", r1)
        print("Root 2 =", r2)
    elif d == 0:
        r = -b / (2*a)
        print("Both roots are equal:", r)
    else:
        real = -b / (2*a)
        imaginary = math.sqrt(-d) / abs(2*a)
        print("Root 1 =", complex(real, imaginary))
        print("Root 2 =", complex(real, -imaginary))
