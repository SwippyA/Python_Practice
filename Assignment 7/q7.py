# Input the lengths of the three sides of the triangle
a = float(input("Enter the length of the first side: "))
b = float(input("Enter the length of the second side: "))
c = float(input("Enter the length of the third side: "))

# Check the type of trianglea
if a == b == c:
    print("The triangle is equilateral.")
elif a == b or b == c or c == a:
    print("The triangle is isosceles.")
else:
    print("The triangle is scalene.")
