myList="A statment given statment given"

wordOneCounter=0
wordTwoCounter=0
for word in myList.split():
    if word == "statment":
        wordOneCounter+=1
    if word == "given":
        wordTwoCounter+=1

print(f"The word Statment has appeared {wordOneCounter} times.")

print(f"The word Given has appeared {wordTwoCounter} times.")
