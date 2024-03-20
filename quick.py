def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def quicksort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quicksort(arr, low, pi - 1)
        quicksort(arr, pi + 1, high)

def quick_select(arr, low, high, i):
    if low == high:
        return arr[low]

    pivot_index = partition(arr, low, high)
    k = pivot_index - low + 1

    if i == k:
        return arr[pivot_index]
    elif i < k:
        return quick_select(arr, low, pivot_index - 1, i)
    else:
        return quick_select(arr, pivot_index + 1, high, i - k)

def ith_order_statistic(arr, i):
    if i < 1 or i > len(arr):
        return None
    return quick_select(arr, 0, len(arr) - 1, i)

# Example
arr = [12, 3, 5, 7, 4, 19, 26]
i = 3
result = ith_order_statistic(arr, i)
print(f"The {i}th order statistic is: {result}")
