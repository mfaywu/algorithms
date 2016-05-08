#Rabin Karp Algorithm
#Common use: detecting plagiarism 
#High # of matches, nonexact matching

def rabin_karp_search (text, pattern):
    hash_pattern = hash(pattern)
    for i in range (0,  len(text) - len(pattern)):
        hash_text = hash(text[i:i+len(pattern)])
        if hash_text == hash_pattern:
            for j in range(0, len(pattern)):
                if text[i+j] != pattern[j]:
                    break
                print ("found at: "%d % (i))

text = input ("Enter string text: ")
pattern = input ("Enter pattern to search for: ")

