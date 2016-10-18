'''
Given an infinite number of quarters, dimes, nickels,
and pennies, write code to calculate the number of 
ways of representing n cents.
'''

def makeChange(map, n):
    if n < 0: 
        map[n] = 0
        return 0
    elif n == 0:
        map[n] = 1
        return 1
    elif n in map:
        return map[n]
    else:
        map[n] = makeChange(map, n-25) + makeChange(map, n-10) + makeChange(map, n-5) + makeChange(map, n-1)
        return map[n]

print makeChange({}, 100)