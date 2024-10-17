given_list = ["hey", "there", "", "what's", "", "up", "", "?"]
modified_list = []

for item in given_list:
    if item:
        modified_list.append(item)

print("Modified List:", modified_list)


# given_list = ["hey", "there", "", "what's", "", "up", "", "?"]
# modified_list = list(filter(None, given_list))
# print("Modified List:", modified_list)
