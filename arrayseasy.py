"""
1.Largest element in a array
2.second element in a array
3.check array is sorted
4.remove duplicates from sorted array
5.left rotate array by one place
6.left rotate by D places
7.move zeroes to end
8.linear search
9.find the union
10.find missing number in an array
11.maximum consecutive ones
12.find the numbers that appears once, and other numbers twice
13.longest sub array with given sum k(positives).
14.longest sub array with sum k(positive+negative).
"""
class Arrayeasy:
    def largestelement(self,arr):
        temp=-1
        for i in arr:
            if i>temp:
                temp=i
        return temp
    def secondlargest(self,arr):
        largest=-1
        slargest=-1
        for i in range(len(arr)):
            if arr[i]>largest:
                slargest=largest
                largest=arr[i]
            elif arr[i]<largest and arr[i]>slargest:
                slargest=arr[i]
        return slargest
    def checkarrayissorted(self,arr):
        for i in range(len(arr)-1):
            if arr[i]<=arr[i+1]:
                continue
            else:
                return False
        return True
    def removeduplicate(self,arr):
        i=0
        for j in range(1,len(arr)):
            if arr[i]!=arr[j]:
                arr[i+1]=arr[j]
                i+=1
        return arr
    def leftrotateoneplace(self,arr):
            temp=arr[0]
            for i in range(1,len(arr)):
                arr[i-1]=arr[i]
            arr[len(arr)-1]=temp
            return arr
    def leftrotatekplaces(self,arr,k):
        k=k%len(arr)
        arr=arr[0:k][::-1]+arr[k:][::-1]
        arr=arr[::-1]
        return arr
    def movezeroestoend(self,arr):
        for j in range(len(arr)):
            if arr[j]==0:
                break
        for i in range(j+1,len(arr)):
            if arr[i]!=0:
                arr[i],arr[j]=arr[j],arr[i]
                j+=1
        return arr
    def linearsearch(self,arr,target):
        for i in range(len(arr)):
            if arr[i] == target:
                return i+1
        return -1
    def union(self,arr1,arr2):
        ans=[]
        n=len(arr1)
        m=len(arr2)
        i=0
        j=0
        while(i<n and j<m):
            if arr1[i]<=arr2[j]:
                if len(ans)==0 or ans[-1]!=arr1[i]:
                    ans.append(arr1[i])
                i+=1
            else:
                if len(ans)==0 or ans[-1]!=arr2[j]:
                    ans.append(arr2[j])
                j+=1
        while(j<m):
            if len(ans)==0 or ans[-1]!=arr2[j]:
                    ans.append(arr2[j])
            j+=1
        while(i<n):
            if len(ans)==0 or ans[-1]!=arr1[i]:
                ans.append(arr1[i])
            i+=1

        return ans
    def intersection(self,arr1,arr2):
        i=0;j=0
        ans=[]
        while(i<len(arr1) and j<len(arr2)):
            if arr1[i]<arr2[j]:
                i+=1
            elif arr2[j]<arr1[i]:
                j+=1
            else:
                ans.append(arr1[i])
        return ans
    def missing(self,arr):
        s=0;m=-1;ms=0
        for i in arr:
            s+=i
            m=max(m,i)

        for i in range(1,m+1):
            ms+=i
        return ms-s
    def max1(self,arr):
        m=0;cunt=0
        for i in arr:
            if i==1:
                cunt+=i
            else:
                cunt=0
            m=max(m,cunt)
        return m
    def once(self,arr):
        xor=0
        for i in arr:
            xor=xor^i
        return xor
    def sarrayk(self,arr,k):
        dk={}
        s=0;maxlen=0
        for i in range(len(arr)):
            s+=arr[i]
            if s==k:
                maxlen=max(maxlen,i+1)
            rem=s-k
            if rem in dk:
                l=i-dk[rem]
                maxlen=max(l,maxlen)
            if s not in dk:
                dk[s]=i
        return maxlen


obj=Arrayeasy()
sarrayk=obj.sarrayk([1,1,2,2,3,4,4],5)
mx=obj.max1([1 for i in range(1,1000000000)])
print(mx)
