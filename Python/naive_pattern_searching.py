def match_pattern(text, pattern):
    i = 0
    while i < len(text):
        if text[i] != pattern [i]:
            return False
        i = i + 1
    return True

def naive_search (text, pattern): 
    i = 0
    idx = []
    while i < (len(text) - len(pattern)):
        if text[i] == pattern[0]:
            if match_pattern(text[i:i+len(pattern)], pattern):
                idx.append(i)
        i = i+1
    return idx

text = input ("Please enter text: ")
pattern = input ("Please enter pattern: " )
found = naive_search (text, pattern)
print (found)
