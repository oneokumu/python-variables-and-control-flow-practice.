# Ask the user to input the lengths of the triangle's sides
side1 = float(input("Enter the length of the first side: "))
side2 = float(input("Enter the length of the second side: "))
side3 = float(input("Enter the length of the third side: "))

# Determining the type of triangle
if side1 == side2 == side3:
    print("The triangle is Equilateral.")
elif side1 == side2 or side2 == side3 or side1 == side3:
    print("The triangle is Isosceles.")
else:
    print("The triangle is Scalene.")
