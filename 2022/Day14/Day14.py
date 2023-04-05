import os
import time

cwd = os.getcwd()

file = open(cwd + "/testcave.txt","r")
lines = file.readlines()
#get the coordinate pairs without arrows "1,2 -> 3,4" ---> "1,2","3,4"
lines = [line.split(" -> ") for line in lines]
lines = [[coord.split(',') for coord in line] for line in lines]
lines = [[[int(coord) for coord in pair] for pair in line] for line in lines]

xMax,yMax = 0,0
xMin,yMin = 10000,100000
for line in lines:
    xMax = max(xMax,max([max(pair[0],xMax) for pair in line]))
    yMax = max(yMax,max([max(pair[1],yMax) for pair in line]))
    xMin = min(xMin,min([min(pair[0],xMin) for pair in line]))
    yMin = 0
xMin-=1

#for part 2
yMax += 2
xMin = 498-yMax
xMax = 502+yMax
print(f'[{xMin},{xMax}], [{yMin},{yMax}]')
#normalize data to move data to 0
for line in lines:
    for pair in line:
        pair[0] -= xMin
        pair[1] -= yMin 

cave = [['.'  for i in range(xMax - xMin + 1)] for j in range(yMax-yMin + 1)]
cave[yMax] = ["#" for i in cave[yMax]]
cave[0][500-xMin]='+'
def printCave(cave):
    print("\n".join(["".join(i) for i in cave]))
def writeRocks(pair,cave):
    x1,x2,y1,y2 = pair[0][0],pair[1][0],pair[0][1],pair[1][1]
    for y in range(min(y1,y2),max(y1,y2)+1):
        cave[y][x1] = '#'
    for x in range(min(x1,x2),max(x1,x2)+1):
        cave[y1][x] = '#'

def drawCave(cave,map):
    for line in map:
        for idx in range(1,len(line)):
            writeRocks([line[idx-1],line[idx]],cave)

#returns L/D/R if grain falls left/down/right, returns S if it stays where it is
def fall(cave,sand):
    x,y = sand[1],sand[0]
    if y == len(cave)-1:
        sand[2] = True
        return sand
    if (y + 1) < len(cave) and cave[y+1][x] == ".":
        cave[y][x] = "."
        cave[y+1][x] = 'o'
        sand = [y+1,x,False]
        return sand
    elif x > 0 and cave[y+1][x-1] == '.':
        cave[y][x] = '.'
        cave[y+1][x-1] = 'o'
        sand = [y+1,x-1,False]
        return sand
    elif x < len(cave[0])-1 and cave[y+1][x+1] == '.':
        cave[y][x] = '.'
        cave[y+1][x+1] = 'o'
        sand = [y+1,x+1,False]
        return sand
    cave[y][x] = 'o'
    sand[2]=True
    return sand

drawCave(cave,lines)
printCave(cave)
sand=[0,500-xMin,False]
   
while sand[0] < len(cave) - 1:
    sand=[0,500-xMin,False]
    sand = fall(cave,sand)
    if sand[2]:
        break
    while not sand[2]:
        # print(sand)
        sand = fall(cave,sand)

        printCave(cave)
        time.sleep(.03)
# print(xMin,xMax)
printCave(cave)
print(sum([row.count('o') for row in cave[:-1]]))

