import math

a = float(input("Enter first side: "))
b = float(input("Enter second side: "))
c = float(input("Enter third side: "))

s = (a + b + c) / 2

if a + b > c and a + c > b and b + c > a:
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))
    print("Area of the triangle =", area)
else:
    print("The given sides cannot form a triangle.")
