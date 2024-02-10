a = int(input('Enter the upper limit:'))
b = int(input('Enter the lower limit:'))
sum = 0

for x in range(a,b+1):
    sum +=x
    
print(f'Sum of number in range {a} to {b} is {sum}')