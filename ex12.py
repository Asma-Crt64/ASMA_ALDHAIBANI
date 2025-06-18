import random

randInt=random.randint(1, 5)

userRand=int(input("Enter your guess: "))

while userRand != randInt:
    if userRand>randInt:
        print("Higher!")
    else:
        print("Lower!")
    
    userRand=int(input("Enter your guess: "))
print("Your guess is right!")
