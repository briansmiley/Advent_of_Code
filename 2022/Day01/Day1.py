import os

cwd = os.getcwd()
file = open(cwd + "/cals.txt", "r")
lines = file.readlines()

totals = []
current = 0

for line in lines:
    if line == "\n":
        totals.append(current)
        current = 0
    else:
        current += int(line)

totals.sort(reverse = True)
print (sum(totals[0:3]))
