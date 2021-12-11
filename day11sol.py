# part 1

f = open("day11.txt","r")
m = []
for line in f:
    line = [c for c in line.strip()]
    m.append(list(map(int, line)))
f.close()

sizeX = 10
sizeY = 10

def update(x, y):
    m[y][x] += 1
    if m[y][x] == 10: # was 9 when updated
        for dx in range(max(0, x-1), min(sizeX, x+2)):
            for dy in range(max(0, y-1), min(sizeY, y+2)):
                update(dx, dy)

flashes = 0

for tick in range(100):
    for x in range(sizeX):
        for y in range(sizeY):
            update(x,y)
    for x in range(sizeX):
        for y in range(sizeY):
            if m[y][x] > 9:
                m[y][x] = 0
                flashes += 1

print(flashes)

# part 2
turns = 100
while True: # while waiting for them to all sync
    turns += 1
    for x in range(sizeX):
        for y in range(sizeY):
            update(x,y)
    total = 0
    for x in range(sizeX):
        for y in range(sizeY):
            if m[y][x] > 9:
                m[y][x] = 0
                total += 1
    if total == sizeX * sizeY:
        print(turns)
        break
