myList=[1, 2, 4, 5, 9, 90, 4, 10]

sum =0

for i in range(len(myList)):
   sum= myList[i]+sum
print(f"The sum is {sum}.")


avg=sum/(len(myList))
print(f"The avg is {avg}.")

abvAvgCount=0

for i in range(len(myList)):
    if myList[i]>avg:
        abvAvgCount+=1
print(f"There are {abvAvgCount} numbers above avg.")
