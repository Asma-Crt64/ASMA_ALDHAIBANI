vowelCount=0

statment=input("Enter your statment: ")

for letter in statment:
   if letter == 'a' or letter == 'e' or letter == 'i' or letter == 'o' or letter == 'u':
        vowelCount+=1
        
print(f"The number of vowel letters is {vowelCount}.")
