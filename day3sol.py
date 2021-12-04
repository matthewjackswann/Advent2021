# part 1

f = open("day3.txt","r")

s = 12

count = [0 for i in range(s)]

for line in f:
    line = line.strip()
    for i in range(s):
        if line[i] == '1':
            count[i] += 1
        else:
            count[i] -= 1
f.close()

gamma = ""
epsilon = ""
for i in range(s):
    if count[i] > 1:
        gamma += "1"
        epsilon += "0"
    else:
        gamma += "0"
        epsilon += "1"

print(gamma)
print(epsilon)
print(int(gamma, 2) * int(epsilon, 2))

# part 2

f = open("day3.txt","r")

oxygen = []
co2 = []

for line in f:
    line = line.strip()
    oxygen.append(line)
    co2.append(line)

i = 0
while i < 12 and len(oxygen) > 1: # oxygen
    total = 0
    for reading in oxygen:
        if reading[i] == '1':
            total += 1
        else:
            total -= 1
    if total >= 0:
        keep = '1'
    else:
        keep = '0'
    oxygen = list(filter(lambda x: (x[i] == keep), oxygen))
    i += 1

print(oxygen[0])

i = 0
while i < 12 and len(co2) > 1: # co2
    total = 0
    for reading in co2:
        if reading[i] == '1':
            total += 1
        else:
            total -= 1
    if total < 0:
        keep = '1'
    else:
        keep = '0'
    co2 = list(filter(lambda x: (x[i] == keep), co2))
    i += 1

print(co2[0])
print(int(oxygen[0],2) * int(co2[0],2))
