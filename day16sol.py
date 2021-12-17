# part 1

f = open("day16.txt","r")

msg = ""

for line in f:
    msg = line.strip()

f.close()

hexDict = {
    "G": "0000", # stops 0s from other binary results being replaced
    "H": "0001", # stops 1s from other binary results being replaced
    "2": "0010",
    "3": "0011",
    "4": "0100",
    "5": "0101",
    "6": "0110",
    "7": "0111",
    "8": "1000",
    "9": "1001",
    "A": "1010",
    "B": "1011",
    "C": "1100",
    "D": "1101",
    "E": "1110",
    "F": "1111"
}

msg = msg.replace("0","G").replace("1","H")

for c in hexDict:
    msg = msg.replace(c, hexDict[c])

def decodePacket(p):
    packet = {}
    packet["version"] = int(p[:3], 2)
    packet["id"] = int(p[3:6], 2)
    if packet["id"] == 4: # literal
        bitGroup = 0
        value = ""
        while p[6 + 5 * bitGroup] == '1':
            value += p[7 + 5 * bitGroup: 6 + 5 * (bitGroup + 1)]
            bitGroup += 1
        value += p[7 + 5 * bitGroup: 6 + 5 * (bitGroup + 1)]
        packet["value"] = int(value, 2)
        return (packet, 6 + 5 * (bitGroup + 1))
    else: # operator
        if p[6] == '0': # num of bits in sub packets
            bits = int(p[7:22], 2)
            bitsFinished = 0
            subpackets = []
            while bitsFinished < bits:
                sp, b = decodePacket(p[22 + bitsFinished:])
                subpackets.append(sp)
                bitsFinished += b
            packet["subpackets"] = subpackets
            return (packet, 22 + bitsFinished)
        else: # num of sub packets
            packetsLeft = int(p[7:18], 2)
            bitsFinished = 0
            subpackets = []
            while packetsLeft > 0:
                sp, b = decodePacket(p[18 + bitsFinished:])
                subpackets.append(sp)
                bitsFinished += b
                packetsLeft -= 1
            packet["subpackets"] = subpackets
            return (packet, 18 + bitsFinished)

def totalVersionNums(p):
    total = 0
    if "subpackets" in p:
        for sp in p["subpackets"]:
            total += totalVersionNums(sp)
    return total + p["version"]

transmission, s = decodePacket(msg)
print(totalVersionNums(transmission))
963
# part 2

def calculateValue(p):
    if p["id"] == 4:
        return p["value"]
    if p["id"] == 0: # sum
        sum = 0
        for sp in p["subpackets"]:
            sum += calculateValue(sp)
        return sum
    if p["id"] == 1: # product
        product = 1
        for sp in p["subpackets"]:
            product *= calculateValue(sp)
        return product
    if p["id"] == 2: # minimum
        v = []
        for sp in p["subpackets"]:
            v.append(calculateValue(sp))
        return min(v)
    if p["id"] == 3: # maximum
        v = []
        for sp in p["subpackets"]:
            v.append(calculateValue(sp))
        return max(v)
    if p["id"] == 5: # greater than
        if calculateValue(p["subpackets"][0]) > calculateValue(p["subpackets"][1]):
            return 1
        else:
            return 0
    if p["id"] == 6: # less than
        if calculateValue(p["subpackets"][0]) < calculateValue(p["subpackets"][1]):
            return 1
        else:
            return 0
    if p["id"] == 7: # equal to
        if calculateValue(p["subpackets"][0]) == calculateValue(p["subpackets"][1]):
            return 1
        else:
            return 0

print(calculateValue(transmission))
