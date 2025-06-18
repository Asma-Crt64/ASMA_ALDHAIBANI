statment="This is my statment, we need to count a word. A word!"
word ="word"

wordCount=0

for words in statment.split():
    if word==words.strip(".,!"):
        wordCount+=1
        
print(f"The word {word} has appeared {wordCount} times.")
