def selectionSort(arr,size):
  for i in range(size):
    minimum = i
    for j in range(i+1,size):
      if arr[j] < arr[minimum]:
        minimum = j 
    arr[i],arr[minimum] = arr[minimum],arr[i]


arr=[987,1,34,11,78,-9,100,28,13]
size = len(arr)
selectionSort(arr,size)
print(arr)