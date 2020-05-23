def mergesort(arr) :
    if len(arr) > 1:
        mid = len(arr)/2
        LH = arr[:int(mid)]  # Left Half
        RH = arr[int(mid):]  # Right Half
        mergesort(LH)
        mergesort(RH)

        i=j=k=0
        while i< len(LH) and j< len(RH) :
            if LH[i]<RH[j] :
                arr[k]=LH[i]
                i+=1
            else :
                arr[k]=RH[j]
                j+=1
            k+=1
        while i< len(LH) :
            arr[k] = LH[i]
            i+=1
            k+=1
        while j< len(RH) :
            arr[k] = RH[j]
            j+=1
            k+=1
            

arr = [4,14,45,23,12,6,7,2,34,1,101,3]
mergesort(arr)
print(arr)
