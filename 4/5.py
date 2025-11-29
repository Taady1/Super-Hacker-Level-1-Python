import hashlib
def hashing(data):
    hash = hashlib.new("md5")
    datatohash = data.encode("utf-8")
    hash.update(datatohash)
    hex = hash.hexdigest()
    return hex

data = input("Enter data you want to hash : ")
print(hashing(data))