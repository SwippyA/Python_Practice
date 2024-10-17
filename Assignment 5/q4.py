# Define the strings
string1 = "MIT WPU FoS – School of Computer Science"
string2 = "Python Programming"

# a) Print string1 and string2
print("String1:", string1)
print("String2:", string2)

# b) Add two strings and print
string_add = string1 + " " + string2
print("Addition of string1 and string2:", string_add)

# c) Print string2, 10 times
print("String2, 10 times:", string2 * 10)

# d) Print the count of letter 'o' in string1 and string2
count_o_string1 = string1.count('o')
count_o_string2 = string2.count('o')
print("Count of 'o' in string1:", count_o_string1)
print("Count of 'o' in string2:", count_o_string2)

# e) Print the length of string1 and string2
length_string1 = len(string1)
length_string2 = len(string2)
print("Length of string1:", length_string1)
print("Length of string2:", length_string2)

# f) Print the index and value of all items in string as pair for string1 and string2
print("Index and value pairs for string1:")
for index, value in enumerate(string1):
    print(index, value)

print("Index and value pairs for string2:")
for index, value in enumerate(string2):
    print(index, value)
