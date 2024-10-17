num_div_9 =[]
num_mul_5 =[]

for x in range(50,101):
    if(x % 9 == 0 ):
        num_div_9.append(x)
    if(x % 5 ==0 ):
        num_mul_5.append(x)

print(num_mul_5)
print(num_div_9)
