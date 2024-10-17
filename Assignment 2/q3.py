import math

def calculate_area(a, b, c):
    # Calculate the semi-perimeter
    s = (a + b + c) / 2

    # Calculate the area using Heron's formula
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))

    return area


# Taking the sides of the triangle as input from the user
a = float(input("Enter the length of side a: "))
b = float(input("Enter the length of side b: "))
c = float(input("Enter the length of side c: "))

# Calculate the area
area = calculate_area(a, b, c)

# Print the result
print(f"The area of the triangle with sides {a}, {b}, and {c} is: {area}")
