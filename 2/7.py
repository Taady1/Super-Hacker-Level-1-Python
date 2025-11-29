import random
random_number = random.randint(1,5)
number = int(input("Guess the Number :"))
if number == random_number :
    print("Correct")
else:
    print(f"wrong it was {random_number}")