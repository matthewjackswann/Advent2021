# part 1
f = open("day7.txt","r")

possitions = []

for line in f:
    possitions = list(map(int, line.strip().split(",")))

f.close()

def calculateFuel(p):
    fuel = 0
    for pos in possitions:
        fuel += abs(p - pos)
    return fuel

score = sum(possitions)
for i in range(1, max(possitions) + 1):
    newScore = calculateFuel(i)
    if newScore < score:
        score = newScore
    else:
        break

print(score)

# part 2

def calculateFuel2(p):
    fuel = 0
    for pos in possitions:
        diff = abs(p - pos)
        fuel += (diff * (diff + 1)) // 2
    return fuel

score = calculateFuel2(0)
for i in range(1, max(possitions) + 1):
    newScore = calculateFuel2(i)
    if newScore < score:
        score = newScore

print(score)
