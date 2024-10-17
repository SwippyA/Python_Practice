def swap_numbers(a, b):
    # Using a temporary variable to swap the numbers
    temp = a
    a = b
    b = temp
    return a, b

# Taking two numbers as input from the user
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Swapping the numbers
num1, num2 = swap_numbers(num1, num2)

# Printing the swapped values
print(f"After swapping: First number is {num1} and Second number is {num2}")
