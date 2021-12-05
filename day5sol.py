# part 1

map = {}

f = open("day5.txt","r")

for line in f:
    parts = line.strip().split(" -> ")
    start = parts[0].split(",")
    end = parts[1].split(",")
    dx = int(end[0]) - int(start[0])
    if dx < 0:
        dx = -1
    elif dx > 0:
        dx = 1
    dy = int(end[1]) - int(start[1])
    if dy < 0:
        dy = -1
    elif dy > 0:
        dy = 1
    if ((dx == 0) != (dy == 0)):
        step = 0
        while True:
            x = int(start[0]) + step * dx
            y = int(start[1]) + step * dy
            map[(x, y)] = map.get((x, y), 0) + 1
            if x == int(end[0]) and y == int(end[1]):
                break
            step += 1
f.close()

total = 0
for num in map.values():
    if num >= 2:
        total += 1

print(total)

# part 2
# same as part 1 but without check for (dx == 0) != (dy == 0)

map = {}

f = open("day5.txt","r")

for line in f:
    parts = line.strip().split(" -> ")
    start = parts[0].split(",")
    end = parts[1].split(",")
    dx = int(end[0]) - int(start[0])
    if dx < 0:
        dx = -1
    elif dx > 0:
        dx = 1
    dy = int(end[1]) - int(start[1])
    if dy < 0:
        dy = -1
    elif dy > 0:
        dy = 1
    step = 0
    while True:
        x = int(start[0]) + step * dx
        y = int(start[1]) + step * dy
        map[(x, y)] = map.get((x, y), 0) + 1
        if x == int(end[0]) and y == int(end[1]):
            break
        step += 1
f.close()

total = 0
for num in map.values():
    if num >= 2:
        total += 1

print(total)
