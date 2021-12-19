# import sys
# sys.setrecursionlimit(10)
# part 1

numbers = []

f = open("day18.txt","r")

for line in f:
    numbers.append(line.strip())

f.close()

def stringToNumber(s):
    if s.isnumeric():
        return int(s)
    s = s[1:-1] # remove outer brackets
    brackets = 0
    splitPos = 0
    for i, c in enumerate(s):
        if c == '[':
            brackets += 1
        elif c == ']':
            brackets -= 1
        if brackets == 0 and c == ',':
            splitPos = i
            break
    left = s[:splitPos]
    right = s[splitPos + 1:]
    return [stringToNumber(left), stringToNumber(right)]

def add(a, b):
    return [a, b]

def getDepth(n):
    if type(n) == int:
        return 0
    l, r = n
    return 1 + max(getDepth(l), getDepth(r))

def getExplodePath(n, p=[], d=0):
    if type(n) == int:
        return []
    if d == 4:
        return p
    left, right = n
    l = getExplodePath(left, p + [0], d + 1)
    if len(l) > 0:
        return l
    r = getExplodePath(right, p + [1], d + 1)
    return r

def followPath(n, path):
    if len(path) == 1:
        return n[path[0]]
    else:
        return followPath(n[path[0]], path[1:])

def explodeLeft(n, p, v):
    path = []
    for i, d in enumerate(p[::-1]):
        if d == 1:
            path = p[:-i-1] + [0] + [1 for x in range(5)]
            break
    if path == []:
        return
    for direction in path:
        if type(n[direction]) == int:
            n[direction] = n[direction] + v
            return
        n = n[direction]

def explodeRight(n, p, v):
    path = []
    for i, d in enumerate(p[::-1]):
        if d == 0:
            path = p[:-i-1] + [1] + [0 for x in range(5)]
            break
    if path == []:
        return
    for direction in path:
        if type(n[direction]) == int:
            n[direction] = n[direction] + v
            return
        n = n[direction]

def explode(n):
    if getDepth(n) < 5: # nothing to be exploded
        return False
    else:
        path = getExplodePath(n)
        x, y = followPath(n, path)
        explodeLeft(n, path, x)
        explodeRight(n, path, y)
        while len(path) != 1:
            n = n[path[0]]
            path = path[1:]
        n[path[0]] = 0
        return True

def split(n):
    l, r = n
    if type(l) == int:
        if l >= 10:
            v1 = l // 2
            v2 = l - v1
            n[0] = [v1, v2]
            return True
    else:
        if split(l):
            return True
    if type(r) == int:
        if r >= 10:
            v1 = r // 2
            v2 = r - v1
            n[1] = [v1, v2]
            return True
    else:
        if split(r):
            return True
    return False

def reduceNumber(n):
    while True:
        if explode(n):
            continue
        if split(n):
            continue
        break

def getMagnitude(n):
    total = 0
    l, r = n
    if type(l) == int:
        total += 3 * l
    else:
        total += 3 * getMagnitude(l)
    if type(r) == int:
        total += 2 * r
    else:
        total += 2 * getMagnitude(r)
    return total

num = stringToNumber(numbers[0])
for n in numbers[1:]:
    num = add(num, stringToNumber(n))
    reduceNumber(num)

print(getMagnitude(num))

# part 2

largestSum = 0
for a in numbers:
    for b in numbers:
        if a == b:
            continue
        else:
            value = add(stringToNumber(a), stringToNumber(b))
            reduceNumber(value)
            size = getMagnitude(value)
            if size > largestSum:
                largestSum = size
print(largestSum)
