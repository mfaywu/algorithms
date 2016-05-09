#Rabin Karp Algorithm
#Common use: detecting plagiarism 
#High # of matches, nonexact matching
#Uses Rabin Fingerprint for hash function

import math

base = 101

def hash(pattern):
    p_len = len(pattern)
    hash = 0.0
    for i in range (0, p_len):
        hash = hash + (ord(pattern[i]) * math.pow(base, p_len -1 - i))
    return hash

def rabin_karp_search (text, pattern):
    found = []
    p_len = len(pattern)
    hash_pattern = hash(pattern)
    hash_text = hash(text[0:p_len])
    for i in range (0,  len(text)-p_len+1):
        if hash_text == hash_pattern:
            for j in range(0, p_len):
                if text[i+j] != pattern[j]:
                    break
                if j == p_len-1:
                    found.append(i)
        if i+p_len < len(text):
            hash_text = (base * (hash_text - (ord(text[i]) * math.pow(base, p_len-1)))) + (ord(text[i+p_len]))
    return found
text = input ("Enter string text: ")
pattern = input ("Enter pattern to search for: ")
print (rabin_karp_search(text, pattern))
