import math 

import os
cwd = os.getcwd()
file = open(cwd + "moves.txt","r")
lines = file.readlines()
moves = [line.split() for line in lines]
moves = [[move[0], int(move[1])] for move in moves]

head, tail = ([0,0],[0,0])
visited = {(0,0):1}

#whenever the tail moves, we will increment the number of times it's visited that location
def logPos(tup):
    visited[tup] = visited.get(tup,0) + 1

#functions to cover what happens when head moves

# class knot:
#     def __init__(self, parent):
#         self.row = 0
#         self.col = 0
#         self.parent = parent
#         self.visited = []
#         self.child = None
#         self.id = parent.id + 1

#     def update(self):
#         if abs(self.parent.row - self.row) > 1:
#             self.row += [1,-1][self.row > self.parent.row]
#             if self.col != self.parent.col:
#                 self.col += [1,-1][self.col > self.parent.col]
#         if abs(self.parent.col - self.col) > 1:
#             self.col += [1,-1][self.col > self.parent.col]
#             if self.row != self.parent.row:
#                 self.row += [1,-1][self.row > self.parent.row]
#         self.child.update()





#moving up only updates the tail if the head is already one space above the tail; the tail always ends up directly below the head
def moveUp(head, tail):
    head[0] += 1
    if head[0] - tail[0] > 1:
        tail[0] = head[0]-1 
        tail[1] = head[1]
        logPos(tuple(tail))

def moveDown(head, tail):
    head[0] -= 1
    if head[0] - tail[0] < -1:
        tail[0] = head[0]+1
        tail[1] = head[1]
        logPos(tuple(tail))

def moveRight(head, tail):
    head[1] += 1
    if head[1] - tail[1] > 1:
        tail[0] = head[0]
        tail[1] = head[1] - 1
        logPos(tuple(tail))

def moveLeft(head, tail):
    head[1] -= 1
    if head[1] - tail[1] < -1:
        tail[0] = head[0]
        tail[1] = head[1] + 1
        logPos(tuple(tail))


    

##For Part 2, might need to add diagonal moves; since diagonal moves are possible as a result of a linear head move, propogation requires accomodating for your parent moving diagonally

def executeMove(move, head, tail):
    if move[0] == "U":
        for i in range(move[1]):
            moveUp(head,tail)
    if move[0] == "D":
        for i in range(move[1]):
            moveDown(head,tail)
    if move[0] == "L":
        for i in range(move[1]):
            moveLeft(head,tail)
    if move[0] == "R":
        for i in range(move[1]):
            moveRight(head,tail)
    
def run():
    for move in moves:
        executeMove(move, head, tail)
    print(len(visited))

# run()



#if we have the snake as a simple list of coordinates, we can propogate moves [-/+1,-/+1]down the list
def iterate(snake,step):
    snake[0][0] += step[0]
    snake[0][1] += step[1]
    for idx in range(len(snake) - 1):
        propagate(snake[idx],snake[idx + 1])

def propagate(parent, child):
    if abs(parent[0] - child[0]) > 1:
        child[0] += [1,-1][child[0] > parent[0]]
        if child[1] != parent[1]:
            child[1] += [1,-1][child[1] > parent[1]]
    if abs(parent[1] - child[1]) > 1:
        child[1] += [1,-1][child[1] > parent[1]]
        if child[0] != parent[0]:
            child[0] += [1,-1][child[0] > parent[0]]

def makeSnake(length):
    return [[0,0] for i in range(length)]

def parseMove(move):
    if move[0] == "U":
        return [[1,0] for i in range(move[1])]
    if move[0] == "D":
        return [[-1,0] for i in range(move[1])]
    if move[0] == "L":
        return [[0,-1] for i in range(move[1])]
    if move[0] == "R":
        return [[0,1] for i in range(move[1])]
def run2():
    snake = makeSnake(10)
    for move in moves:
        for step in parseMove(move):
            iterate(snake, step)
            logPos(tuple(snake[len(snake)-1]))
            if(len(visited) == 1): print(snake,move)
    print(len(visited))

run2()
    
