class sorting:


    def bubble_sort(self, arr):
        for i in range(len(arr)):
            swapped=False
            for j in range(len(arr)-i-1):
                if arr[j]>arr[j+1]:
                    arr[j],arr[j+1]=arr[j+1],arr[j]
                    swapped=True
            if not swapped:
                break
            print(arr)
        return arr



    def selection_sort(self,arr):
        for i in range(len(arr)):
            for j in range(i+1,len(arr)):
                if arr[j]<arr[i]:
                    arr[i],arr[j]=arr[j],arr[i]
        return arr




    def insertion_sort(self,arr):
        for i in range(len(arr)):
            j=i
            while(j>0 and arr[j-1]>arr[j]):
                arr[j-1],arr[j]=arr[j],arr[j-1]
                j-=1
        return arr




    def merge_sort(self,arr,low,high):
        mid=(low+high)//2
        if low>=high:
            return 
        self.merge_sort(arr,low,mid)
        self.merge_sort(arr,mid+1,high)
        self.merge(arr,low,mid,high)




    def merge(self,arr,low,mid,high):
        left=low
        right=mid+1
        temp=[]
        while(left<=mid and right<=high):
            if arr[left]<=arr[right]:
                temp.append(arr[left])
                left+=1
            else:
                temp.append(arr[right])
                right+=1
        while(left<=mid):
            temp.append(arr[left])
            left+=1
        while(right<=high):
            temp.append(arr[right])
            right+=1
        for i in range(low,high+1):
            arr[i]=temp[i-low]



    def quick_sort(self,arr,low,high):
        if low<high:
            pindex=self.part(arr,low,high)
            self.quick_sort(arr,low,pindex-1)
            self.quick_sort(arr,pindex+1,high)
    def part(self,arr,low,high):
        pivot=arr[low]
        i=low
        j=high
        while(i<j):
            while(arr[i]<=pivot and i<=high-1):
                i+=1
            while(arr[j]>pivot and j>=low+1):
                j-=1
            if i<j:
                arr[i],arr[j]=arr[j],arr[i]
        arr[low],arr[j]=arr[j],arr[low]
        return j




                
arr=[3,1,10,0,8,86,45]

obj=sorting()
quick_sort=obj.quick_sort(arr,0,6)
print(arr)
