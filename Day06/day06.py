from collections import defaultdict


input = list(open('Day06\\input.txt').read().splitlines())
input = [int(x) for x in input[0].split(',')]


fishes = defaultdict(int)
for number in input:
    if number not in fishes:
        fishes[number] = 0
    fishes[number] += 1

for day in range(256):
    if day == 80:
        print("Part 1 :", sum(fishes.values()))

    temp = defaultdict(int)
    for number, count in fishes.items():
        if number == 0:
            temp[6] += count
            temp[8] += count
        else:
            temp[number-1] += count
    fishes = temp
    
print("Part 2 :", sum(fishes.values()))
