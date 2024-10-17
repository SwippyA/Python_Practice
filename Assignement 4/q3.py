# Create a list with nested list
list3 = [11, 33, 22, 11, [11, 22, 33, 'BCA', 'SoCS']]

# a) Print the list
print("List3:", list3)

# b) Replace string 'BCA' with 'B.Sc CS'
list3[4][3] = 'B.Sc CS'
print("List3 after replacing 'BCA' with 'B.Sc CS':", list3)

# c) Print the index of string 'B.Sc CS'
index_bsc_cs = list3[4].index('B.Sc CS')
print("Index of 'B.Sc CS':", index_bsc_cs)

# d) How many times number 11 is appearing in the list
count_11 = list3.count(11)
print("Number 11 appears", count_11, "times")

# e) Extend the list by adding 'FoS' and 'Python'
list3.extend(['FoS', 'Python'])
print("List3 after extending:", list3)

# f) Reverse the order of items in list
list3.reverse()
print("List3 after reversing:", list3)
