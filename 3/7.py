list1 = ["apple" , "apple" , "banana" , "btats" , "gwafa"]

def cleanlist(l):
    clean = []
    for i in l:
        if i not in clean:
            clean.append(i)
    return clean

print(cleanlist(list1))