while True:
    line = input("command:>")
    if line.startswith("#"):
        continue
    if line=="Done":
        break
    print(line)