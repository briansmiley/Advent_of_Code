import re
import time
file = open("/Users/briansmiley/Projects/Advent/Day11/monkeys.txt","r")
lines = file.readlines()

monkeys = []
for i in range(len(lines)//7 + 1):
    monkeys.append([lines[7 * i + j] for j in range(6)])

class monkeyClass:
    def __init__(self, monke):
        self.id = int(re.findall('\d+',monke[0])[0])
        self.items = [int(item) for item in re.findall('\d+',monke[1])]
        
        opString = re.search("(\w+) (\+|\*) (\w+)",monke[2]).groups()
        self.operand1 = opString[0]
        self.operator = opString[1]
        self.operand2 = opString[2]
        self.divisor = int(re.findall("\d+",monke[3])[0])
        self.trueTarget = int(re.findall("\d+",monke[4])[0])
        self.falseTarget = int(re.findall("\d+",monke[5])[0])
        self.inspected = 0
    
    def inspectItems(self, monkeys):
        for item in self.items:
            self.inspected += 1
            if self.operand1 == "old":
                x = item
            else:
                x = int(self.operand1)
            if self.operand2 == "old":
                y = item
            else:
                y = int(self.operand2)
            
            if self.operator == "*":
                z = x * y
            elif self.operator == "+":
                z = x + y
            z = z%9699690
            
            self.throw(monkeys, [self.falseTarget,self.trueTarget][z % self.divisor ==0], z)
        self.clearItems()
    def clearItems(self):
        self.items.clear()
    def catch(self, item):
        self.items.append(item)
    def throw(self, colony, target, item):
        colony[target].catch(item)


monkeys = [monkeyClass(monkey) for monkey in monkeys]

divisors = [monke.divisor for monke in monkeys]
product = 1
for divisor in divisors:
    product *= divisor

# monkeys[2].inspectItems(monkeys)
def runRounds(x):
    for i in range(x):
        # if i%200 == 0:
        #     print(i)
        # print(i, ": ", [monke.items for monke in monkeys])
        for monkey in monkeys:
            monkey.inspectItems(monkeys)
        # print(i, ": ", [monke.items for monke in monkeys])
startTime = time.time()
runRounds(10000)
inspectList = [[monke.id, monke.inspected] for monke in monkeys]
inspectList.sort(key = lambda x: x[1])
endTime = time.time()
print(inspectList[-2:][0][1]*inspectList[-2:][1][1]," calulated in ", endTime-startTime)
