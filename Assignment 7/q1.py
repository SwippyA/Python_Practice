def factorial(n):
    return 1 if n == 0 else n * factorial(n - 1)

# Input from the user
number = int(input("Enter a number: "))
print(f"The factorial of {number} is {factorial(number)}")
