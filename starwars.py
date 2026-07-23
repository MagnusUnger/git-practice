#Simple bublee-sort

array = [1,5,4,8,2,3,9,7,6]

for i in range(len(array)):
    for j in range(len(array)-1):
        if array[j] > array[j+1]:
            temp        = array[j]
            array[j]    = array[j + 1]
            array[j + 1]= temp

print(array)
