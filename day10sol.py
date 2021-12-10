from collections import deque
from statistics import median

# part 1

f = open("day10.txt","r")

points = 0
autoPoints = [] # for part 2

score = {')': 3, ']': 57, '}': 1197, '>':25137}
autoScore = {'(': 1, '[': 2, '{': 3, '<':4} # for part 2

for line in f:
    stack = deque()
    broken = False
    for c in line.strip():
        if c in "([{<":
            stack.append(c)
        else:
            match = stack.pop()
            if match == '(' and c == ')':
                continue
            elif match == '{' and c == '}':
                continue
            elif match == '[' and c == ']':
                continue
            elif match == '<' and c == '>':
                continue
            else:
                broken = True
                points += score[c]
                break

    # part 2 - this only takes non broken input so can be done in the same iteration
    if not broken:
        thisPoints = 0
        while len(stack) > 0:
            match = stack.pop()
            thisPoints = (thisPoints * 5) + autoScore[match]
        autoPoints.append(thisPoints)

f.close()

print(points)
print(median(autoPoints))
