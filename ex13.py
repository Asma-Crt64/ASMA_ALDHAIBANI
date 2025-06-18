print("1. Add item\n2. Show list\n3. Remove item")
choice=int(input("Enter your choice: "))

shoppingList=["Fruits", "Pencil"]

if choice==1:
    item=input("Enter an item to be added: ")
    shoppingList.append(item)
    for items in shoppingList:
        print(items)
elif choice==2:
    for items in shoppingList:
        print(items)
else:
    item=input("Enter an item to be removed: ")
    shoppingList.remove(item)
    for items in shoppingList:
        print(items)
