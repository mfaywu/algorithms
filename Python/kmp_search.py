def build_table(word):
    T = [-1, 0]
    pos = 2
    matches = False
    
    while pos < len(word):
        if word[pos] == word[T[pos-1]+1]:
            T.append(T[pos-1] + 1)
            matches = True
        elif matches == True and T[pos-1] > 0:
            T.append(T[pos-1] + 1)
            matches = False
        else: 
            T.append(0)
            matches = False
        pos = pos + 1
    print T
    return T

def kmp(search_string, word):
    m = 0
    i = 0
    T = build_table(word)

    while m + i < len(search_string):
        if word[i] == search_string[m+i]:
            if i == len(word) - 1:
                return m
            i = i + 1
        else:
            if T[i] > -1:
                m = m + i - T[i]
                i = T[i]
            else:
                m = m + i - T[i]
                i = 0
    return -1

search_string = input ("Enter search string: ")
word = input ("Enter string to find: ")
print (kmp(search_string, word))
