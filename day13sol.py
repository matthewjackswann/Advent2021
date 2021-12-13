# part 1

f = open("day13.txt","r")

folding = False

m = {}
folds = []

for line in f:
    line = line.strip()
    if line == "":
        folding = True
        continue
    if not folding:
        x, y = line.split(",")
        m[(int(x),int(y))] = '#'
    else:
        t, v = line.replace("fold along ","").split("=")
        folds.append((t, int(v)))

def fold(n, f):
    result = {}
    direction, position = f
    if direction == "y":
        for dot in n:
            x, y = dot
            if y > position:
                result[(x,position-(y-position))] = '#'
            else:
                result[(x,y)] = '#'
    elif direction == "x":
        for dot in n:
            x, y = dot
            if x > position:
                result[(position-(x-position),y)] = '#'
            else:
                result[(x,y)] = '#'
    return result

f.close()

print(len(fold(m, folds[0])))

# paer 2

for f in folds:
    m = fold(m, f)

maxX = max(m, key=lambda c: c[0])[0] + 1
maxY = max(m, key=lambda c: c[1])[1] + 1

for y in range(maxY):
    row = ""
    for x in range(maxX):
        row += m.get((x,y), " ")
    print(row)
