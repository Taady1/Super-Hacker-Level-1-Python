password = input("Enter Password : ")
numbers = "1234567890"
schar = "@#$%!"
def strongpasswordcheck(p):
    if len(p) > 8 and any(char in schar for char in p) and any(char in numbers for char in p):
        print("Strong")
    else:
        print("Not Strong Enough")

strongpasswordcheck(password)