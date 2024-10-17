list_of_number = []
for i in range(200, 251):
    list_of_number.append(i)

for x in list_of_number:
    num = str(x)
    count = 0
    for y in num:
        if int(y) % 2 == 0:
            count += 1
        else:
            break

    if count == len(num):  # Ensure all digits are even
        print(x)
