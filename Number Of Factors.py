try:
    n=(int(input("enter a number to find the factors => ")))
    if(n<=0):
        print("enter the value greater than zero")
    else:
        lis=[]
        for i in range(1,n+1):
            if(n%i==0):
                lis.append(i)
        print(lis)
        print("the no of factors for the the number",n,"is => ",len(lis))
        ele=int(input("N => "))
        if(ele==0):
            print("enter the value greater than zero")
        elif ele>len(lis):
            print(n,"does not have",ele,"number of factorials....!!!!!")
        else:
            print("the",ele,"factorial of",n,"is => ",lis[ele-1])
except:
    print("enter an integer not a string....!!!!!")
