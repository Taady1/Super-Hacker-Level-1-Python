num = 0
for i in range(100):
    num += 1
    if num % 4 == 0:
        skip = True       
    else:
        print (num)