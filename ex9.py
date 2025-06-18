def findMax(myList):
    max=0
    for item in myList:
        if item >=max:
            max=item
    print(f"The max num is {max}.")


myList=[1, 2, 3, 4, 5, 6]
findMax(myList)
