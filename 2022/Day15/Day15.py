import re

file = open("/Users/briansmiley/Projects/Advent/Day15/readings.txt","r")
lines = file.readlines()
data = [[int(num) for num in re.findall("\d+",line)] for line in lines]
pairedData = [[[datum[0],datum[1]],[datum[2],datum[3]]] for datum in data]
# print("\n".join([",".join([str(num) for num in line]) for line in data]))
checkRow = 2000000

class Point:
    def __init__(self,coords):
        self.x = coords[0]
        self.y = coords[1]
    def reverse(self):
        a = self.x
        self.x = self.y
        self.y = a
    def distance(self,p2):
        return abs(self.x -p2.x) + abs(self.y - p2.y)
    def __repr__(self):
        return f"[{self.x},{self.y}]"
class Pair:
    def __init__(self,sensor,beacon):
        self.beacon = Point(beacon)
        self.sensor = Point(sensor)
    def radius(self):
        return abs(self.sensor.distance(self.beacon))
    def __repr__(self):
        return(f'Sensor: {self.sensor} Beacon: {self.beacon}')
pairs = [Pair(pair[0],pair[1]) for pair in pairedData]
# print("\n".join([str(pair) for pair in pairs]))

xVals, yVals = [],[]
for pair in pairs:
    xVals.extend([pair.sensor.x,pair.beacon.x])
    yVals.extend([pair.sensor.y, pair.beacon.y])
xMin, xMax, yMin, yMax = min(xVals),max(xVals),min(yVals),max(yVals)

class Interval:
    def __init__(self,a,b):
        self.lower = a
        self.upper = b
        self.span = [a,b]
        self.size = abs(a-b) + 1
        self.range = range(a,b+1)
    #returns bool for whether
    def overlaps(self,other):
        if self.lower in range(other.lower,other.upper+1) or other.lower in range(self.lower,self.upper+1):
            return True
        return False
    #returns a new Interval that is the Union of self and other
    def union(self,other):
        if self.overlaps(other):
            return Interval(min(self.lower,other.lower),max(self.upper,other.upper))
        return False
    def __repr__(self):
        return f'Interval({self.lower}, {self.upper})'

class MultiInterval:
    def __init__(self):
        self.intervals = []
    def add(self,newGuy):
        toClear=[]
        for interval in self.intervals:
            if interval.overlaps(newGuy):
                newGuy = interval.union(newGuy)
                toClear.append(interval)
        self.intervals.append(newGuy)
        for trash in toClear:
            self.intervals.remove(trash)
        self.sort()
    def sort(self):
        self.intervals.sort(key = lambda i: i.lower)
    def gapsSize(self):
        g = []
        for i in range(len(self.intervals)-1):
            g.append(Interval(self.intervals[i].upper+1,self.intervals[i+1].lower-1))
        return sum([gap.size for gap in g])
    def totalSpan(self):
        return sum([i.size for i in self.intervals])


rowIntervals = MultiInterval()
for pair in pairs:
    yDiff = pair.sensor.y-checkRow
    if abs(yDiff) <= pair.radius():
        intervalRadius = pair.radius() - abs(yDiff)
        a = Interval(pair.sensor.x - intervalRadius,pair.sensor.x + intervalRadius)
        # print(f'Sensor at {pair.sensor}, distance of {abs(yDiff)} and a sensed radius of {pair.radius()} sees {intervalRadius} blocks at row {checkRow} and clears interval {a.span}')
        rowIntervals.add(a)
beaconsInRow = {}
print(rowIntervals.intervals)
for pair in pairs:
    if pair.beacon.y == checkRow:
        for interval in rowIntervals.intervals:
            if pair.beacon.x in interval.range:
                beaconsInRow[str(pair.beacon)] = 1
print(rowIntervals.totalSpan()-len(beaconsInRow))
