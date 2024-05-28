def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    # Auxiliary array to avoid creating new lists in each recursion
    aux = [0] * len(arr)
    _merge_sort(arr, aux, 0, len(arr) - 1)
    return arr

def _merge_sort(arr, aux, left, right):
    if left >= right:
        return

    mid = (left + right) // 2
    _merge_sort(arr, aux, left, mid)
    _merge_sort(arr, aux, mid + 1, right)
    merge(arr, aux, left, mid, right)

def merge(arr, aux, left, mid, right):
    # Copy both halves into the auxiliary array
    for i in range(left, right + 1):
        aux[i] = arr[i]

    i, j = left, mid + 1
    for k in range(left, right + 1):
        if i > mid:  # Left half is exhausted
            arr[k] = aux[j]
            j += 1
        elif j > right:  # Right half is exhausted
            arr[k] = aux[i]
            i += 1
        elif aux[i] <= aux[j]:  # Smaller element from the left half
            arr[k] = aux[i]
            i += 1
        else:  # Smaller element from the right half
            arr[k] = aux[j]
            j += 1

# Example usage:
arr = [3, 4, 32, 45, 2, 12, 45, 6, 77]
print(merge_sort(arr))
