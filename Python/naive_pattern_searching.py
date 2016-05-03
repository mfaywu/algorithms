def bubble_sort (ls):
    for items in range (len (ls) - 1, 0, -1):
        for i in range (items):
            if ls[i] > ls[i+1]:
                temp = ls[i]
                ls[i] = ls[i+1]
                ls[i+1] = temp

def naive_search (text, pattern): 
    i = 0
    j = 0
    found = False
    while (i < len(text)):
        if text[i] == pattern[j]:
            if j == len(pattern) - 1:
                return i - len(pattern) + 1
            j = j + 1
        i = i + 1
    return -1

text = input ("Please enter text: ")
pattern = input ("Please enter pattern: " )
found = naive_search (text, pattern)
print (found)
