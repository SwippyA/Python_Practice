# Read 5 numbers from the user into a list
numbers = []
for _ in range(5):
    number = int(input("Enter a number: "))
    numbers.append(number)
# Print the input data and reversed list
print("Input data:", numbers)
print("Printing values from the list in reverse order:")
for number in reversed(numbers):
    print(number)
