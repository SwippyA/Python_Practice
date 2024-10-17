
num  = [ 123 , 678, 34, 8 , 78, 89, 22,101 , 333, 888, 456, 761, 4 , 7, 11]

count_even =0
count_odd =0
for x in num:
    if(x % 2 ==0):
        count_even+= 1
    else:
        count_odd+=1

print(count_odd)
print(count_even)