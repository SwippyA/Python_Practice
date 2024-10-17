# Initialize a list
my_list = [1, 2, 3, 4, 5]

my_list.append(6)
print("After append(6):", my_list)

my_list.extend([7, 8, 9])
print("After extend([7, 8, 9]):", my_list)

my_list.insert(3, 'a')
print("After insert(3, 'a'):", my_list)

my_list.remove('a')
print("After remove('a'):", my_list)

popped_element = my_list.pop(2)
print("After pop(2):", my_list)
print("Popped element:", popped_element)

my_list.clear()
print("After clear():", my_list)

my_list = [1, 2, 3, 4, 5, 3, 3]

index_of_3 = my_list.index(3)
print("Index of first occurrence of 3:", index_of_3)

count_of_3 = my_list.count(3)
print("Count of 3 in the list:", count_of_3)

my_list.sort()
print("After sort():", my_list)

my_list.reverse()
print("After reverse():", my_list)

my_list_copy = my_list.copy()
print("Copy of the list:", my_list_copy)
