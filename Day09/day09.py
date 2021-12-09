input = list(open('Day09\\input.txt').read().splitlines())

height_map =[]
for line in input:
    y = []
    for i,v in enumerate(line):
        y.append(int(v))
    height_map.append(y)

def getNeigbourValues(x, y):
    values = []
    if 0 <= (x - 1) < len(height_map[0]):
        values.append(height_map[y][x - 1])
    if 0 <= (x + 1) < len(height_map[0]):
        values.append(height_map[y][x + 1])
    if 0 <= (y + 1) < len(height_map):
        values.append(height_map[y + 1][x])
    if 0 <= (y - 1) < len(height_map):
        values.append(height_map[y - 1][x])
    return values

def getNeigbourCoords(x, y):
    coords = []
    if 0 <= (x - 1) < len(height_map[0]) and height_map[y][x - 1] != 9:
        coords.append((x - 1, y))
    if 0 <= (x + 1) < len(height_map[0]) and height_map[y][x + 1] != 9:
        coords.append((x + 1, y))
    if 0 <= (y + 1) < len(height_map) and height_map[y + 1][x] != 9:
        coords.append((x, y + 1))
    if 0 <= (y - 1) < len(height_map) and height_map[y - 1][x] != 9:
        coords.append((x, y - 1))
    return coords

def getBasinSize(x, y):
    coords =  []
    visited = []
    coords.append((x, y))
    
    size = 0
    while len(coords) > 0:
        next = coords.pop()
        if next not in visited:
            visited.append(next)
            size += 1
            x, y = next
            for neighbour in getNeigbourCoords(x, y): #there is probably some pythonic way of doing this much cleaner!
                coords.append(neighbour)
    return size

basins = []
risk_level = 0
for y, rv in enumerate(height_map):
    for x, height in enumerate(rv):
        lowest = True
        for neighbour_height in getNeigbourValues(x, y):
            if height >= neighbour_height:
                lowest = False
                break
        if lowest:
            risk_level += height + 1
            basins.append(getBasinSize(x, y))

basins = sorted(basins, reverse=True)
print("Part 1: ", risk_level)
print("Part 2: ", basins[0] * basins[1] * basins[2])

