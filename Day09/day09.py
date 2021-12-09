input = list(open('Day09\\input.txt').read().splitlines())

height_map =[]
for line in input:
    row = []
    for i,v in enumerate(line):
        row.append(int(v))
    height_map.append(row)

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
part1 = 0
for row, rv in enumerate(height_map):
    for col, cv in enumerate(rv):
        lowest = True
        for neighbour in getNeigbourValues(col, row):
            if cv >= neighbour:
                lowest = False
                break
        if lowest:
            part1 += cv + 1
            basins.append(getBasinSize(col, row))

basins = sorted(basins, reverse=True)
print(part1)
print(basins[0] * basins[1] * basins[2])

