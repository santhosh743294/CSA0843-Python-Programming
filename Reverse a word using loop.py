def reverse(s):
    str = ""
    for i in s:
        str = i + str
    return str
s =input("enter the string")  
print("The reversed string(using loops) is : ", end="")
print(reverse(s))
