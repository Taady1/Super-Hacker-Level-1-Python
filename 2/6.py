password = "log"
for i in range(1,4):
    print(f"try number {i} out of 3")
    enter_password = input("Enter password : ")
    if password == enter_password :
        print ("Done")
        break
    elif i<3:
        print("Try again")
    elif i == 3 :
        print("bye bye")