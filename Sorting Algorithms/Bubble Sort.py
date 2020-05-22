numbers = [12,15,13,3,48,22]
for x in range(len(numbers)) :
    swap = False
    i=0
    while i < len(numbers)-1 :
        if numbers[i] > numbers[i+1] :
            numbers[i] , numbers[i+1] = numbers[i+1] , numbers[i]
            swap = True
        i+=1
    if swap == False :
        break

print(numbers)
