size=int(input("enter the size"))
list1=[]
for i in range(0,size):
    x=int(input("enter elemenent"))
    list1.append(x)

print(list1[::-1])
