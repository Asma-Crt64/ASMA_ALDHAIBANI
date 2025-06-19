# Part 1
counter = 0
list1 = []  
while counter <= 10:
    list1.append(counter * counter)  
    counter += 1

print(list1)

#Part 2
counter2 = 0
list2 = []  
while counter2 <= 20:
    if counter2%2==0:
        list2.append(counter2)  
    counter2 += 1

print(list2)
