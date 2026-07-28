#Simple bublee-sort
def bublee_sort(array: list) ->list:
    for i in range(len(array)):
        was_swapped = False

        for j in range(len(array)-1):
            if array[j] > array[j+1]:
                array[j], array[j + 1] = array[j +1], array[j]
                was_swapped = True

        #if no swap happened in iteration -> already sorted (checks for every iteration)
        if was_swapped == False:
            break

    return array
