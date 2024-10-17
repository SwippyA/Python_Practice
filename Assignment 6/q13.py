def display_powers_of_two(n):
    for i in range(n):
        print(f"2^{i} = {2 ** i}")


n = int(input("Enter the number of terms: "))
if n <= 0:
    print("Please enter a positive integer.")
else:
     display_powers_of_two(n)

