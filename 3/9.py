list1 = ["btats" , "ahmed" , "mohtady" , "abotreka"]
def tallestword(l):
    n = len(l)
    tallest = ""
    for i in range(n):
        if len(tallest) <= len(l[i]):
            tallest = l[i]
    return tallest

print(tallestword(list1))