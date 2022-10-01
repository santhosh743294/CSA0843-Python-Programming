age=int(input("enter the age="))
a=18-age
if age<=0:
    print("please enter valid input")
elif age<18:
    print("you are allowed to vote after",a,"years")
else:
    print("you are eligible to vote")
