number = 0
number_format = f"{number:04d}"
for i in range(9999):
    number += 1
    number_format = f"{number:04d}"
    print(number_format)