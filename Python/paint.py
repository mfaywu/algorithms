'''
Implement the 'paint fill' function that one might 
see on many image editing programs. That is, given a 
screen(represented by a two-d array of colours), a point,
and a new colour, fill in the surrounding area until
the colour changes from the original colour.
''' 

def fill(arr, pt, new_c, old_c=None):
    print pt
    row = pt['row']
    col = pt['col']
    if row < len(arr) and row >= 0 and col < len(arr[0]) and col >= 0:
        if old_c is None:
            old_c = arr[row][col]
        if (arr[row][col] == old_c):
            arr[row][col] = new_c
            fill(arr, {'row': row-1, 'col': col}, new_c, old_c)
            fill(arr, {'row': row, 'col': col-1}, new_c, old_c)
            fill(arr, {'row': row+1, 'col': col}, new_c, old_c)
            fill(arr, {'row': row, 'col': col+1}, new_c, old_c)

arr = [
    [0, 0, 0, 0, 0],
    [0, 1, 1, 1, 1],
    [0, 1, 1, 0, 0],
    [0, 1, 0, 0, 1],
    [0, 0, 0, 1, 0]
]
pt = {'row': 1, 'col': 1}
new_c = 2

fill(arr, pt, new_c)
for row in arr:
    print row