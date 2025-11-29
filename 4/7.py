def xor(t,k):
    xored = []
    for i in range(len(t)):
        tord = ord(t[i])
        kord = ord(k[i % len(k)])
        xoredres = tord ^ kord
        xored.append(chr(xoredres))
    
    return "".join(xored)

t = input("text : ")
k = input("key : ")
print(xor(t,k))