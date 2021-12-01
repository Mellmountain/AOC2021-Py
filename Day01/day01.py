input = [int(x) for x in open('Day01\\input.txt').read().splitlines()]

last_depth = 0
part1 = 0
three_measure = []
sum = 0
count = 0

for i in range(0, len(input)):
    depth = input[i]
    count += 1
    if(last_depth != 0 and depth > last_depth):
        part1 += 1
    last_depth = depth

    sum = 0
    for j in range(i, i + 3):
        if j >= len(input):
            sum = 0
            break
        sum += input[j]
    
    if sum > 0:
        three_measure.append(sum)

print(part1)
part2 = 0
last_depth = 0
for i in range(0, len(three_measure)):
    depth = three_measure[i]
    if(last_depth != 0 and depth > last_depth):
        part2 +=1 
    last_depth = depth
print(part2)
