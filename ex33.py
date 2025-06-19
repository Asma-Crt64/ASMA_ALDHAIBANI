myListOne = [1, 2, 3, 4, 5, 6, 7, 8]
myListTwo = [0, 1, 2, 3, 90, 61, 44, 9]

print("Numbers in both sets:")
for num in myListOne:
    if num in myListTwo:
        print(num)
 
print("\nNumbers not in both sets:")
for num in myListOne:
    if num not in myListTwo:
        print(num)
for num in myListTwo:
    if num not in myListOne:
        print(num)  
