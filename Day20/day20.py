
def printImage():
    global current, image, width, height
    for y in range(height):
        line = ""
        for x in range(width):
            line += image[current][y*width + x]
        print(line)

def nextPixel(center, it, sample):
    global image, current, iea
    (x, y) = center
    index = 0
    bit = 0
    for dy in [-1, 0, 1]:
        for dx in [-1, 0, 1]:
            xx = x + dx
            yy = y + dy
            if 0 <= xx < width and 0 <= yy < height:
                bit = 1 if image[current][yy*width + xx] == '#' else 0
            else:
                bit = it % 2 if not sample else 0
            index = (index << 1) | bit
    return iea[index]

def countLightPixels():
    global image, current
    result = 0
    for i in range(len(image[current])):
        if image[current][i] == '#':
            result += 1
    return result
    
def nextImage(it, sample = False):
    global current, image, width, height
    next = 1 - current
    next_width = width + 2
    next_height = height + 2
    image[next] = ['.' for _ in range(next_height*next_width)]
    for y in range(next_height):
        for x in range(next_width):
            image[next][y*next_width + x] = nextPixel((x-1,y-1), it, sample)

    width = next_width
    height = next_height
    current = next

input = list(open('Day20\\test.txt').read().splitlines())
iea = ""
image = [[]]
current = 0
width = 0
height = 0
for line in input:
    if line:
        if iea == "":
            iea = line
        else:
            width = max(width, len(line))
            for x, chr in enumerate(line):
                image[current].append(chr)
            height += 1
image.append([])

part1 = 0
print(f"{width}x{height}")
for i in range(50):
    if i == 2:
        part1 = countLightPixels()
    nextImage(i)

print('Part 1: ', part1)
print('Part 2: ', countLightPixels())
