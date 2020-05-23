def quicksort(arr , low , high) :
    if low < high :
        pivot = partition(arr , low ,high)
        quicksort(arr , low , pivot-1)
        quicksort(arr , pivot+1 , high)

def partition(arr , low , high) :
    i = low-1
    pivot = arr[high]
    for j in range(low , high) :
        if arr[j] < pivot :
            i+=1
            arr[i] , arr[j] = arr[j] , arr[i]
    arr[i+1] , arr[high] = arr[high] , arr[i+1]
    return i+1
        
arr = [4,14,45,23,12,6,7,2,34]
n = len(arr)
quicksort(arr , 0 , n-1)
for i in range(n) :
    print(arr[i])
