#Rabin Karp Algorithm
#Common use: detecting plagiarism 
#High # of matches, nonexact matching

import math

base = 101

def hash(pattern):
    p_len = len(pattern)
    hash = 0.0
    for i in range (0, p_len):
        hash = hash + (ord(pattern[i]) * math.pow(base, p_len -1 - i))
    return hash

def rabin_karp_search (text, pattern):
    p_len = len(pattern)
    hash_pattern = hash(pattern)
    print ("hash of pattern is: %i" % (hash_pattern))
    hash_text = hash(text[0:p_len])
    print ("hash at i = 0 is: %i" % (hash_text))
    for i in range (0,  len(text)-p_len):
        if hash_text == hash_pattern:
            print("Matched hash at: %i" % (i))
            for j in range(0, p_len-1):
                if text[i+j] != pattern[j]:
                    print ("char not matched")
                    break
                if j == p_len-1:
                    print (i)
        hash_text = hash_text - hash(text[i:i+1]) + hash(text[i+p_len:i+p_len+1])

text = input ("Enter string text: ")
pattern = input ("Enter pattern to search for: ")
print (rabin_karp_search(text, pattern))


