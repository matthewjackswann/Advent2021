from itertools import permutations, product
# part 1

f = open("day19.txt","r")

scannerReadings = {}

scannerNo = 0

for line in f:
    line = line.strip()
    if line == "":
        scannerNo += 1
    elif line[:3] == "---":
        continue
    else:
        reading = tuple(map(int, line.split(",")))
        if scannerNo in scannerReadings:
            scannerReadings[scannerNo].append(reading)
        else:
            scannerReadings[scannerNo] = [reading]

def getRotations(initialPoints):
    rotations = []
    for a in permutations([0,1,2]): # representing x, y, z directions
        for b in product([-1, 1], repeat=3):
            thisRotationPoints = []
            for point in initialPoints:
                thisRotationPoints.append((point[a[0]] * b[0], point[a[1]] * b[1], point[a[2]] * b[2]))
            rotations.append(thisRotationPoints)
    return rotations

def scannerMatches(knownScanners, potentialScannerPoints):
    for knownScanner in knownScanners:
        for points in getRotations(potentialScannerPoints):
            commonBeacons = {}
            for point in points:
                for p in knownScanners[knownScanner]:
                    pointDifference = (p[0]-point[0],p[1]-point[1],p[2]-point[2])
                    commonBeacons[pointDifference] = commonBeacons.get(pointDifference, 0) + 1
            for p in commonBeacons:
                if commonBeacons[p] == 12:
                    return True, points, p

    return False, (), ()

knownScanners = {0: scannerReadings[0]}

scannerPositions = [] # for part 2

while len(knownScanners) != len(scannerReadings):
    for potentialScanner in scannerReadings:
        if potentialScanner in knownScanners:
            continue
        valid, scannerPoints, scannerPos = scannerMatches(knownScanners, scannerReadings[potentialScanner])
        if not valid:
            continue
        scannerPositions.append(scannerPos) # for part 2
        absolutePoints = []
        for p in scannerPoints:
            absolutePoints.append((p[0]+scannerPos[0],p[1]+scannerPos[1],p[2]+scannerPos[2]))
        knownScanners[potentialScanner] = absolutePoints

allPoints = []

for scanner in knownScanners:
    allPoints.extend(knownScanners[scanner])

allPoints = list(set(allPoints))

print(len(allPoints))

# part 2

# inefficient implementation but as the size of the set is small its fast

maxDistance = 0

for i in scannerPositions:
    for j in scannerPositions:
        distance = abs(i[0]-j[0]) + abs(i[1]-j[1]) + abs(i[2]-j[2])
        if distance > maxDistance:
            maxDistance = distance

print(maxDistance)
