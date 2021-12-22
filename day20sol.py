from functools import lru_cache
# part 1

algorithm = ""

f = open("day20.txt","r")

initial = {} # stores in dict so expanding image is easy, this isn't the most efficient but easiest to implement

maxY = 0
maxX = 0

for line in f:
    line = line.strip()
    if algorithm == "":
        algorithm = line.replace(".","0").replace("#","1")
    elif line == "":
        continue
    else:
        maxX = len(line)
        for x, pixel in enumerate(line):
            if pixel == '#':
                initial[(x,maxY)] = "1"
        maxY += 1

@lru_cache(maxsize=None) # allows dynamic programming. Not most efficient soln but the other way was annoying me
def getPoint(x, y, t):
    encoding = ""
    if t == 1:
        for dy in range(y-1,y+2):
            for dx in range(x-1,x+2):
                encoding += initial.get((dx,dy), "0")
    else:
        for dy in range(y-1,y+2):
            for dx in range(x-1,x+2):
                encoding += getPoint(dx, dy, t-1)
    index = int(encoding, 2)
    return algorithm[index]

total = 0
steps = 2
for y in range(-steps,maxY+steps):
    for x in range(-steps,maxX+steps):
        if getPoint(x, y, steps) == "1":
            total += 1

print(total)

# part 2

# not the fastest but not too slow and a nice use of dynamic programming

total = 0
steps = 50
for y in range(-steps,maxY+steps):
    for x in range(-steps,maxX+steps):
        if getPoint(x, y, steps) == "1":
            total += 1

print(total)
