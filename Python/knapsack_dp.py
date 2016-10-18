#Knapsack problem using memoisation

def knapsack(values, weights, capacity, item):
    C = [[0 for x in range(item+1)] for x in range(item+1)]

    for i in range(item+1):
        for j in range(item+1):
            if 
