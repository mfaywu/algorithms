def special(lst):
    ones = 0
    twos = 0
    for x in lst:
        twos |= ones & x
        ones ^= x
        not_threes = ~(ones & twos)
        ones &= not_threes
        twos &= not_threes
    return ones

ls = [1, 1, 3, 2, 3, 4, 4, 5, 2, 1, 3, 2, 4]

print special(ls)