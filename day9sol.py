from bisect import insort

# part 1

f = open("day9.txt","r")

m = []
sizeX = 100
sizeY = 100

for line in f:
    m.append(line.strip())

f.close()

def getNeighbours(x, y):
    n = []
    if x + 1 < sizeX:
        n.append(m[y][x+1])
    if x - 1 >= 0:
        n.append(m[y][x-1])
    if y + 1 < sizeY:
        n.append(m[y+1][x])
    if y - 1 >= 0:
        n.append(m[y-1][x])
    return n

danger = 0

lowPoints = [] # for part 2

for y in range(sizeY):
    for x in range(sizeX):
        n = getNeighbours(x, y)
        if min(n) > m[y][x]:
            danger += int(m[y][x]) + 1
            lowPoints.append((x, y)) # for part 2

print(danger)

# part 2

def calcSize(point):
    points = []
    newPoints = [point]
    while len(newPoints) > 0:
        points.extend(list(set(newPoints)))
        newPoints = []
        for p in points:
            if p[0] + 1 < sizeX and not (p[0]+1, p[1]) in points:
                if m[p[1]][p[0]+1] != '9':
                    newPoints.append((p[0]+1, p[1]))
            if p[0] - 1 >= 0 and not (p[0]-1, p[1]) in points:
                if m[p[1]][p[0]-1] != '9':
                    newPoints.append((p[0]-1, p[1]))
            if p[1] + 1 < sizeY and not (p[0], p[1]+1) in points:
                if m[p[1]+1][p[0]] != '9':
                    newPoints.append((p[0], p[1]+1))
            if p[1] - 1 >= 0 and not (p[0], p[1]-1) in points:
                if m[p[1]-1][p[0]] != '9':
                    newPoints.append((p[0], p[1]-1))
    return(len(points))

basinSize = [0, 0, 0]
for point in lowPoints:
    insort(basinSize, calcSize(point))
    basinSize = basinSize[1:]

print(basinSize[0] * basinSize[1] * basinSize[2])
