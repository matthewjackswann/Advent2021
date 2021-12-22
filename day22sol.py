# part 1

f = open("day22.txt","r")

m = {}

lineNo = 0
for line in f:
    if lineNo == 20:
        break
    else:
        toggle, area = line.strip().split(" ")
        x, y, z = area.split(",")
        x = x.replace("x=","")
        y = y.replace("y=","")
        z = z.replace("z=","")
        xMin, xMax = map(int, x.split(".."))
        yMin, yMax = map(int, y.split(".."))
        zMin, zMax = map(int, z.split(".."))
        if toggle == "on":
            for dx in range(xMin, xMax+1):
                for dy in range(yMin, yMax+1):
                    for dz in range(zMin, zMax+1):
                        m[(dx, dy, dz)] = True
        else:
            for dx in range(xMin, xMax+1):
                for dy in range(yMin, yMax+1):
                    for dz in range(zMin, zMax+1):
                        m.pop((dx, dy, dz), None)
        lineNo += 1

f.close()

print(len(m))

# part 2

# this looks like a pain, store cubes as large cubes which can have areas removed
# the large cubes are split into a list of small cubes when an area is removed

class Cube(object):
    def __init__(self, xMin, xMax, yMin, yMax, zMin, zMax):
        self.xMin = xMin
        self.xMax = xMax
        self.yMin = yMin
        self.yMax = yMax
        self.zMin = zMin
        self.zMax = zMax

    def contains(self, cube):
        return self.xMin <= cube.xMin and self.xMax >= cube.xMax and self.yMin <= cube.yMin and self.yMax >= cube.yMax and self.zMin <= cube.zMin and self.zMax >= cube.zMax

    def intersects(self, cube):
        return self.xMin <= cube.xMax and self.xMax >= cube.xMin and self.yMin <= cube.yMax and self.yMax >= cube.yMin and self.zMin <= cube.zMax and self.zMax >= cube.zMin

    def getVolume(self):
        return (self.xMax - self.xMin) * (self.yMax - self.yMin) * (self.zMax - self.zMin)

    def __repr__(self):
        return str((self.xMin, self.xMax, self.yMin, self.yMax, self.zMin, self.zMax))

    def subtract(self, cube):
        subCubes = []

        if cube.contains(self):
            return subCubes

        xsplits = [self.xMin]
        ysplits = [self.yMin]
        zsplits = [self.zMin]
        if self.xMin < cube.xMin < self.xMax:
            xsplits.append(cube.xMin)
        if self.xMin < cube.xMax < self.xMax:
            xsplits.append(cube.xMax)
        if self.yMin < cube.yMin < self.yMax:
            ysplits.append(cube.yMin)
        if self.yMin < cube.yMax < self.yMax:
            ysplits.append(cube.yMax)
        if self.zMin < cube.zMin < self.zMax:
            zsplits.append(cube.zMin)
        if self.zMin < cube.zMax < self.zMax:
            zsplits.append(cube.zMax)
        xsplits.append(self.xMax)
        ysplits.append(self.yMax)
        zsplits.append(self.zMax)
        for cxMin, cxMax in zip(xsplits, xsplits[1:]):
            for cyMin, cyMax in zip(ysplits, ysplits[1:]):
                for czMin, czMax in zip(zsplits, zsplits[1:]):
                    c = Cube(cxMin, cxMax, cyMin, cyMax, czMin, czMax)
                    if cube.contains(c):
                        continue
                    subCubes.append(c)
        return subCubes

f = open("day22.txt","r")

cubes = []

for line in f:
    toggle, area = line.strip().split(" ")
    x, y, z = area.split(",")
    x = x.replace("x=","")
    y = y.replace("y=","")
    z = z.replace("z=","")
    xMin, xMax = map(int, x.split(".."))
    yMin, yMax = map(int, y.split(".."))
    zMin, zMax = map(int, z.split(".."))
    newCube = Cube(xMin, xMax+1, yMin, yMax+1, zMin, zMax+1)
    newCubes = []
    for c in cubes:
        if c.intersects(newCube):
            newCubes.extend(c.subtract(newCube))
        else:
            newCubes.append(c)
    if toggle == "on":
        newCubes.append(newCube)
    cubes = newCubes

total = 0
for c in cubes:
    total += c.getVolume()

print(total)
