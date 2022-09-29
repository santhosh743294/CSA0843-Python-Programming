dic={1:['a','b','c'],2:['d','e','f'],
     3:['g','h','i'],4:['j','k','l'],
     5:['m','n','o'],6:['p','q','r','s'],
     7:['t','u','v'],8:['w','x','y','z']}
num=input("Enter Number")
digits=[int(x) for x in num]
output_list=[]
if len(digits)==2:
    for i in dic[digits[0]]:
        for j in dic[digits[1]]:
            output_list.append(i+j)
elif len(digits)==1:
    for i in dic[digits[0]]:
        output_list.append(i)
elif len(digits)==0:
    pass
else:
    print("Wrong Input")
print(output_list)
