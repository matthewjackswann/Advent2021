# part 1

f = open("day24.txt","r")

blocks = []

blockNo = -1
for line in f:
    line = line.strip()
    if line == "inp w":
        blockNo += 1
        blocks.append([])
        continue
    blocks[blockNo].append(line)

class Block(object):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def getOutZ(self, inZ, w):
        if inZ < 0:
            return False, None
        x = (inZ % 26) + self.a
        z = inZ // self.b
        if (x != w):
            z *= 26
        y = w + self.c if x != w else 0
        return True, z + y

blockData = []
for block in blocks:
    a = int(block[4].split(" ")[-1])
    b = int(block[3].split(" ")[-1])
    c = int(block[14].split(" ")[-1])
    blockData.append(Block(a, b, c))
blocks = blockData

# Each block looks very similar and is of the form
'''
x = (z mod 26) + a
z = z // b
if (x != w):
    z = z * 26
y = (w + c) * (x != w)
z = z + y
'''
# Where a, b and c are the only changes between blocks of the program

# For the final block we know z = 0 so z = -y. As both z >= 0 and y >= 0
# z // b == 0 => |z| < b
# As z in (z mod 26) can't be -ve, previous result of z: 0 <= z < b
# y == 0 => x == 0 => x == w

# For each block b = 1 or 26
# Where b == 1 the block can either z ≈ z * 26  if (x != w) else z ≈ z
# Where b == 26 the block can either z ≈ z id (x != w) else z ≈ z // 26

password = "59996912981939"

z = 0
for i, block in enumerate(blocks):
    valid, z = block.getOutZ(z, int(password[i]))
    if not valid:
        print("broke")

password = "17241911811915"
if z == 0:
    print("passes")

z = 0
for i, block in enumerate(blocks):
    valid, z = block.getOutZ(z, int(password[i]))
    if not valid:
        print("broke")
        break
if z == 0:
    print("passes")

# as much as it pains me I didn't make a solver and looking at the output worked through
# the combinations until I got a working solution
