array   = [2,7,9,5,3,1,6,8]

def insertionee_sort(array: list) -> list:
    for i in range(1, len(array)):
        
        to_be_inserted_numba = array[i]
        j = i - 1

        while j >= 0 and array[j] > to_be_inserted_numba:
            array[j + 1] = array[j]
            j -= 1


        array[j + 1] = to_be_inserted_numba

    return array

print(insertionee_sort(array))
