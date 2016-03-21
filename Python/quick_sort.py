def quick_sort (ls, first, last):
    if first < last: 
        pivot = partition (ls, first, last)
        quick_sort (ls, first, pivot)
        quick_sort (ls, pivot + 1, last)

def partition (ls, first, last):
    

ls = input ("Please enter array of unsorted numbers: ")
quick_sort (ls)
print (ls)
