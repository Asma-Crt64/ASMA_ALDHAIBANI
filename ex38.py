import random
def guessingGame():
    guessCount=1
    bestScore=0
    randInt=random.randint(1, 5)

    userRand=int(input("Enter your guess: "))

    while userRand != randInt:
        if userRand>randInt:
            print("Higher!")
        else:
            print("Lower!")
        guessCount+=1
        userRand=int(input("Enter your guess: "))
    if bestScore<=guessCount:
        bestScore=guessCount
    print(f"Your total guesses is {guessCount} and your best score is {bestScore}.")
    return 0
choice="yes"

while choice == "yes":
    if guessingGame()==0:      
        print("Your guess is right!")
    choice=input("Would you like to play again?")
    if choice == "yes":
        guessingGame()

