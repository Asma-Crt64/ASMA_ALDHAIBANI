def dupFinder(myList):
    item=0
    for i in range(len(myList)):
        smallest = myList[i]
        for j in range(i+1, len(myList)):
            if myList[i]==myList[j]:
                item=myList[i]
    print(f"The {item} is duplicated.")
    

myList=[1, 2, 2, 4, 5]
dupFinder(myList)
