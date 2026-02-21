print("Enter your text (Enter empty line to finish):")
lines = []

while True:
    line = input()
    if line == "":
        break
    lines.append(line.lstrip())


print("\nCleaned text:")
for line in lines:
    print(line)
