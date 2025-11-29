word = "P@ssw0rd"
vowels = "aeiouy@0"
new = ""
for char in word:
    if char.lower() in vowels:
        new += "*"
    else:
        new += char
print(new)