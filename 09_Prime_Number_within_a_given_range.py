lower_limit = int(input("Enter Lower limit: "))
upper_limit = int(input("Enter Upper limit: "))

for i in range(lower_limit,upper_limit+1):
    count=0
    for j in range(1,i+1):
        if i%j == 0:
            count += 1
    if count<=2:
        print(f"{j} is a Prime Number")