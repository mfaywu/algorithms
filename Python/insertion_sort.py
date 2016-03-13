def insertion_sort (ls):
    for i in range (1, len(ls)):
        curr = ls[i]
        j = i - 1
        while ls[j] > curr and j >= 0:
            ls[j+1] = ls[j]
            j = j - 1
        ls[j+1] = curr

ls = input ("Please enter array of numbers: " )
insertion_sort (ls)
print (ls)
