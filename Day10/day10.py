from collections import deque
input = list(open('Day10\\input.txt').read().splitlines())

part1 = 0
part2 = []
incomplete = []
for line in input:
    queue = deque()
    corrupt = False
    for chr in line:
        if chr in ['{', '[', '(', '<']:
            queue.append(chr)
        else:
            if chr == ')':
                if queue[-1] != '(':
                    part1 += 3
                    corrupt = True
                    break
                else:
                    queue.pop()
            elif chr == ']':
                if queue[-1] != '[':
                    part1 += 57
                    corrupt = True
                    break
                else:
                    queue.pop()
            elif chr == '}':
                if queue[-1] != '{':
                    part1 += 1197
                    corrupt = True
                    break
                else:
                    queue.pop()
            elif chr == '>':
                if queue[-1] != '<':
                    part1 += 25137
                    corrupt = True
                    break
                else:
                    queue.pop()
    if not corrupt:
        points = 0
        for chr in reversed(queue):
            chr_score = 0
            if chr == '(':
                chr_score = 1
            elif chr == '[':
                chr_score = 2
            elif chr == '{':
                chr_score = 3
            elif chr == '<':
                chr_score = 4
            points = points * 5 + chr_score
        part2.append(points)

print("Part 1: ", part1)
part2.sort()
print("Part 2: ", part2[len(part2) // 2])
