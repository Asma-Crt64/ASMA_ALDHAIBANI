def nameFormatter(fullName):
    
    nameParts=fullName.split()

    firstName=nameParts[0]
    lastName=nameParts[-1]
    
    print(f"Your first name is {firstName} and your last name is {lastName}")
    
nameFormatter("John Doe")
nameFormatter("Mary Jane Smith")
