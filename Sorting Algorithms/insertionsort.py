def insertionsort(arr) :
    for i in range(1 , len(arr)) :
        recent_number = arr[i]
        for j in range(i-1 , -1 , -1):
            if arr[j] > recent_number :
                arr[j],arr[j+1] = arr[j+1],arr[j]
            else :
                arr[j+1] = recent_number
                break
    return arr

arr = [2,12,1,34,21,45,24,56,5]
insertionsort(arr)
print(arr)
