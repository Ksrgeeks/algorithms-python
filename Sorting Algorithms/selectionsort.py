arr = [4,14,45,23,12,6,7,2,34]
for i in range(len(arr)):
    min = i
    for j in range(i+1 , len(arr)) :
        if arr[min] > arr[j] :
            min = j
    arr[i] , arr[min] = arr[min] , arr[i]
for i in range(len(arr)) :
    print(arr[i])
