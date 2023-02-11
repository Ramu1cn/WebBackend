with open("random.txt", "r") as f:
    lines = f.readlines()
    for line in lines:
        if line.__contains__("random"):
            print(line)
