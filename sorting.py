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
                


obj=sorting()
selection_sort=obj.selection_sort([3,1,10,0,8,86,45])
bubble_sort=obj.bubble_sort([1,2,3])
insertion_sort=obj.insertion_sort([3,1,10,0,8,86,45])
print(insertion_sort)
