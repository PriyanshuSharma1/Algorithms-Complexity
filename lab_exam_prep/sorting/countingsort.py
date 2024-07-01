def counting_sort(arr):
    max_val=max(arr)
    m=max_val+1
    count= [0]*m

    for a in arr:
        count[a]=count[a]+1

    i=0
    for a in range(m):
        for c in range(count[a]):
            arr[i]=a
            i=i+1

arr=[4,3,2,2,4,1,5,2,5,1]
counting_sort(arr)
print(arr)