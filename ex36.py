#Part 1
import random

i=0
myList=[]
while(i<10):
    randNum=random.randint(1, 90)
    myList.append(randNum)
    print(randNum)
    i+=1

#Part 2
max = 0
for item in myList:
    if max<=item:
        max=item
    
print(f"The maximum random number is {max}.")
        
        
#Part 3
doubles_count = 0

for _ in range(100):
    die1 = random.randint(1, 6)
    die2 = random.randint(1, 6)
    if die1 == die2:
        doubles_count += 1

print(f"\nDoubles appeared {doubles_count} times in 100 rolls.")

