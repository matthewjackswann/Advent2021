# part 1

f = open("day14.txt","r")

gettingTemplate = True

template = ""

pairs = {}

for line in f:
    if line.strip() == "":
        gettingTemplate = False
        continue
    if gettingTemplate:
        template = line.strip()
    else:
        left, right = line.strip().split(" -> ")
        pairs[left] = right
f.close()

def calcStep(t):
    result = t[0]
    for i in range(1,len(t)):
        result +=  pairs[t[i-1:i+1]] + t[i]
    return result

result = template
for step in range(10):
    result = calcStep(result)

counts = {}
for i in result:
  counts[i] = counts.get(i, 0) + 1

print(max(counts.values()) - min(counts.values()))

# part 2
# once again the above method is to inefficient for large strings

def calcStep2(t):
    newT = {}
    for pair in t:
        newP = pairs[pair]
        newT[pair[0] + newP] = newT.get(pair[0] + newP, 0) + t[pair]
        newT[newP + pair[1]] = newT.get(newP + pair[1], 0) + t[pair]
    return newT

def templateToDict(template):
    t = {}
    for i in range(1,len(template)):
        t[template[i-1:i+1]] = t.get(template[i-1:i+1], 0) + 1
    return t

t = templateToDict(template)
for step in range(40):
    t = calcStep2(t)

counts = {}
for key in t:
  counts[key[0]] = counts.get(key[0], 0) + t[key]
counts[template[-1]] = counts.get(template[-1], 0) + 1 # counts all first of pair, accounts for final part of chain

print(max(counts.values()) - min(counts.values()))
