import os
cwd = os.getcwd()
file = open(cwd + "strategy.txt","r")

rounds = file.readlines()
splitrounds = []
for round in rounds:
    splitrounds.append(round.split())

score = 0

for round in splitrounds:
    game = "".join(round)
    if game == "AX":
        score += 3
    elif game == "AY":
        score += 4
    elif game == "AZ":
        score += 8
    elif game == "BX":
        score += 1
    elif game == "BY":
        score += 5
    elif game == "BZ":
        score += 9
    elif game == "CX":
        score += 2
    elif game == "CY":
        score += 6
    elif game == "CZ":
        score += 7
print(score)
    
    
        

