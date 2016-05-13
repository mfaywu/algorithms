#Knapsack problem

def knapsack (values, weights, capacity, item):
    if item < 0 or capacity == 0: 
        return 0
    else: 
        return max (values[item] + knapsack(values, weights, capacity - weights[item], item-1), knapsack(values, weights, capacity, item-1))

values = input ("Enter array of values: ")
weights = input ("Enter array of weights: ")
capacity = input ("Enter capacity: ")
print (knapsack (values, weights, capacity, len(values) - 1))
