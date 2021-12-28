from itertools import permutations

class Scanner:
    def __init__(self, id, beacons, location, visited = False):
        self.id = id
        self.beacons = beacons
        self.visited = visited
        self.location = location
        self.overlap = None

def printScanners(scanners, print_beacons = False):
    for scanner in scanners:
        if print_beacons:
            for beacon in scanner.beacons:
                print(beacon)

def distance(a, b):
    return (max(a, b) - min(a, b)) * (-1 if a > b else 1)

def manDist(a, b):
    return (abs(a[0] - b[0]) + abs(a[1] - b[1]) + abs(a[2] - b[2]))

def offsetScanner(offset, scanner):
    for i, (x, y, z) in enumerate(scanner.beacons):
        x += offset[0]
        y += offset[1]
        z += offset[2]
        scanner.beacons[i] = [x, y, z]
    (x, y, z) = scanner.location
    x += offset[0]
    y += offset[1]
    z += offset[2]
    scanner.location = [x, y, z]
#3:27

def invertPoint(offset):
    (x, y, z) = offset
    x = -x
    y = -y
    z = -z
    return (x, y, z)


def commonBeacons(s1, s2):
    result = 0
    overlap = []
    for beacon in s2.beacons:
        if beacon in s1.beacons:
            overlap.append(beacon)
            result += 1
    s2.overlap = overlap
    return result

def rotate(p1, p2):
    temp = p1
    p1 = p2
    p2 = temp * -1
    return p1, p2



def rotatePoint(p, plane):
    x, y, z = p
    if plane == 'XY':
        x, y = rotate(x, y)
    elif plane == 'ZX':
        z, x = rotate(z, x)
    elif plane == 'ZY':
        z, y = rotate(z, y)
    else:
        print("Bad plane!!!!")
    return [x, y, z]

def rotatePoints(points, plane):
    rotated = []
    for point in points:
        rotated.append(rotatePoint(point, plane))
    return rotated

def matchScannersOffsets(s1, s2):
    overlap_cnt = 0
    for i, (x1, y1, z1) in enumerate(s1.beacons):
        for j, (x2, y2, z2) in enumerate(s2.beacons):
            offset = (distance(x2,x1), distance(y2,y1), distance(z2,z1))
            offsetScanner(offset, s2)
            if commonBeacons(s1, s2) >= 12:
                print(f'matched scanner {s1.id} and scanner {s2.id}')
                #print(f'location of {s2.id} is {s2.location}')
                return True
            else:
                offset = invertPoint(offset)            
                offsetScanner(offset, s2)
    
    return False

def matchScannersRotation(s1, s2):
    result = 0
    for j in range(4):
        for i in range(4):
            if matchScannersOffsets(s1, s2):
                return True
            s2.beacons = rotatePoints(s2.beacons, "XY")
        s2.beacons = rotatePoints(s2.beacons, "ZX")
    s2.beacons = rotatePoints(s2.beacons, "ZY")
    for k in range(4):
        if matchScannersOffsets(s1, s2):
            return True
        s2.beacons = rotatePoints(s2.beacons, "XY")
    s2.beacons = rotatePoints(s2.beacons, "ZY")
    s2.beacons = rotatePoints(s2.beacons, "ZY")
    for k in range(4):
        if matchScannersOffsets(s1, s2):
            return True
        s2.beacons = rotatePoints(s2.beacons, "XY")
    s2.beacons = rotatePoints(s2.beacons, "ZY")

    return False
    
def arrangeScanners(current):
    result = 0
    for i, s in enumerate(scanners):
        if i != current.id and not scanners[i].visited:
            if matchScannersRotation(scanners[current.id], scanners[i]):
                scanners[i].visited = True
                arrangeScanners(scanners[i])



input = list(open('Day19\\input.txt').read().splitlines())
scanners = []
scanner_id = 0
scanner = scanner = Scanner(scanner_id, [], [0,0,0])


for i, line in enumerate(input):
    if line:
        if line[0] == '-' and line[1] == '-':
            continue
        position = [int(x) for x in line.split(',')]
        scanner.beacons.append(position)
    else:
        scanners.append(scanner)
        scanner_id += 1
        scanner = Scanner(scanner_id, [], [0,0,0])
        
scanners[0].visited = True
arrangeScanners(scanners[0])

result = set()
for i, scanner in enumerate(scanners):
    for beacon in scanner.beacons:
        result.add(tuple(beacon))

max_dist = float('-inf')
for i, s1 in enumerate(scanners):
    for j, s2 in enumerate(scanners):
        if i != j:
            max_dist = max(max_dist, manDist(s1.location, s2.location))

print("Part 1: ", len(result))
print("Part 2: ", max_dist)
