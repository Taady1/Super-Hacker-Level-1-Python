import random
import string

def randompassword(lenth):
    chars = string.ascii_letters + string.digits + string.punctuation
    password = "".join(random.choices(chars , k=lenth))
    return password

l = 12
print(f"password is : {randompassword(l)}")