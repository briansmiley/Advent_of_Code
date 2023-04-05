import os
cwd = os.getcwd()
file = open(cwd + "signal.txt","r")
lines = file.readlines()
instructions = [line.split() for line in lines]

#cycle and X respectively are stored in the first element of log
log = [[0,1],[]]
screen = [[] for i in range(6)]

def incrementCycle(i):
    for j in range(i):
        row = log[0][0]//40
        column = log[0][0]%40
        x = log[0][1]
        screen[row].append([".","#"][column in range(x-1,x+2)])
        log[0][0] += 1
        if ((log[0][0] - 20) % 40) == 0:
            log[1].append(log[0].copy())

def prodList(lis):
    i = 1
    for item in lis:
        i *= item
    return i

def processLine(line):
    if line[0] == "noop":
        incrementCycle(1)
    else:
        incrementCycle(2)
        log[0][1] += int(line[1])

def run1():
    for line in instructions:
        processLine(line)
    print(log)
    print(sum([prodList(i) for i in log[1]]))

def run2():
    for line in instructions:
        processLine(line)
    print("\n".join(["".join(line) for line in screen]))

run2()