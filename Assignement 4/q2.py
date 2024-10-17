# Create list1 and list2
list1 = ['rose', 'lily', 'tulip', 'jasmine', 'MyName', 5, 10, 3.4, 4.5]
list2 = ['apple', 'banana', 'mango', 'grapes', 'orange', 'PRN12345', 15, 20]

# a) Print list1 and list2
print("List1:", list1)
print("List2:", list2)

# b) Append 'MITWPU' to list1 and 'PUNE' to list2
list1.append('MITWPU')
list2.append('PUNE')

# c) Add two lists and print
combined_list = list1 + list2
print("Combined list:", combined_list)

# d) Repeat list1 three times
repeated_list1 = list1 * 3
print("List1 repeated three times:", repeated_list1)

# e) Insert 'SoCS' at index 3 in list1
list1.insert(3, 'SoCS')
print("List1 after inserting 'SoCS' at index 3:", list1)
