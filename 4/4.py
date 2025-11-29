def validipcheck(ip):
    partschecked = 0
    splitter = ip.split(".")
    if len(splitter) == 4:
        for i in range(4):
            part = int(splitter[i])
            if part >= 0 and part < 256:
               partschecked = partschecked +1
            else:
                print("Not Valid")
    else:
        print("Not Valid")        
    if partschecked == 4:
        print("valid")
    else:
        print("Not Valid")

ip = input("Enter ip : ")
validipcheck(ip)