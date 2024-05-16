def quick_sort(arr):
    n= len(arr)
    if len(arr)<1:
        return arr
    pivot=arr[n//2]
    left=[]
    right=[]
    equal=[]
    for i in arr:
        if(i<pivot):
            left.append(i)
        elif(i>pivot):
            right.append(i)
        else:
            equal.append(i)
    return quick_sort(left)+equal+quick_sort(right)

    