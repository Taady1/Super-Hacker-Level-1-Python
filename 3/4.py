text = input("Enter the Text : ")
char = list(text)
for i in set(char):
    print (f"{i} = {char.count(i)}")