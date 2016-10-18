'''
Implement an algorithm to print all valid (i.e., properly opened and closed) 
combinations of n pairs of parantheses.
'''

def parans(ls, left_count, right_count, str):
    if left_count == 0 and right_count == 0:
        ls.append(str)
    else:
        if left_count > 0:
            temp_str = str + '('
            parans(ls, left_count-1, right_count, temp_str)
        if right_count > left_count:
            temp_str = str + ')'
            parans(ls, left_count, right_count-1, temp_str)

def gen_parans(n):
    ls = []
    parans(ls, n, n, '')
    return ls

print gen_parans(3)


