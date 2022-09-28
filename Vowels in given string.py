str=input("enter the string:")
vowels=0
for i in str:
    if(i=='a' or i=='e' or i=='o' or i=='u' or i=='i' or i=='A' or i=='E' or i=='O' or i=='U' or i=='I' ):
        vowels+=1
print(" number of vowels for given string",str,"is:",vowels)
