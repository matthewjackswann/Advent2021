import re
from queue import PriorityQueue
from functools import lru_cache
# part 1

f = open("day23.txt","r")

room1 = ""
room2 = ""
room3 = ""
room4 = ""
hallway = "..x.x.x.x.."

scoring = {'a': 1, 'b': 10, 'c': 100, 'd':1000}
target = {'a': 0, 'b': 1, 'c': 2, 'd': 3}

for i, line in enumerate(f):
    if i == 2 or i == 3:
        r1, r2, r3, r4 = re.findall("[ABCD]", line)
        room1 += r1 # pair with bool is for if the amphipods have moved yet
        room2 += r2
        room3 += r3
        room4 += r4
f.close()

@lru_cache(None)
def move(f, t, rooms, hallway):
    pieceMoved = None
    rooms = rooms.split(",")
    hallway = [c for c in hallway]
    if f < 10:
        pieceMoved = rooms[f][0].lower()
        rooms[f] = rooms[f][1:]
    else:
        pieceMoved = hallway[f - 10].lower()
        hallway[f - 10] = '.'
    if t < 10:
        rooms[t] = pieceMoved + rooms[t]
    else:
        hallway[t - 10] = pieceMoved
    return ",".join(rooms), "".join(hallway)

@lru_cache(None)
def findLowestValue(rooms, hallway, maxDepth):
    rooms = rooms.split(",")
    if all(map(lambda r: len(set(r.lower())) == 1, rooms)) and len(set(hallway)) == 2:
        return 0
    for pos, thing in enumerate(hallway): # moves into room prioritied
        if thing != '.' and thing != 'x':
            for h in range(pos - 1, -1, -1): # looks left down hallway
                if hallway[h] != '.' and hallway[h] != 'x':
                    break
                if hallway[h] == 'x': # check room
                    roomNo = (h // 2) - 1
                    if target[thing] != roomNo:
                        continue
                    room = rooms[roomNo]
                    if (len(room) == 0) or (len(room) < maxDepth and len(set(room.lower())) == 1 and list(set(room.lower()))[0] == thing): # if room has space empty always move into that as first priority
                        thisDistance = pos - h + maxDepth - len(room)
                        thisDifficulty = thisDistance * scoring[thing]
                        return thisDifficulty + findLowestValue(*move(pos + 10, roomNo, ",".join(rooms), hallway), maxDepth)
            for h in range(pos + 1, 11): # looks right down hallway
                if hallway[h] != '.' and hallway[h] != 'x':
                    break
                if hallway[h] == 'x': # check room
                    roomNo = (h // 2) - 1
                    if target[thing] != roomNo:
                        continue
                    room = rooms[roomNo]
                    if (len(room) == 0) or (len(room) < maxDepth and len(set(room.lower())) == 1 and list(set(room.lower()))[0] == thing): # if room has space empty always move into that as first priority
                        thisDistance = h - pos + maxDepth - len(room)
                        thisDifficulty = thisDistance * scoring[thing]
                        return thisDifficulty + findLowestValue(*move(pos + 10, roomNo, ",".join(rooms), hallway), maxDepth)
    nextStates = []
    for roomNo, room in enumerate(rooms):
        if len(room) > 0 and room[0].isupper(): # if can move out of room
            distance = maxDepth + 1 - len(room) # steps taken to leave room
            hallwayPos = (roomNo + 1) * 2
            for h in range(hallwayPos - 1, -1, -1): # looks left down hallway
                if hallway[h] != '.' and hallway[h] != 'x':
                    break
                if hallway[h] == '.': # go to spot in hallway
                    thisDistance = distance + hallwayPos - h
                    thisDifficulty = thisDistance * scoring[room[0].lower()]
                    nextStates.append(thisDifficulty + findLowestValue(*move(roomNo, h + 10, ",".join(rooms), hallway), maxDepth))
            for h in range(hallwayPos + 1, 11): # looks left down hallway
                if hallway[h] != '.' and hallway[h] != 'x':
                    break
                if hallway[h] == '.': # go to spot in hallway
                    thisDistance = distance + h - hallwayPos
                    thisDifficulty = thisDistance * scoring[room[0].lower()]
                    nextStates.append(thisDifficulty + findLowestValue(*move(roomNo, h + 10, ",".join(rooms), hallway), maxDepth))
    if len(nextStates) == 0:
        return 10000000000000000
    return min(nextStates)

print(findLowestValue(room1 + "," + room2 + "," + room3 + "," + room4, hallway, 2))

# part 2

room1 = room1[0] + "DD" + room1[1]
room2 = room2[0] + "CB" + room2[1]
room3 = room3[0] + "BA" + room3[1]
room4 = room4[0] + "AC" + room4[1]

print(findLowestValue(room1 + "," + room2 + "," + room3 + "," + room4, hallway, 4))
