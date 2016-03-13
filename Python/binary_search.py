# Python provides bisect module

def binary_search_i (ls, item):
    first = 0
    last = len (ls) - 1
    found = False

    while first <= last and not found:
        midpoint = (first + last)//2
        if ls[midpoint] == item:
            found = True
        else:
            if item < ls[midpoint]:
                last = midpoint - 1
            else:
                first = midpoint + 1
                
    return found

def binary_search_r (ls, item):
    first = 0
    last = len (ls) - 1
    if first == last:
        return False
    midpoint = (first + last)//2
    
    if ls[midpoint] == item:
        return True
    else:
        if item < ls[midpoint]:
            return binary_search_r (ls[:midpoint], item)
        else:
            return binary_search_r (ls[midpoint+1:], item)
    

ls = input ("Please enter sorted array of numbers: ")
item = input ("Please enter number you are searching for: ")
r = input ("0 for recursive; 1 for iterative: ")

if r == 0:
    if binary_search_r (ls, item):
        print (str(item) + " found.")
    else:
        print (str(item) + " not found.")
else:
    if binary_search_i (ls, item):
        print (str(item) + " found.")
    else:
        print (str(item) + " not found.")
