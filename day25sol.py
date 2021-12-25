# part 1

m = []

f = open("day25.txt","r")

for line in f:
    m.append([c for c in line.strip()])
f.close()

width = len(m[0])
height = len(m)

def moveCucumbers():
    movingEast = []
    for y, row in enumerate(m):
        for x, thing in enumerate(row):
            if thing == '>' and m[y][(x + 1) % width] == '.':
                movingEast.append((x, y))
    for cx, cy in movingEast:
        m[cy][cx] = '.'
        m[cy][(cx + 1) % width] = '>'
    movingSouth = []
    for y, row in enumerate(m):
        for x, thing in enumerate(row):
            if thing == 'v' and m[(y + 1) % height][x] == '.':
                movingSouth.append((x, y))
    for cx, cy in movingSouth:
        m[cy][cx] = '.'
        m[(cy + 1) % height][cx] = 'v'
    return len(movingSouth) != 0 or len(movingEast) != 0


turn = 1
while moveCucumbers():
    turn += 1

print(turn)
