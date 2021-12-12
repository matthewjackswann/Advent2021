# part 1

f = open("day12.txt","r")

m = {}

for line in f:
    nodeA, nodeB = line.strip().split("-")
    lst = m.get(nodeA, [])
    if nodeB not in lst:
        lst.append(nodeB)
        m[nodeA] = lst
    lst = m.get(nodeB, [])
    if nodeA not in lst:
        lst.append(nodeA)
        m[nodeB] = lst

f.close()

def BFS(path):
    if path[-1] == "end":
        return 1
    neighbours = m[path[-1]]
    visitable = [n for n in neighbours if not (n.islower() and n in path)]
    paths = 0
    for v in visitable:
        paths += BFS(path + [v])
    return paths

print(BFS(["start"]))

# part 2

def BFS2(path):
    if path[-1] == "end":
        return 1
    dupes = [x for n, x in enumerate(path) if x in path[:n]]
    for d in dupes:
        if d.islower():
            return BFS(path) # if second small cave already explored default
    neighbours = m[path[-1]]
    visitable = [n for n in neighbours if (not n.islower() or path.count(n) < 2) and n != "start"]
    paths = 0
    for v in visitable:
        paths += BFS2(path + [v])
    return paths

print(BFS2(["start"]))
