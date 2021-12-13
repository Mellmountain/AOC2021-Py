from collections import defaultdict, deque
input = list(open('Day12\\input.txt').read().splitlines())

map = defaultdict(list)
for line in input:
    start, dest = line.strip().split('-')    
    map[start].append(dest)
    map[dest].append(start)

def solve(part2):
    start = ('start', set(['start']), None)
    paths = 0
    queue = deque([start])
    while len(queue) > 0:
        cave, forbidden, small_visited = queue.pop()
        if cave == 'end':
            paths += 1
            continue
        for node in map[cave]:
            if node not in forbidden:
                new_forbidden = set(forbidden)
                if node.islower():
                    new_forbidden.add(node)
                queue.append((node, new_forbidden, small_visited))
            elif node in forbidden and small_visited is None and node not in ['start', 'end'] and part2:
                queue.append((node, forbidden, node))
    return paths

print("Part 1: ", solve(False))
print("Part 2: ", solve(True))