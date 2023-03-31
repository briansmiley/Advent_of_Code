import ast
from itertools import zip_longest
from functools import cmp_to_key

file = open("/Users/briansmiley/Projects/Advent/Day13/packets.txt","r")
lines = [line.strip() for line in file.readlines()]
packets = []
for i in range(len(lines)//3 + 1):
    packets.append([ast.literal_eval(x) for x in lines[3*i:3*i+2]])
# print(len(packets))
#returns true if pair is ordered correctly, false otherwise
def compare(left,right):
    
    for l,r in zip_longest(left,right):
        if l == None: return 1
        if r == None: return -1

        if isinstance(l, int) and isinstance(r, int):
            if l < r: return 1
            if r < l: return -1
        
        else:
            if isinstance(l,int): l = [l]
            if isinstance(r,int): r = [r]
        
            sub = compare(l,r)
            if sub in [1,-1]: return sub
    return 0
    
ordered = []
for idx,pair in enumerate(packets,1):
    if compare(pair[0],pair[1]) == 1: ordered.append(idx)
    # if pair[0]==pair[1]: print('match')
# print(sum(ordered))
# print(f'{packets[0][0]}\n\n{packets[0][1]}\n\n{packets[-1][0]}\n\n{packets[-1][1]}\n\n')'


allPacks = [[[2]],[[6]]]
for packet in packets:
    allPacks.append(packet[0])
    allPacks.append(packet[1])



# print(len(allPacks))
a = sorted(allPacks,key = cmp_to_key(compare))
a.reverse()
for i,pack in enumerate(a,1):
    if pack ==[[2]]:
        print(i)
        i1 = i
    if pack ==[[6]]:
        print(i)
        i2=i
print(i1*i2)