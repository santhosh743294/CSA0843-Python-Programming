w=str(input("enter the string"))
vowels=0
for i in range(0,len(w)):
    ch=w[i]
    if ((ch=='a' or ch=='e' or ch=='i' or ch=='o' or ch=='u')):
        vowels += 1
        print("vowels:",vowels)
