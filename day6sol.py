# part 1

fish = []

f = open("day6.txt")

for line in f:
    initialConfig = line.strip().split(",")
    fish = list(map(int,initialConfig))

f.close()

for day in range(80):
    newFish = []
    for i in range(len(fish)):
        if fish[i] == 0:
            fish[i] = 6
            newFish.append(8)
        else:
            fish[i] -= 1
    fish.extend(newFish)

print(len(fish))

# part 2

# this part is obviously just to prevent bad implementations like my part 1

fish = {}

f = open("day6.txt")

for line in f:
    initialConfig = line.strip().split(",")
    initialConfig = list(map(int,initialConfig))
    for initialAge in range(9):
        fish[initialAge] = initialConfig.count(initialAge)

f.close()

for day in range(256):
    newFish = fish[0]
    for fishAge in range(8):
        fish[fishAge] = fish.get(fishAge + 1, 0)
    fish[8] = newFish
    fish[6] = fish.get(6, 0) + newFish

sum = 0
for st in fish.values():
    sum += st

print(sum)
