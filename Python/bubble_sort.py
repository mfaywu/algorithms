def bubble_sort (ls):
    for items in range (len (ls) - 1, 0, -1):
        for i in range (items):
            if ls[i] > ls[i+1]:
                temp = ls[i]
                ls[i] = ls[i+1]
                ls[i+1] = temp

def bubble_sort_o (ls):
    swapped = False; 
    for items in range (len (ls) - 1, 0, -1):
        for i in range (items):
            if ls[i] > ls[i+1]:
                temp = ls[i]
                ls[i] = ls[i+1]
                ls[i+1] = temp
                swapped = True
        if swapped == False:
            break

ls = input ("Please enter array of numbers: ")
choice = input ("0 regular; 1 optimized: " )
if choice == 0:
    bubble_sort (ls)
else:
    bubble_sort_o (ls)
print (ls)
