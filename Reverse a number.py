num  = int(input("enter integer to display it in  reverse="))
reverse = 0
remainder = 0

while num != 0:
    remainder = num % 10
    reverse = reverse * 10 + remainder
    num //= 10

print("Reversed Number: " +str(reverse))
