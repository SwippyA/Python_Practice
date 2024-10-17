input_string = input("Enter three values separated by space: ")
input_list = input_string.split()
if len(input_list) == 3:
    val1, val2, val3 = input_list
    print(f"First value: {val1}")
    print(f"Second value: {val2}")
    print(f"Third value: {val3}")
else:
    print("Please enter exactly three values separated by space.")
languages_string = input("Enter names of programming languages separated by space: ")
languages_list = languages_string.split()
print("List of programming languages:")
for language in languages_list:
    print(language)
