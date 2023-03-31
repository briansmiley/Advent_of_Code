import re

file = open("/Users/briansmiley/Projects/Advent/Day5/crates.txt","r")

stacks = [list("TRDHQNPB"),list("VTJBGW"),list("QMVSDHRN"),list("CMNZP"),list("BZD"),list("ZWCV"),list("SLQVCNZG"),list("VNDMJGL"),list("GCZFMPT")]

def shift (arrs, num, fr, to):
    temp = arrs[fr][:num]
    arrs[fr] = arrs[fr][num:]
    # temp.reverse()
    arrs[to] = temp + arrs[to]

steps = file.readlines()
moves = [[int(num) for num in re.findall('\d+',step)] for step in steps]

# testStacks = [list("NZ"),list("DCM"),list("P")]
# testSteps = ["move 1 from 2 to 1","move 3 from 1 to 3","move 2 from 2 to 1","move 1 from 1 to 2"]
# testMoves = [[int(num) for num in re.findall('\d+',step)] for step in testSteps]

# for move in testMoves:
#     print(testStacks)
#     shift(testStacks,move[0],move[1]-1,move[2]-1)

for move in moves:
    shift(stacks,move[0],move[1]-1,move[2]-1)


print(["".join(stack[0]) for stack in stacks])

# print("".join([stack[0] for stack in testStacks]))
# print(stacks)