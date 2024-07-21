def mergesort(arr,low,high):
    if low==high:
        return 0
    mid=(low+high)//2
    mergesort(arr,low,mid)
    mergesort(arr,mid+1,high)
    merge(low,high,mid,arr)
def merge(low,high,mid,arr):
    l=low
    r=mid+1
    temp=[]
    while(l<=mid and r<=high):
        if arr[l]<=arr[r]:
            temp.append(arr[l])
            l+=1
        else:
            temp.append(arr[r])
            r+=1
    while(l<=mid):
        temp.append(arr[l])
        l+=1
    while(r<=high):
        temp.append(arr[r])
        r+=1
    #for i in range(low,high+1):
     #   arr[i]=temp[i-low]
    arr[low:high+1]=temp[0:high+1]
dk=[5,8,99,100,5,3,27,89]
mergesort(dk,0,len(dk)-1)
print(dk)