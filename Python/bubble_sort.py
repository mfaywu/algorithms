def bubble_sort (ls):
    for items in range (len (ls) - 1, 0, -1):
        for i in range (items):
            if ls[i] > ls[i+1]:
                temp = ls[i]
                ls[i] = ls[i+1]
                ls[i+1] = temp

# TODO def bubble_sort_short (ls):

ls = input ("Please enter array of numbers: ")
bubble_sort (ls)
print (ls)
