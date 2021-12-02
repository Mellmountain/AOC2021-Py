input = list(open('Day02\\input.txt').read().splitlines())

x1, y1 = 0, 0
x2, y2, aim = 0, 0, 0

for line in input:
    command, amount = line.split()
    amount = int(amount)
    if command == 'up':
        aim -= amount
        y1 -= amount
    if command == 'down':
        aim += amount
        y1 += amount
    if command == 'forward':
        x1 += amount
        x2 += amount
        y2 += (aim * amount)

print("Part 1: ", x1 * y1)
print("Part 2: ", x2 * y2)
