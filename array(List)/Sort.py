arr=[1,5,3,4,2,6]
for i in range(0,len(arr)):
    for j in range(i+1,len(arr)):
        if arr[i]<arr[j]:
            t=arr[i]
            arr[i]=arr[j]
            arr[j]=t

print(arr)
