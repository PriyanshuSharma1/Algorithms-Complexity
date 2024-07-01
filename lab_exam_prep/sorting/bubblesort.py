def bubblesort(arr):
    n=len(arr)
    for i in range(n):
        swapped= False
        for j in range(0, n-i-1):
            if arr[j]>arr[j+1]:
                arr[j+1],arr[j]=arr[j],arr[j+1]
                swapped=True
        if not swapped:
            break
        
arr=[4,2,3,7,1]
bubblesort(arr)
print(arr)