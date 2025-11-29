import socket

def gethostbyname(name):
    host = socket.gethostbyname(name)
    return host
    
hostname = input("host name : ")
print(gethostbyname(hostname))