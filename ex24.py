# Save friends to file (overwrites existing file)
friends = ["Ali", "Sam", "Mia"]
with open("friends.txt", "w") as f:
    f.write("\n".join(friends))
print("Done!")
