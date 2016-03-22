#def heap_sort (ls):
#    for i in range (len(ls), -1, -1):
#        heapify (ls, len(ls), i)

#    for i in range (len(ls) - 1, 0, -1):
#        ls[0], ls[i] = ls[i], ls[0]
#        heapify (ls, i, 0)
    
#def heapify (ls, length, i):
#    root_idx = i
#    big_idx = i
#    left_idx = 2 * i + 1
#    right_idx = 2 * i + 2

#    if left_idx < length and ls[left_idx] > ls[root_idx]:
#        big_idx = left_idx
        
 #   if right_idx < length and ls[right_idx] > ls[big_idx]:
 #       big_idx = right_idx

  #  if big_idx != root_idx:
  #      ls[big_idx], ls[root_idx] = ls[root_idx], ls[big_idx]

   # heapify (ls, length, big_idx)

def heap_sort (ls):
    for i in range (0, len(ls)-1):
        heapify (ls, 0, i)
        print ls

def heapify (ls, first, last):
    child = last
    print "child is " + str(ls[last])

    if child % 2 == 0:
        root = (child - 2) / 2
        
    if (child - 1) % 2 == 0:
        root = (child - 1) / 2

    else:
        print "root is same"
        root = child
    
    print "root is " + str(ls[root])
        
    if root != child and ls[root] < ls[child]:
        print "swap" + str(ls[root]) + " with " + str(ls[child])
        ls[root], ls[child] = ls[child], ls[root]
        heapify (ls, first, root)

ls = input ("Please enter an array of numbers: ")
heap_sort(ls)
print ls
