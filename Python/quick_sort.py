def quick_sort (ls, first, last):
    if first < last: 
        pivot = partition (ls, first, last)
        quick_sort (ls, first, pivot)
        quick_sort (ls, pivot + 1, last)

def partition (ls, first, last):
    pivot = ls[last]
    i = first - 1

    for i in range (first, last):
        if ls[i] <= pivot:
            j = j + 1
            arr[j],arr[i] = arr[i],arr[j]
    arr[j+1],arr[last] = arr[last], arr[j+1]
    return j+1

ls = input ("Please enter array of unsorted numbers: ")
quick_sort (ls)
print (ls)
