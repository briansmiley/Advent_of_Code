file = open("/Users/briansmiley/Projects/Advent/Day3/packs.txt","r")

packs = file.readlines()

def priority(char):
    return ord(char)-[96,38][ord(char) < 96]

total = 0
letters = []

#part 1
# for pack in packs:
#     half = int(len(pack)/2)
#     comp1, comp2 = pack[:half], pack[half:]
#     found = False
#     for letter in comp1:
#         if not(found):
#             if letter in comp2:
#                 found = True
#                 total += priority(letter)
#                 letters.append((letter, priority(letter)))
# print(total)

#Part 2
total = 0
n = 0
badges = []
group = []
for pack in packs:
    group.append(pack)
    if len(group) == 3:
        found = False
        for char in group[0]:
            if (not(found) and char in group[1] and char in group[2]):
                found = True
                badges.append(char)
        group.clear()

total = 0
for badge in badges:
    total += priority(badge)

print(total)
