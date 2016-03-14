def merge_sort (ls):
    if len (ls) <= 1: 
        return ls
    midpoint = len (ls) // 2
    ls_a = merge_sort (ls[:midpoint])
    ls_b = merge_sort (ls[midpoint:len(ls)])
    return merge (ls_a, ls_b)

def merge (ls_a, ls_b): 
    ls_c = []
    i = 0
    j = 0
    while i < len(ls_a) and j < len(ls_b):
        if ls_a[i] <= ls_b[j]:
            ls_c.append(ls_a[i])
            i = i + 1
        else:
            ls_c.append(ls_b[j])
            j = j + 1
    while i < len(ls_a):
        ls_c.append(ls_a[i])
        i = i + 1
    while j < len(ls_b):
        ls_c.append (ls_b[j])
        j = j+1
    return ls_c

ls = input ("Please enter array of numbers: ")
print merge_sort (ls)
