for number in range(1, 101):
    if number < 2:
        print(f"{number} is not prime")
        continue
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            print(f"{number} is not prime")
            break
    else:
        print(f"{number} is prime")