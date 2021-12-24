from os import system
from collections import Counter
input = list(open('Day14\\input.txt').read().splitlines())

template = input[0]
inserts = set()
pairs = {}
counter = {}
step = 0

for i, line in enumerate(input):
    if i > 1:
        pair, insert = line.strip().split('->')
        pairs[pair.strip()] = insert.strip()
        inserts.add(insert.strip())

def part1():
    global template
    for step in range(10):
        temp = ''
        for i in range(0, len(template) - 1):
            polymer = pairs[template[i] + template[i + 1]]
            temp += template[i] + polymer
        template = temp + template[-1]
        print(f'({len(template)}) : {step + 1}')
    
    min = float('inf')
    max = float('-inf')
    for i in inserts:
        count = template.count(i)
        if count < min:
            min = count
        elif count > max:
            max = count

    print(max - min)

def part2():
    global template
    # The string gets to large to loop through. If we keep track of how many pairs we have
    # generated we can still calculate the result.
    
    pair_cnt = Counter() #yay! new cool python object
    for i in range(len(template) - 1):
        pair_cnt[template[i] + template[i + 1]] += 1

    for i in range(0, 40):
        pair_cnt_temp = Counter()
        for pair in pair_cnt:
            pair_cnt_temp[pair[0] + pairs[pair]] += pair_cnt[pair]
            pair_cnt_temp[pairs[pair] + pair[1]] += pair_cnt[pair]
        pair_cnt = pair_cnt_temp
    
    char_cnt = Counter()
    for pair in pair_cnt:
        # For the whole string. Every char in a pair is both the begin char and end char 
        # of another pair, except for the first and last character. 
        # 
        # Example: pairs NN=1, NC=1, CB=1, and polymer string is NNCB
        # 
        # So if we add the count of the first char for each char + the last char from 
        # the starting template (it never changes) to get the total count.
        char_cnt[pair[0]] += pair_cnt[pair]
    char_cnt[template[-1]] += 1 #last char from start string
    print(max(char_cnt.values()) - min(char_cnt.values()))

part1()
template = input[0]
part2()

