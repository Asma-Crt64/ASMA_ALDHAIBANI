class BookCont:
    name = ""
    phone = ""
    
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone
    
    def addCont(self, BookContList, name, phone):
        BookContList.append(BookCont(name, phone)) 
    
    def searchByName(self, name, BookContList):
        for contact in BookContList:
            if contact.name == name:  
                print(contact.phone)
                return
        print("Contact not found")
    
    def displyList(self, BookContList):
        for contact in BookContList:
            print(f"{contact.name}: {contact.phone}")

print("1. Add new contact\n2. Search by name\n3. Display")
choice = int(input("Enter your choice: "))

b1 = BookCont("Bob", "067835317")
b2 = BookCont("Nana", "5673738383")
BookContList = [b1, b2]

if choice == 1:
    name = input("Enter name: ")
    phone = input("Enter phone: ")
    BookCont("", "").addCont(BookContList, name, phone)  
elif choice == 2:
    name = input("Enter name to search: ")
    BookCont("", "").searchByName(name, BookContList)
else:
    BookCont("", "").displyList(BookContList)








    
