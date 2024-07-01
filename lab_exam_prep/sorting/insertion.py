def insertion_sort(arr):
   for i in range (1, len(arr)):
      key= arr[i]
      j=i-1
      while j>=0 and key<arr[j]:
         arr[j+1]=arr[j]
         j=j-1
      arr[j+1]=key
   for u in range(len(arr)):
      print(arr[u])

arr=[4,2,7,8,1]
insertion_sort(arr)


