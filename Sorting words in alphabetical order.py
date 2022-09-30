Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:06:47) [MSC v.1914 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> n=int(input("enter number of words : "))
words=[]
print("enter the words")
for i in range(0,n):
    y=str(input())
    words.append(y)
print("words=",words)
print("input your choice:")
choice=input("assending or dessending :")
if(choice == 'a'or choice == 'A'):
    words.sort()
    print("the ascending sorted list are : ",words)
elif(choice == 'd' or choice == 'D'):
    words.sort(reverse=True)
    print("the descending sorted list are = ",words)
else:
    print("invalid input")
