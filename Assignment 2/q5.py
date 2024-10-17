import cmath


def find_roots(a, b, c):
    # Calculate the discriminant
    d = (b ** 2) - (4 * a * c)

    # Find two solutions
    sol1 = (-b - cmath.sqrt(d)) / (2 * a)
    sol2 = (-b + cmath.sqrt(d)) / (2 * a)

    return sol1, sol2


# Taking coefficients of the quadratic equation as input from the user
a = float(input("Enter coefficient a: "))
b = float(input("Enter coefficient b: "))
c = float(input("Enter coefficient c: "))

# Calculate the roots
root1, root2 = find_roots(a, b, c)

# Print the results
print(f"The roots of the quadratic equation are: {root1} and {root2}")
