def selection_sort (array):
    for i in range (0, len(array)):
        min = i
        for j in range (i+1, len(array)):
            if array[min] > array[j]:
                min = j

        array[i], array[min] = array[min], array[i]
        
    return array

array = input ("Enter array: ")
print (selection_sort(array))
