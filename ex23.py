# Count lines in a file (no error handling)
with open("myfile.txt") as f:
    print("Total lines:", len(f.readlines()))
