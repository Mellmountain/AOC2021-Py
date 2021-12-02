input = [int(x) for x in open('Day01\\input.txt').read().splitlines()]

last_depth = None
part1 = 0
part2 = 0
three_measurements = []
sum = 0

for i in range(0, len(input)):
    current_depth = input[i]
    if(last_depth and current_depth > last_depth):
        part1 += 1

    sum = 0
    for j in range(i, i + 3):
        if j >= len(input):
            sum = 0
            break
        sum += input[j]
    
    if sum:
        three_measurements.append(sum)

    last_depth = current_depth

last_depth = None
for i in range(0, len(three_measurements)):
    current_depth = three_measurements[i]
    if(last_depth and current_depth > last_depth):
        part2 +=1 
    last_depth = current_depth

print("Part 1: ",part1)
print("Part 2: ",part2)
