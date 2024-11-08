"""
1.binary search to find in x sorted array
2.implement lower bound
3.implement upper bound
4.search insert position
5.floor/cell in sorted array
6.find the first or last occurrence of a given number in a sorted array
7.count occurrences of a number in a sorted array with duplicates
8.search in rotated sorted array 1
9.search in rotated sorted array 2
10.find minimum in rotated sorted array
11.find out how many times has an array been rotated
12.single element in a sorted array
13.find peak element
"""
class binarysearch:
    def bsearch(self,arr,target):
        low=0
        high=len(arr)-1
        while(low<=high):
            mid=(low+high)//2
            if arr[mid]<target:
                low=mid+1
            elif arr[mid]>target:
                high=mid-1
            else:
                return True
        return False
    def lower_bound(self,arr,target):
        low=0
        high=len(arr)-1
        ans=len(arr)
        while(low<=high):
            mid=(low+high)//2
            if arr[mid]>=target:
                ans=mid
                high=mid-1
            else:
                low=mid+1
        return ans      
    def upper_bound(self,arr,target):
        low=0
        high=len(arr)-1
        ans=len(arr)
        while(low<=high):
            mid=(low+high)//2
            if arr[mid]>target:
                ans=mid
                high=mid-1
            else:
                low=mid+1
        return ans
    def floor(self,arr,target):
        low=0
        high=len(arr)-1
        while(low<=high):
            mid=(low+high)//2
            if arr[mid]<=target:
                ans=arr[mid]
                low=mid+1
            else:
                high=mid-1
        return ans
    def rotated_sorted_array1(self,arr,k):
        low=0
        high=len(arr)-1
        while(low<=high):
            mid=(low+high)//2
            if arr[mid]==k:
                return mid
            elif arr[low]<=arr[mid]:
                if k>=arr[low] and k<=arr[mid]:
                    high=mid-1
                else:
                    low=high+1
            else:
                if arr[mid]<=k and k<=arr[high]:
                    low=mid+1
                else:
                    high=mid-1
        return -1
    def rotated_sorted_array2(self,arr,k):
        low=0
        high=len(arr)-1
        while(low<=high):
            mid=(low+high)//2
            if arr[mid]==k:
                return mid
            if arr[low]==arr[mid] and arr[mid]==arr[high]:
                continue
            elif arr[low]<=arr[mid]:
                if k>=arr[low] and k<=arr[mid]:
                    high=mid-1
                else:
                    low=high+1
            else:
                if arr[mid]<=k and k<=arr[high]:
                    low=mid+1
                else:
                    high=mid-1
        return -1
    def findmin(self,arr):
        low=0
        high=len(arr)-1
        ans=100000
        while(low<=high):
            mid=(low+high)//2
            if arr[low]<=arr[mid]:
                ans=min(ans,arr[low])
                low=mid+1
            else:
                ans=min(ans,arr[mid])
                high=mid-1
        return ans
''' Search insert position is same as lower bound
    ceil of the array is same as lower bound
    first occurence is same as lower bound
    last occurence is same as upper bound-1
'''
    


obj=binarysearch()
bsearch=obj.bsearch([1,2,3,4,5],6)
lower_bound=obj.lower_bound([1,3,5,7,9,11,45],4)
upper_bound=obj.upper_bound([1,2,2,2,2,3,5,8,99,101],6)
floor=obj.floor([1,2,4,5,6,6,6],10)
findmin=obj.findmin([2,3,4,5,0,1])
print(findmin)

