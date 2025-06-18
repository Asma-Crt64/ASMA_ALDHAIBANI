password=input("Enter your password: ")

passLength=0

for char in password:
    passLength+=1
    
if passLength>8:
    print("Your password enterd is longer than 8 char!")
