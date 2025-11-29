numbers = [4,8,9]
n = len(numbers)
result = numbers.copy()
for i in range(n):
    for j in range(0, n-i-1):
        if result[j] > result[j+1]:
            result[j], result[j+1] = result[j+1], result[j]
print(result)