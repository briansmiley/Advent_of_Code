import sys
import time 

print(sys.setrecursionlimit(2000))

import os
cwd = os.getcwd()
file = open(cwd + "grid.txt","r")
rows = [line.strip() for line in file.readlines()]

class Node:
    def __init__(self,height, x, y):
        self.x = x
        self.y = y
        if height == 'S':
            self.height = 0
        elif height == 'E':
            self.height = 25
        else:
            self.height = ord(height)-97

        self.edges = []
        self.revEdges= []
        self.distance = -1
        self.backDistance = -1
    def setEdge(self, space):
        self.edges.append(space)
    def setRevEdge(self,space):
        self.revEdges.append(space)
    def setDistance(self, distance):
        self.distance = distance
    def printEdges(self):
        print([[edge.x, edge.y, edge.height] for edge in self.edges])

def buildGraph(map):
    for row in map:
        for node in row:
            neighbors = []
            if node.x > 0:
                neighbors.append(map[node.y][node.x - 1])
            if node.x < len(row) - 1:
                neighbors.append(map[node.y][node.x + 1])
            if node.y > 0:
                neighbors.append(map[node.y - 1][node.x])
            if node.y < len(map) - 1:
                neighbors.append(map[node.y + 1][node.x])
            
            for neighbor in neighbors:
                if neighbor.height <= node.height + 1:
                    node.setEdge(neighbor)
                if neighbor.height >= node.height - 1:
                    node.setRevEdge(neighbor)
    
S, E = [0,0], [0,0]
for y, row in enumerate(rows):
    for x,cell in enumerate(row):
        if cell == "S":
            S = [x,y]
        if cell == "E":
            E = [x,y]

map = [[Node(node, x, i) for x, node in enumerate(rows[i])] for i in range(len(rows))]
start = map[S[1]][S[0]]
end = map[E[1]][E[0]]

buildGraph(map)

def traverse(node, graph, distance):
    if node.distance == -1 or node.distance > distance + 1:
        node.distance = distance + 1
        for child in node.edges:
            traverse(child,graph,node.distance)

def backTraverse(node, graph, backDistance):
    if node.backDistance == -1 or node.backDistance > backDistance + 1:
        node.backDistance = backDistance + 1
        for child in node.revEdges:
            backTraverse(child, graph, node.backDistance)

startTime = time.time()
# traverse(start,map,-1)
backTraverse(end,map,-1)
print(time.time()-startTime)

newLength = start.backDistance
for row in map:
    for node in row:
        if node.height == 0 and node.backDistance > -1:
            newLength = min(newLength,node.backDistance)
print(newLength)