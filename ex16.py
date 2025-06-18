def sortList(myList):
    for i in range(len(myList)):
        smallest = myList[i]
        for j in range(i+1, len(myList)):
            if smallest > myList[j]:
                smallest = myList[j]
                myList[i], myList[j] = myList[j], myList[i]
    print(myList)

myList = [3, 5, 7, 6, 1, 2, 4]
sortList(myList)
