# Sample input list
input_list = [10, 20, 24, 25, 26, 35, 70]
# Check if the task is possible
if len(input_list) > 4:
    new_list = input_list[2:-2]
    print("New list:", new_list)
else:
    print("Not possible")
