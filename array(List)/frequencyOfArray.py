arr=[1,2,2,3,4,4,5,5,6]
freq={}
for i in range(0,len(arr)):
    if arr[i] in freq:
        freq[arr[i]]+=1
    else:
        freq[arr[i]]=1

for k,v in freq.items():
    print(k,"comes ",v ,"times")