'''
In the classic problem of the Towers of Hanoi, you have 3 towers and N disks of different
sizes which can slide onto any towers. The puzzle starts with disks sorted in ascending 
order of size from top to bottom. You have the following constraints:
(1) Only one disk can be moved at a time.
(2) A disk is slid off the top of one tower onto another tower.
(3) A disk cannot be placed on top of a smaller disk.

Write a program to move the disks from the first tower to the last using Stacks.
'''

def moveDisks (n, orig, dest, buff):
    if (n > 0):
        moveDisks(n-1, orig, buff, dest)
        moveTop(orig, dest)
        moveDisks(n-1, buff, dest, orig)

def moveTop(orig, dest):
    item = orig.pop()
    dest.append(item)

orig = [1, 2, 3, 4, 5]
buff = []
dest = []

moveDisks(5, orig, dest, buff)
print dest
