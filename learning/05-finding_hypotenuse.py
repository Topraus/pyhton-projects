import math
a = float(input("Enter the length of the first leg: "))
b = float(input("Enter the length of the second leg: "))

c_squared = a**2 + b**2 

hypotenuse = math.sqrt(c_squared)

print(f"The hypotenuse is {hypotenuse}cm.")

