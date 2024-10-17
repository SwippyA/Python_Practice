# Accept a string from the user
user_input = input("Enter a string: ")


letter_count = 0
digit_count = 0
symbol_count = 0


for char in user_input:
    if char.isalpha():
        letter_count += 1
    elif char.isdigit():
        digit_count += 1
    else:
        symbol_count += 1

print("Number of letters:", letter_count)
print("Number of digits:", digit_count)
print("Number of symbols:", symbol_count)
