'''
Credits for Part 2 goes to Jonathan Paulson (https://www.youtube.com/channel/UCuWLIm0l4sDpEe28t41WITA)
I rewrote parts of my solution to fit his. It is however quite slow on my machine.  
'''
input = list(open('Day22\\input.txt').read().splitlines())
cuboids = []
X_Range = set()
Y_Range = set()
Z_Range = set()

for line in input:
        command, cuboid = line.split(' ')
        ranges = cuboid.split(',')
        for r in ranges:
            axis = r[:1]
            min_range, max_range = r[2:].split('..')
            if axis == 'x':
                xmin = min(int(min_range), int(max_range))
                xmax = max(int(min_range), int(max_range))
                X_Range.add(xmin)
                X_Range.add(xmax + 1)
            elif axis == 'y':
                ymin = min(int(min_range), int(max_range))
                ymax = max(int(min_range), int(max_range))
                Y_Range.add(ymin)
                Y_Range.add(ymax + 1)
            elif axis == 'z':
                zmin = min(int(min_range), int(max_range))
                zmax = max(int(min_range), int(max_range))
                Z_Range.add(zmin)
                Z_Range.add(zmax + 1)
            else:
                print('Oh no! You did not parse the input correct!')
        cuboids.append((xmin, xmax, ymin, ymax, zmin, zmax, command == 'on'))

def expand_interval(range):
    copy = set()
    for val in range:
        copy.add(val)
    copy = sorted(copy)

    result = {}
    U = {}
    length_sum = 0
    for i, val in enumerate(copy):
        result[val] = i
        if i + 1 < len(copy):
            length = copy[i + 1] - val
            length_sum += length
            U[i] = length
    
    return (result, U)


def limitRange(min_value, min_limit, max_value, max_limit):
    if min_value < min_limit:
        min_value = min_limit
    if max_value > max_limit:
        max_value = max_limit
    return (min_value, max_value)

def reboot_reactor(limit_range = True):
    active_cubes = set()
    for i, (xmin, xmax, ymin, ymax, zmin, zmax, cmd) in enumerate(cuboids):
        print(f'processed ({i+1}/{len(cuboids)} cuboids')
        if limit_range:
            (xmin, xmax) = limitRange(xmin, -50, xmax, 50)
            (ymin, ymax) = limitRange(ymin, -50, ymax, 50)
            (zmin, zmax) = limitRange(zmin, -50, zmax, 50)
        for x in range(X_Range[xmin],X_Range[xmax + 1]):
            for y in range(Y_Range[ymin], Y_Range[ymax + 1]):
                for z in range(Z_Range[zmin], Z_Range[zmax + 1]):
                    if cmd:
                        active_cubes.add((x, y, z))
                    else:
                        active_cubes.discard((x, y, z))
    result = 0
    for (x, y, z) in active_cubes:
        volX = VolumeX[x]
        volY = VolumeY[y]
        volZ = VolumeZ[z]
        result += volX * volY * volZ
    return result

X_Range.add(-50)
X_Range.add(51)
Y_Range.add(-50)
Y_Range.add(51)
Z_Range.add(-50)
Z_Range.add(51)

X_Range, VolumeX = expand_interval(X_Range)
Y_Range, VolumeY = expand_interval(Y_Range)
Z_Range, VolumeZ = expand_interval(Z_Range)

print("Part 1: ", reboot_reactor(True))
print("Part 2: ", reboot_reactor(False))

    
    