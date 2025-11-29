import random
import string

hexdecimal = "ABCDEF0123456789"
pairs = []
for i in range(6):
    pair = "".join(random.choices(hexdecimal, k=2))
    pairs.append(pair)

macaddress = ":".join(pairs)
print(macaddress)