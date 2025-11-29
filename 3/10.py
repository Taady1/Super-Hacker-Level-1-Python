list1 = {
    "Mohtady": "mahmoud",
    "omar": "wikii",
    "ali": "mounir"
}
def showname(name):
    if name in list1:
        print(list1[name])
    else:
        print("Not Found")
        
entername = input("Enter Name : ") 
showname(entername)