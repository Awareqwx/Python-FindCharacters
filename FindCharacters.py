def findCharacters(arr, char):
    arr2 = []
    for i in arr:
        if i.find(char) != -1:
            arr2.append(i)
    return arr2

print findCharacters(['hello','world','my','name','is','Anna'], "o")