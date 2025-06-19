#   Part1

names = ["Alice", "Bob", "Charlie", "Diana"]
sorted_names = sorted(names, key=lambda x: len(x))
print(sorted_names)  


#   Part2
numbers = [5, -2, 0, 12, -7, 3]
positive = list(filter(lambda x: x > 0, numbers))
print(positive)  
