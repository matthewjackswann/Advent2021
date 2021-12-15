# part 1
# just use a bad implementation of dijkstra

size = 100

f = open("day15.txt","r")

m = []

for line in f:
    m.append(line.strip())
f.close()

src = (0,0)
target = (size - 1, size - 1)

def getNeighbours(pos):
    x, y = pos
    n = []
    if x > 0:
        n.append((x-1, y))
    if x < size - 1:
        n.append((x+1,y))
    if y > 0:
        n.append((x,y-1))
    if y < size - 1:
        n.append((x,y+1))
    return n

def dijkstra(src, target):
    distances = {src: 0}
    front = getNeighbours(src)
    while len(front) > 0:
        best = (0,0)
        dis = 1000000000
        for n in front:
            for neighbour in getNeighbours(n):
                x, y = n
                score = distances.get(neighbour, 1000000000) + int(m[y][x])
                if score < dis:
                    dis = score
                    best = n
        if best == target:
            return dis
        distances[best] = dis
        front.extend(getNeighbours(best))
        front = [n for n in front if not n in distances]

print(dijkstra(src, target))

# part 2
# i know you're supposed to make an optimised program but I'll hapilly wait

size = 500
defaultSize = 100
target = (size - 1, size - 1)

def dijkstra5(src, target):
    distances = {src: 0}
    front = getNeighbours(src)
    while len(front) > 0:
        best = (0,0)
        dis = 1000000000
        for n in front:
            for neighbour in getNeighbours(n):
                x, y = n
                increase = (x // defaultSize) + (y // defaultSize) - 1
                score = distances.get(neighbour, 1000000000) + ((int(m[y % defaultSize][x % defaultSize]) + increase) % 9) + 1
                if score < dis:
                    dis = score
                    best = n
        if best == target:
            return dis
        distances[best] = dis
        front.extend(getNeighbours(best))
        front = [n for n in front if not n in distances]

print(dijkstra5(src, target))
