try:
    r=int(input("enter the no.of rows="))
    if(r<=0):
        print("invalid input")
        exit()
    else:
        for i in range(1,r+1):
            k=0.1
            for j in range(1,i+1):
                print("%.1f"%k,end=" ")
                k=k+0.1
            print("\n")
except valueError:
    print("invalid")
