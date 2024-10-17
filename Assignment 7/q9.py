
user_input = input("Enter a string: ")
lowercase_letters = [char for char in user_input if char.islower()]
uppercase_letters = [char for char in user_input if char.isupper()]
result = ''.join(lowercase_letters + uppercase_letters)
print("String with lowercase letters followed by uppercase letters:", result)
