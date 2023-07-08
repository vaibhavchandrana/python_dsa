#this approach work when array is sorted
#tc-O(nlogn)
def approach1(arr,size):
    arr.sort()
    print('Sorted array is ',arr)
    return arr[size-2]

def approach2(arr,size):
    maxi=max(arr)
    secondMax=0
    for i in range(0,size):
        if arr[i]>secondMax and arr[i]<maxi:
            secondMax=arr[i]
    return secondMax


arr=[5,7,7,6,4,6,3,2,5]

print("second Largest is ",approach2(arr,len(arr)))