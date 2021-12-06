def getPoints(line, part2 = False):
    x1, y1, x2, y2 = (line)
    points = []
    if y1 == y2: #isHorizontal
        if x1 > x2:
            tmp = x1
            x1 = x2
            x2 = tmp
        for x in range(x1, x2 + 1):
            points.append((x, y1))
    elif x1 == x2: #isVertical
        if y1 > y2:
            tmp = y1
            y1 = y2
            y2 = tmp
        for y in range(y1, y2 + 1):
            points.append((x1, y))
    elif part2:
        line_rise = (y2 - y1)
        line_run =  (x2 - x1)
        for i in range(max(abs(line_rise), abs(line_run)) + 1):
            x = x1 + (1 if line_run > 0 else (-1 if line_run < 0 else 0)) * i
            y = y1 + (1 if line_rise > 0 else (-1 if line_rise < 0 else 0)) * i
            points.append((x, y))
    return points


input = list(open('Day05\\input.txt').read().splitlines())

points_part1 = {}
points_part2 = {}

for line in input:
    coords = line.replace("->", ",")
    coords = coords.strip().split(',')
    line = int(coords[0]), int(coords[1]), int(coords[2]), int(coords[3])
    for p in getPoints(line):
        if p not in points_part1:
            points_part1[p] = 1
        else:
            points_part1[p] += 1
    for p in getPoints(line, True):
        if p not in points_part2:
            points_part2[p] = 1
        else:
            points_part2[p] += 1

part1 = 0
part2 = 0
for k,v in points_part1.items():
    if v > 1:
        part1 += 1
for k,v in points_part2.items():
    if v > 1:
        part2 += 1

print("Part 1: ", part1)
print("Part 2: ", part2)   