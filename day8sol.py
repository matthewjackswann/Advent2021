import re
# probably useful at some point

zero = [c for c in "abcefg"]
one = [c for c in "cf"]
two = [c for c in "acdeg"]
three = [c for c in "acdfg"]
four = [c for c in "bcdf"]
five = [c for c in "abdfg"]
six = [c for c in "abdefg"]
seven = [c for c in "acf"]
eight = [c for c in "abcdefg"]
nine = [c for c in "abdcfg"]

unique = [one, four, seven, eight]
allNums = [zero, one, two, three, four, five, six, seven, eight, nine]

# part 1

f = open("day8.txt","r")

total = 0

for line in f:
    input, output = line.strip().split(" | ")
    for digit in output.split(" "):
        l = len(digit)
        if l == len(one) or l == len(four) or l == len(seven) or l == len(eight):
            total += 1
f.close()

print(total)


# part 2

f = open("day8.txt")

total = 0

for line in f:
    possibleMapping = {}
    for c in "abcdefg":
        possibleMapping[c] = [c for c in "abcdefg"]
    input, output = line.strip().split(" | ")
    digits = (input + " " + output).split(" ")
    # start of logic
    lengths = {}
    for digit in digits:
        lengths[len(digit)] = lengths.get(len(digit), []) + ["".join(sorted(digit))]
        for num in unique:
            if len(digit) == len(num):
                for s in digit:
                    possibleMapping[s] = [v for v in possibleMapping[s] if v in num]
    for l in lengths:
        lengths[l] = list(set(lengths[l]))
    if 3 in lengths and 2 in lengths:
        aMapping = list(set(lengths[3][0]) - set(lengths[2][0]))[0]
        for m in possibleMapping:
            if 'a' in possibleMapping[m]: possibleMapping[m].remove('a')
        possibleMapping[aMapping] = ['a']
    if 4 in lengths and 2 in lengths:
        bdMappings = list(set(lengths[4][0]) - set(lengths[2][0]))
        for m in possibleMapping:
            possibleMapping[m] = [n for n in possibleMapping[m] if (n != 'b' and n != 'd') or (m in bdMappings)]
        for s in bdMappings:
            possibleMapping[s] = [n for n in possibleMapping[s] if n == 'b' or n == 'd']
    if 5 in lengths and len(lengths[5]) > 1:
        adgMappings = set("abcdefg")
        for digit in lengths[5]:
            adgMappings = adgMappings.intersection(digit)
        for s in adgMappings:
            possibleMapping[s] = [n for n in possibleMapping[s] if n == 'a' or n == 'd' or n == 'g']
    if 6 in lengths and len(lengths[6]) > 1:
        abfgMappings = set("abcdefg")
        for digit in lengths[6]:
            abfgMappings = abfgMappings.intersection(digit)
        for s in abfgMappings:
            possibleMapping[s] = [n for n in possibleMapping[s] if n == 'a' or n == 'b' or n == 'f' or n == 'g']
    while any(len(possibleMapping[m]) != 1 for m in possibleMapping):
        for m in possibleMapping:
            value = possibleMapping[m][0]
            if len(possibleMapping[m]) == 1: # remove all other occurrences
                for n in possibleMapping:
                    if n != m:
                        if value in possibleMapping[n]: possibleMapping[n].remove(value)
    # all mappings are done
    result = ""
    for digit in output.split(" "):
         segments = set(map(lambda d: possibleMapping[d][0] ,digit))
         for value, s in enumerate(allNums):
             if set(s) == segments:
                 result += str(value)
    total += int(result)
f.close()

print(total)
