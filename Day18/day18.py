import math

def addition(first_pair, second_pair):
    return "[" + first_pair + "," + second_pair + "]"

def reduce(number):
    open_bracket = 0
    reduced = []
    reader = 0
    has_exploded = False
    while(reader < len(number)):
        if number[reader] == "[":
            open_bracket += 1
            if open_bracket > 4 and not has_exploded:
                
                left = int(number[reader + 1])
                right = int(number[reader + 3])
                
                scan_index = reader
                has_left_value = False
                while scan_index >= 0:
                    if isinstance(number[scan_index], int):
                        has_left_value = True
                        break
                    scan_index -= 1
                
                if has_left_value:
                    replace = int(number[scan_index]) + left
                    reduced[scan_index] = replace
                
                scan_index = reader + 4
                has_right_value = False
                while scan_index < len(number):
                    if isinstance(number[scan_index], int):
                        has_right_value = True
                        break
                    scan_index += 1
              
                if has_right_value:
                    replace = int(number[scan_index]) + right
                    number[scan_index] = replace
                
                reader += 5
                reduced.append(0)
                open_bracket -= 1
                has_exploded = True
            else:
                reduced.append(number[reader])
                reader += 1
        elif number[reader] == "]":
            open_bracket -= 1
            reduced.append(number[reader])
            reader += 1
        else:
            reduced.append(number[reader])         
            reader += 1
    
    return (reduced, has_exploded)

def split(number):
    splitted = []
    has_splitted = False
    for i, chr in enumerate(number):
        if isinstance(chr, int) and chr >= 10 and not has_splitted:
            splitted.append('[')
            splitted.append(math.floor(chr / 2))
            splitted.append(',')
            splitted.append(math.ceil(chr / 2))
            splitted.append(']')
            has_splitted = True
        else:
            splitted.append(chr)
    return (splitted, has_splitted)

def magnitude(number):
    mag = []
    reader = 0
    has_mag = False
    while reader < len(number):
        if number[reader] == "[":
            if reader + 3 < len(number) and isinstance(number[reader + 1], int) and isinstance(number[reader + 3], int):
                mag.append(number[reader + 1] * 3 + number[reader + 3] * 2)
                reader += 5
                has_mag = True
            else:
                mag.append(number[reader])
                reader += 1
        else:
            mag.append(number[reader])
            reader += 1
    return (mag, has_mag)

def makeSnailfishNumber(number):
    snail_number = []
    reader = 0
    while reader < len(number):
        if number[reader].isnumeric():
            if reader + 1 < len(number) and number[reader + 1].isnumeric():
                snail_number.append(int(number[reader] + number[reader + 1]))
                reader += 1
            else:
                snail_number.append(int(number[reader]))
        else:
            snail_number.append(number[reader])
        reader += 1
    return snail_number


input = list(open('Day18\\input.txt').read().splitlines())

snail_number_1 = input[0]
result = []

for reader in range(1, len(input)):
    snail_number_2 = input[reader]
    result = addition(snail_number_1, snail_number_2)
    result = makeSnailfishNumber(result)

    while(True):
        (result, reduced) = reduce(result)
        if not reduced:
            (result, splitted) = split(result)
            if not splitted:
                snail_number_1 = "".join(map(str, result))
                break

while(True):
    result, calc = magnitude(result)
    if not calc:
        break
part1 = result


max_mag = float('-inf')
for i in range(0, len(input)):
    for j in range(0, len(input)):
        if i != j:
            snail_number_1 = input[i]
            snail_number_2 = input[j]
            result = addition(snail_number_1, snail_number_2)
            result = makeSnailfishNumber(result)

            while(True):
                (result, reduced) = reduce(result)
                if not reduced:
                    (result, splitted) = split(result)
                    if not splitted:
                        snail_number_1 = "".join(map(str, result))
                        break
            while(True):
                result, calc = magnitude(result)
                if not calc:
                    break
            max_mag = max(result[0], max_mag)


print("Part 1: ", part1[0])
print("Part 2: ", max_mag)








