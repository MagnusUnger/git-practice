import threading

from mergesort      import mergee_sort
from bubblesort     import bublee_sort
from insertionsort  import insertionee_sort


array_example1  = [3,9,5,4,6,7,2,1]
array_example2  = [15,17,16,14,18,12,11,19]
array_example3  = [28,24,21,25,27,29,23,22]


def sort1(array, delay=3):
    sorted_array    = bublee_sort(array)
    print(sorted_array)

def sort2(array, delay=3):
    sorted_array    = insertionee_sort(array)
    print(sorted_array)

def sort3(array, delay=3):
    sorted_array    = mergee_sort(array)
    print(sorted_array)

bublee_thread       = threading.Thread(target=sort1, args=(array_example1,), kwargs={"delay":3})
insertionee_thread  = threading.Thread(target=sort2, args=(array_example2,), kwargs={"delay": 3})
mergee_thread       = threading.Thread(target=sort3, args=(array_example3,), kwargs={"delay": 3})

bublee_thread.start()
insertionee_thread.start()
mergee_thread.start()


bublee_thread.join()
insertionee_thread.join()
mergee_thread.join()
