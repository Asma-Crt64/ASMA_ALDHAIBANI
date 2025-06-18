def stringCount(word, letter):
    letterCount=0
    for letters in word:
        if letters == letter:
            letterCount+=1
    print(f"Letter {letter} is found {letterCount} times.")
    

word="ASMA"
letter="A"
stringCount(word, letter)
