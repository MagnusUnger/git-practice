import threading

from mergesort      import mergee_sort
from bubblesort     import bublee_sort
from insertionsort  import insertionee_sort

list_example    = [3,9,5,4,6,7,2,1]
functions       = [mergee_sort, bublee_sort, insertionee_sort]                  #LoL, I didnt know one could store functions in a list

#Professional function name xd
def cheeseburger(passed_list: list[int], parsed_functions: list[str]):
    
    #this one ive seen once and wanted to try
    def inside(func_name, delay=3):
        sorted_list = func_name(passed_list.copy())     #didnt think of the "threads accessing the same list" problem at first
        print(sorted_list)

    threads_created= []
    #iterating over imported functions
    for element in parsed_functions:
        thread_object   = threading.Thread(target=inside, args=(element,), kwargs={"delay": 3})     #then pass func / element in inside
        threads_created.append(thread_object)       #store created thread object

    for element in threads_created:     #starting them ...
        element.start()

    for element in threads_created:     #joining them ...
        element.join()

cheeseburger(list_example, functions)
