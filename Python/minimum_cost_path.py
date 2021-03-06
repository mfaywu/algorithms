#Minimum Cost Path
#Matrix cost[][]
#Min cost path from (0,0) to (m,n)
import sys

def min_cost_path (matrix, x, y):
    if x < 0 or y < 0:
        return sys.maxsize
    if x == 0 and y == 0: 
        return matrix[0][0]
    else: 
        return matrix[x][y] + min (min_cost_path (matrix, x-1, y-1),
                                   min_cost_path (matrix, x-1, y),
                                   min_cost_path (matrix, x, y-1))

matrix = input("Enter 2D Matrix: ")
dest_x = input("Enter destination x: ")
dest_y = input("Enter destination y: ")
print (min_cost_path(matrix, dest_x, dest_y))
