
a = float(input("Enter the first number: "))
b = float(input("Enter the second number: "))

addition = a + b
subtraction = a - b
multiplication = a * b
division = a / b if b != 0 else 'Undefined (division by zero)'
modulo = a % b if b != 0 else 'Undefined (modulo by zero)'


print(f"Addition: {addition}")
print(f"Subtraction: {subtraction}")
print(f"Multiplication: {multiplication}")
print(f"Division: {division}")
print(f"Modulo: {modulo}")
