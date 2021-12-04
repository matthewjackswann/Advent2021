# part 1
f = open("day1.txt","r")

increases = -1 # -1 as first

lastDepth = 0

for line in f:
    line = line.strip()
    if lastDepth < int(line):
        increases += 1
    lastDepth = int(line)
f.close()

print(increases)

#part 2
f = open("day1.txt","r")

sum1 = 0
count1 = 0
sum2 = 0
count2 = -1
sum3 = 0
count3 = -2

windowed = []

for line in f:
    value = int(line.strip())
    if count1 >= 0:
        sum1 += value
    if count2 >= 0:
        sum2 += value
    if count3 >= 0:
        sum3 += value
    count1 += 1
    count2 += 1
    count3 += 1
    if count1 == 3:
        count1 = 0
        windowed.append(sum1)
        sum1 = 0
    if count2 == 3:
        count2 = 0
        windowed.append(sum2)
        sum2 = 0
    if count3 == 3:
        count3 = 0
        windowed.append(sum3)
        sum3 = 0
f.close()

increases = -1 # -1 as first

lastDepth = 0

for v in windowed:
    if lastDepth < v:
        increases += 1
    lastDepth = v

print(increases)
