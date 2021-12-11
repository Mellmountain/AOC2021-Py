from collections import deque
input = list(open('Day11\\input.txt').read().splitlines())
octopussys = []
part1 = 0
part2 = 0
ans = 0

def flash(x, y):
    global ans
    ans += 1
    octopussys[y][x] = -1
    for dx in [-1, 0, 1]:
        for dy in [-1, 0, 1]:
            xx = x + dx
            yy = y + dy
            if 0 <= xx < len(octopussys[0]) and 0 <= yy < len(octopussys) and octopussys[yy][xx] != -1:
                octopussys[yy][xx] += 1
                if octopussys[yy][xx] >= 10:
                    flash(xx, yy)

for i, line in enumerate(input):
    row = []
    for chr in line:
        row.append(int(chr))
    octopussys.append(row)

for q in range(1000):
    for i, row in enumerate(octopussys):
        for j, chr in enumerate(octopussys[i]):
            octopussys[i][j] += 1
    
    for i, row in enumerate(octopussys):
        for j, chr in enumerate(octopussys[i]):
            if chr > 9:
                flash(j, i)
    
    for i, row in enumerate(octopussys):
        for j, chr in enumerate(octopussys[i]):
            if octopussys[i][j] == -1:
                octopussys[i][j] = 0

    allFlash = True
    for i, row in enumerate(octopussys):
        for j, chr in enumerate(octopussys[i]):
            if octopussys[i][j] != 0:
                allFlash = False

    if q == 99:
        part1 = ans
    if allFlash:
        part2 = q + 1
        break
        
print("Part 1:", part1)
print("Part 2:", part2)

