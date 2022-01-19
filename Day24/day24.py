from itertools import product

steps =    [14, 8, 5, None, 10, None, 16, None, 6, 13, None, None, None, None]
required = [None, None, None, 0, None, 13, None, 9, None, None, 14, 3, 2, 14]

part1_input_space = product(range(9, 0, -1), repeat=7)
part2_input_space = product(range(1, 10), repeat=7)

'''
https://www.youtube.com/watch?v=Eswmo7Y7C4U
The input program can be divided into 14 sub-programs. 
Each sub-program can be categorized into one of two different types (type 1 and type 2). 
Type 1 programs modify the value of z by:

z = 26 * z + input + some_number

Type 2 programs modify the value of z by the integer division:
z = z / 26
if and only if
z % 26 + some_number == input
'''

def valid(digits):
    z = 0
    res = [0] * 14

    digits_idx = 0
    for i in range(14):
        increment, mod_req = steps[i], required[i]

        if increment == None:
            res[i] = ((z % 26) - mod_req)
            z //= 26
            if not (1 <= res[i] <= 9):
                return False
        else:
            z = z * 26 + digits[digits_idx] + increment
            res[i] = digits[digits_idx]
            digits_idx += 1
    return res

for digits in part1_input_space:
    res = valid(digits)
    if res:
        print("Part 1: " + "".join([str(i) for i in res])) 
        break

for digits in part2_input_space:
    res = valid(digits)
    if res:
        
        print("Part 2: " + "".join([str(i) for i in res])) 
        break