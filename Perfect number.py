n= int(input("Enter the number: "))
sum1 = 0
for i in range(1, n):
    if(n % i == 0):
        sum1 = sum1 + i
if(sum1==n):
    print("number is perfect")
else:
    print("number is not perfect number")
