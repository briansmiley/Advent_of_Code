import re

import os
cwd = os.getcwd()
file = open(cwd + "terminal.txt","r")
log = file.readlines()
logTokenized = [line.split() for line in log]

#dir class representing any folders or files in the tree
#directories are created with defaul size 0; files are directories which will never be populated and have size assigned at creation
#directories' sizes are dynamically determined when getSize is run by recursively adding the size of all child directories and all file contents
class dir:
    def __init__(self, name, parent, size = 0):
        self.parent = parent
        self.name = name
        self.contents = {}
        self.size = size
    def mkdir(self, name):
        self.contents[name] = dir(name, self)
    def touch(self, name, size):
        self.contents[name] = file(name, self, size)
    def getSize(self):
        if self.size > 0: 
            return self.size
        else:
            return sum([item.getSize() for item in self.contents.values()])
class file:
    def __init__(self,name,parent,size):
        self.name = name
        self.size = size
        self.parent = parent
    def getSize(self):
        return self.size

#Basic testing
    # root = dir("/",None)
    # root.mkdir("Desktop")
    # root.contents["Desktop"].touch("Screenshot",400)
    # root.contents["Desktop"].touch("Screenshot2",300)
    # root.mkdir("Users")
    # root.contents["Users"].touch("Screenshot",1400)
    # root.contents["Users"].touch("Screenshot2",3400)

    # print([item.getSize() for item in root.contents.values()])
    # print(root.getSize())

#Populate the directories
root = dir("/",None)
cwd = None
for line in logTokenized:
    if line[0] == "$":
        if line[1] == "cd":
            if line[2] == "/":
                cwd = root
            elif line[2] == "..":
                cwd = cwd.parent
            else:
                if line[2] not in cwd.contents:
                    print("Error, changed to directory not established in a prior ls")
                    break
                else:
                    cwd = cwd.contents[line[2]]
        
        
    else:
        if re.match("\d+",line[0]):
            if not(line[1] in cwd.contents):
                cwd.touch(line[1],int(line[0]))
        elif line[0] == "dir":
            if not line[1] in cwd.contents:
                cwd.mkdir(line[1])

sizeList = []
def walkDown(dirs,directory):
    dirs.append((directory.name,directory.getSize()))
    for item in directory.contents.values():
        if type(item).__name__ == "dir":
            walkDown(dirs,item)

walkDown(sizeList,root)
# print(sum([folder[1] for folder in sizeList if folder[1] < 100000]))
# print(root.getSize())

totalSpace = 70000000
usedSpace = root.getSize()
neededSpace = 30000000
freeSpace = totalSpace-usedSpace
toClear = neededSpace-freeSpace
print(toClear)

victim = ["/",root.getSize()]
for directory in sizeList:
    if directory[1] >= toClear and directory[1] < victim[1]:
        victim = directory
print(victim)