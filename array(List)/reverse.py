size=int(input("enter the size"))
list1=[]
def reverFunc(arr):
    st=0
    end=len(arr)-1
    for i in range(0,int(end/2)+1):
        temp=arr[st]
        arr[st]=arr[end]
        arr[end]=temp
        st+=1
        end-=1
    return arr
for i in range(0,size):
    x=int(input("enter elemenent"))
    list1.append(x)
# list2=list1[::-1]
print("original array is ",list1)
print("reverse array is ",reverFunc(list1))
