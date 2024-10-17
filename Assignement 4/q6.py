# Read 10 numbers from the user into a list
numbers = []
for _ in range(10):
    number = int(input("Enter a number: "))
    numbers.append(number)
    print("Numbers so far:", numbers)
