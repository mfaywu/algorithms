#Write a method to compute all permutations of a string of unique characters

str = ["a", "b", "c"]

def permutations(str):
    if len(str) == 1:
        return [str]
    elif len(str) > 1:
        top = str.pop() #'b'
        str = permutations(str) 
        temp = []
        for item in str: #['a']
            for i in range(0, len(item)+1):
                temp_item = []
                for j in item:
                    temp_item.append(j)
                temp_item.insert(i, top)  
                temp.append(temp_item) 
                
        return temp
                
                
print permutations(str)
