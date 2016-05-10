#Minimum Cost Path
#Matrix cost[][]
#Min cost path from (0,0) to (m,n)

def min_cost_path (matrix, dest_x, dest_y):
    if dest_x == 0 and dest_y == 0: 
        return matrix[0][0]
    

matrix = input("Enter 2D Matrix: ")
dest_x = input("Enter destination x: ")
dest_y = input("Enter destination y: ")

