def function(myList):
    result=0
    try:
        index=int(input("Enter ythe index: "))
        print(f"{myList[index]}")
    except:
        print("Invalid index input!")



myList=[1, 2, 3, 4, 5, 6, 7]
function(myList)
