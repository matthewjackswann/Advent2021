# part 1

f = open("day4.txt","r")

boardSize = 5

def checkBoard(board):
    for row in board:
        all = True
        for e in row:
            if e != -1:
                all = False
        if all:
            return True
    for column in range(boardSize):
        all = True
        for row in board:
            if row[column] != -1:
                all = False
        if all:
            return True
    return False

def scoreBoard(board):
    score = 0
    for row in board:
        for e in row:
            if e != -1:
                score += e
    return score

lineNo = 1
boardNumber = -1

numbers = []
boards = []

for line in f:
    line = line.strip()
    if lineNo == 1:
        numbers = list(map(int,line.split(",")))
    else:
        if line == "":
            boardNumber += 1
            boards.append([])
        else:
            boards[boardNumber].append(list(map(int,line.split())))
    lineNo += 1
f.close()

nextNumIndex = 0 # for part 2
for n in numbers:
    nextNumIndex += 1 # for part 2
    for b in boards:
        for row in b:
            for c in range(boardSize):
                if row[c] == n:
                    row[c] = -1
        if checkBoard(b):
            print(scoreBoard(b) * n)
            break
    else: # continue if not broken
        continue
    break # break if inner loop breaks


# part 2

# the same boards can be used as processing can be skipped for first few numbers

nextNumIndex -= 1 # ensure this pass if fully done

while len(boards) > 1:
    toRemove = []
    for b in boards:
        for row in b:
            for c in range(boardSize):
                if row[c] == numbers[nextNumIndex]:
                    row[c] = -1
        if checkBoard(b):
            toRemove.append(b)
    for b in toRemove:
        boards.remove(b)
    nextNumIndex += 1

# only one board is remaining

while True:
    for row in boards[0]:
        for c in range(boardSize):
            if row[c] == numbers[nextNumIndex]:
                row[c] = -1
    if checkBoard(boards[0]):
        print(scoreBoard(boards[0]) * numbers[nextNumIndex])
        break
    nextNumIndex += 1
