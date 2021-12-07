input = [int(x) for x in list(open('Day07\\input.txt').read().split(','))]

costs = {}
min = min(input)
max = max(input)

for i in range(min,max):
    total_cost = 0
    for num in input:
        total_cost += abs(i - num)
    if i not in costs:
        costs[i] = total_cost

print("Part 1: ", sorted(costs.items(), key=lambda x : x[1])[0][1])
costs = {}

for i in range(min,max):
    total_cost = 0
    for num in input:
        for j in range(1, abs(i-num) + 1):
            total_cost += j
    if i not in costs:
        costs[i] = total_cost

print("Part 2: ", sorted(costs.items(), key=lambda x : x[1])[0][1]) 