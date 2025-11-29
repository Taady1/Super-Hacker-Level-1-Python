password = "yes"
correct = False
while correct != True:
    pas = input("Enter Password :")
    if pas == password :
        print("Done")
        break
    else:
        print("Try again")