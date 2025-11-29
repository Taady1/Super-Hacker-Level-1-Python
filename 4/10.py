def vowelsextract(word):
    vowels = "aeiou"
    new = ""
    for i in word:
        if i in vowels:
            new += i
    return new

word = input("enter a word : ")
print(vowelsextract(word))