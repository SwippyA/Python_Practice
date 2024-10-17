def add(x, y):
    return x + y
def subtract(x, y):
    return x - y
def multiply(x, y):
    return x * y
def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Error! Division by zero."
# Taking two numbers as input from the user
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
# Taking the operator as input from the user
operator = input("Enter the operator (+, -, *, /): ")
# Performing the selected operation
if operator == '+':
    result = add(num1, num2)
    operation = "sum"
elif operator == '-':
    result = subtract(num1, num2)
    operation = "difference"
elif operator == '*':
    result = multiply(num1, num2)
    operation = "product"
elif operator == '/':
    result = divide(num1, num2)
    operation = "quotient"
else:
    result = "Invalid operator"
    operation = "operation"
# Printing the result
print(f"The {operation} of {num1} and {num2} is: {result}")
