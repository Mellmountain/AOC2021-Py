def print_sea_floor(sea_floor, step):
    print(f"After {step} step:")
    for line in sea_floor:
        l = ""
        for chr in line:
            l += chr
        print(l)

def update_east(sea_floor, sea_eastbound):
    for idx, row in enumerate(sea_eastbound):
        for jdx, col in enumerate(sea_eastbound[idx]):
            if sea_floor[idx][jdx] != 'v':
                sea_floor[idx][jdx] = col
    return sea_floor


input = list(open('Day25\\input.txt').read().splitlines())

sea_floor = []
for line in input:
    row = []
    for chr in line:
        row.append(chr)
    sea_floor.append(row)

steps = 0
while True:
    movements = 0
    sea_floor_copy = [['.' for _ in range(0, len(sea_floor[0]))] for _ in range(0, len(sea_floor))]
    for idx, row in enumerate(sea_floor):
        for jdx, col in enumerate(row):
            if col == '>':
                index = (jdx + 1) % len(sea_floor[idx])
                if sea_floor[idx][index] == '.':
                    sea_floor_copy[idx][index] = '>'
                    movements += 1
                else:
                    sea_floor_copy[idx][jdx] = '>'
    
    sea_floor = update_east(sea_floor, sea_floor_copy)

    for idx, row in enumerate(sea_floor):
        for jdx, col in enumerate(row):
            if col == 'v':
                index = (idx + 1) % len(sea_floor)
                if sea_floor[index][jdx] == '.':
                    sea_floor_copy[index][jdx] = 'v'
                    movements += 1
                else:
                    sea_floor_copy[idx][jdx] = 'v'
    sea_floor = sea_floor_copy
    steps += 1
    #print_sea_floor(sea_floor, steps)
    if movements == 0:
        break

print(steps)

