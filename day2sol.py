# part 1
x = 0
y = 0

f = open("day2.txt","r")

for line in f:
    line = line.strip().split()
    if line[0] == "down":
        y += int(line[1])
    elif line[0] == "up":
        y -= int(line[1])
    else:
        x += int(line[1])
print(str(x) + "," + str(y))
print(x*y)

f.close()

# part 2

x = 0
y = 0
aim = 0

f = open("day2.txt","r")

for line in f:
    line = line.strip().split()
    if line[0] == "down":
        aim += int(line[1])
    elif line[0] == "up":
        aim -= int(line[1])
    else:
        x += int(line[1])
        y += int(line[1]) * aim
print(str(x) + "," + str(y))
print(x*y)

f.close()
