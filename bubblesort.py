def bubble_sort(arr):
  for n in range(0,len(arr)):
    for i in range(0,len(arr)-1):
      if arr[i] < arr[i + 1]:
        arr[i], arr[i + 1] = arr[i + 1], arr[i]

arr = [39, 12, 18, 85, 72, 10, 2, 18]
bubble_sort(arr)
print("Sorted list is:")
print(arr)
