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

# TODO: 







# stuff
