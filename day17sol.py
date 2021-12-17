from operator import methodcaller
# part 1

f = open("day17.txt","r")

txMin = 0
txMax = 0
tyMin = 0
tyMax = 0

for line in f:
    line = line.strip()
    line = line.replace("target area: ","").replace("x=","").replace("y=","")
    x, y = line.split(", ")
    txMin, txMax = map(abs, map(int,x.split(".."))) # abs is fine for x as it doesn't affect anything
    tyMin, tyMax = map(int,y.split(".."))

# max y velocity => max y position

def validYVel(y):
    d = 0
    while d >= tyMin:
        if d <= tyMax:
            return True
        d += y
        y -= 1
    return False

def maxYPos(y):
    d = 0
    while y > 0:
        d += y
        y -= 1
    return d

# this is a bad solution. I don't know how to limit it range
# after letting it run for a while no value > 100 showed up so it only checks
# the first 100 y values, this gives the correct answer
largestY = 0
for y in range(1,100):
    if validYVel(y):
        largestY = y

print(maxYPos(largestY))

# part 2

xValues = {}
yValues = {}

def calcYPos(y, t):
    d = 0
    for i in range(t+1):
        d += y
        y -= 1
    return d

# calculate possible y velocities and their time period
maxTime = 1
for y in range(tyMin,largestY + 1):
    timePeriod = []
    d = 0
    t = 0
    ty = y
    while d >= tyMin:
        if d <= tyMax:
            timePeriod.append(t)
        d += ty
        t += 1
        ty -= 1
    if t > maxTime:
        maxTime = t
    if len(timePeriod) > 0:
        yValues[y] = timePeriod


# find lower bound for possible x velocities
lowestX = 0
for n in range(txMin+1):
    if n * (n + 1) >= 2 * txMin: # sum of first n natural numbers must be greater than or equal to minX
        lowestX = n
        break

def calcXPos(x, t):
    d = 0
    for i in range(t):
        d += x
        x -= 1
        if x == 0:
            return d
    return d

# calculate possible x velocities and their time period
for xv in range(lowestX, txMax + 1):
    timePeriod = []
    t = 1
    d = calcXPos(xv, t)
    while d <= txMax and t <= maxTime:
        if d >= txMin:
            timePeriod.append(t)
        t += 1
        d = calcXPos(xv, t)
    if len(timePeriod) > 0:
        xValues[xv] = timePeriod

valid = [(x, y) for x in xValues for y in yValues if len(set(xValues[x]) & set(yValues[y])) > 0]

print(len(valid))
