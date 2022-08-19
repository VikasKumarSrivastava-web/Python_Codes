#main logic
def insertionSort(arr,n):
  for i in range(1,n):
    curr= arr[i]
    j = i
    while j > 0 and arr[j-1] > curr:
      arr[j] = arr[j-1]
      j = j - 1
    arr[j] = curr

#driver code
arr=[2,55,1,10,11,100,90,90,-1]
n = len(arr)
insertionSort(arr,n)
print(arr)