def selection_sort(arr):
    for i in range(len(arr)):
        min_index=i
        for j in range(i+1, len(arr)):
            if arr[j]<arr[min_index]:
                min_index=j
        arr[i],arr[min_index]=arr[min_index],arr[i]
    for u in range(len(arr)):
      print(arr[u])
        
arr=[4,2,7,8,1]
selection_sort(arr)