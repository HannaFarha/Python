
for i in range(1,10,2):
    print(i)
while True:
        line = input("command:>")
        if line.startswith("#"):
            continue
        if line == "Done":
            break
        print(line)