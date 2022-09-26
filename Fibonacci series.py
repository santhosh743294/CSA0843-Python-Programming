nterms=int(input("how manyterms:"))
n1,n2=0,1
count=0
if nterms<=0:
    print("invalid input")
elif nterms==1:
    print("fibonacci sequenece upto",nterms,":")
    print(n1)
else:
    print("fibonaccisequence:")
    while count<nterms:
        print(n1)
        nth=n1+n2
        n1=n2
        n2=nth
        count+=1
