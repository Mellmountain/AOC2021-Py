input = list(open('Day13\\input.txt').read().splitlines())
coords = []

for line in input:
    if line:
        x, y = line.split(',')
        coords.append((int(x), int(y)))
    else:
        break

def stampsheet():
    sheet = [['.' for x in range(0,40)] for y in range(0,7)]
    for c in coords:
        x, y = c
        sheet[y][x] = '#'
    for i in range(0,7):
        print(sheet[i])

def foldY(line):
    global coords
    fold = set()
    for cord in coords:
        x, y = cord
        if y > line:
            delta = y - line
            y = line - delta
        fold.add((x, y))
    coords = fold

def foldX(line):
    global coords
    fold = set()
    for cord in coords:
        x, y = cord
        if x > line:
            delta = x - line
            x = line - delta
        fold.add((x, y))
    coords = fold

foldX(655)
print("Part 1: ", len(coords))
foldY(447)
foldX(327)
foldY(223)
foldX(163)
foldY(111)
foldX(81)
foldY(55)
foldX(40)
foldY(27)
foldY(13)
foldY(6)
print("Part 2:")
stampsheet()