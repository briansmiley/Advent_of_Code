import math

import os
cwd = os.getcwd()
file = open(cwd + "forest.txt","r")

grid = [line.strip() for line in file.readlines()]
#takes a tree's coordinates and returns whether it is visible from any direction
def isVisible(tree,forest):
    #if on edge, true
    cols = len(grid[0])
    rows = len(grid)
    if tree[0] in [0,rows-1] or tree[1] in [0,cols-1]:
        return True
    else:
        visible = [True, True, True, True]
        height = forest[tree[0]][tree[1]]
        #check trees to north, from [0,col] to [row-1,col]
        for row in range(0,tree[0]):
            if forest[row][tree[1]] >= height:
                visible[0] = False
                break
        #check trees to south from row+1 to bottom
        for row in range(tree[0]+1,rows):
            if forest[row][tree[1]] >= height:
                visible[2] = False
                break
        #check trees to west from 0 to col-1
        for col in range(0,tree[1]):
            if forest[tree[0]][col] >= height:
                visible[3] = False
                break
        #check trees to east from col+1 to 99
        for col in range(tree[1]+1,cols):
            if forest[tree[0]][col] >= height:
                visible[1] = False
                break
    if any(visible): print(tree)
    return any(visible)

def scenicScore(tree,forest):
    cols = len(forest[0])
    rows = len(forest)
    score = [0,0,0,0]
    height = forest[tree[0]][tree[1]]
    #check north
    x = tree[0]
    while x > 0:
        x -= 1
        score[0] += 1
        if forest[x][tree[1]] >= height:
            break
    
    #check east
    y = tree[1]
    while y < cols -1:
        y += 1
        score [1] += 1
        if forest[tree[0]][y] >= height:
            break

    #check south
    x = tree[0]
    while x < rows-1:
        x += 1
        score [2] += 1
        if forest[x][tree[1]] >= height:
            break

    #check west
    y = tree[1]
    while y > 0:
        y -= 1
        score [3] += 1
        if forest[tree[0]][y] >= height:
            break

    print(tree, score)
    return math.prod(score)


def countVisible():
    count = 0
    print(grid)
    for x in range(len(grid)):
        for y in range(len(grid[0])):
            count += isVisible([x,y],grid)
    print(count)

def maxScenic():
    most = 0
    for x in range(len(grid)):
        for y in range(len(grid[0])):
            most = max(most,scenicScore([x,y],grid))
    print(most)

maxScenic()