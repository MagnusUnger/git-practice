def mergee_sort(array: list) -> list:
    #well if the array is array is less or equals 1 element ... its sorted .. 
    if len(array) <= 1:
        return array

    middle = len(array) // 2    #what is this operator? -> // ... im assuming divide with no rest?

    left_half   = mergee_sort(array[:middle])
    right_half  = mergee_sort(array[middle:])

    return merge(left_half, right_half)


def merge(left, right):
    sorted = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):
        if left[i]  <= right[j]:
            sorted.append(left[i])
            i += 1

        else:
            sorted.append(right[j])
            j += 1


    sorted.extend(left[i:])
    sorted.extend(right[j:])

    return sorted


example = [8,3,2,7,6,9,4,5]

print(mergee_sort(example))
            
    
