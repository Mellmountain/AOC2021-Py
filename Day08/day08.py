input = list(open('Day08\\input.txt').read().splitlines())

mapping = {}
'''
  0:      1:      2:      3:      4:
 aaaa    ....    aaaa    aaaa    ....
b    c  .    c  .    c  .    c  b    c
b    c  .    c  .    c  .    c  b    c
 ....    ....    dddd    dddd    dddd
e    f  .    f  e    .  .    f  .    f
e    f  .    f  e    .  .    f  .    f
 gggg    ....    gggg    gggg    ....

  5:      6:      7:      8:      9:
 aaaa    aaaa    aaaa    aaaa    aaaa
b    .  b    .  .    c  b    c  b    c
b    .  b    .  .    c  b    c  b    c
 dddd    dddd    ....    dddd    dddd
.    f  e    f  .    f  e    f  .    f
.    f  e    f  .    f  e    f  .    f
 gggg    gggg    ....    gggg    gggg
'''

'''
    The decode method tries to map what number that 
    hides behind a specific segment input

    segment(s) of length 2, 3, 4 and 7 are certain and
    maps to numbers 1, 7, 4 and 8 respectively

    input of length 5 is either 2, 3 or 5
    We can deduce what number it is by looking at
    the input segments (encoded) and segments from known numbers.
    - 3 is the only number that has all segments from 1
    - 5 is the only number that has all segments from 9
    If none of the above are true for the input it must be a 2.

    input of lenth 6 is either 0, 6 or 9
    Just like input of length 5 we can deduce what number 
    it is by looking at the input segments (encoded) and segments from known numbers.
    - 9 is the only number that has all segments from 4
    - 6 is the only number that does not have all segments from 1
    If none of the above are true for the input it must be a 0
'''
def decode(segment_input):
    while len(mapping.items()) != 10:
        for encoded in segment_input:
            encoding = set()
            for chr in encoded:
                encoding.add(chr)
            if len(encoded) == 2:
                mapping[1] = encoding
            if len(encoded) == 3:
                mapping[7] = encoding    
            if len(encoded) == 4:
                mapping[4] = encoding
            if len(encoded) == 7:
                mapping[8] = encoding
            if len(encoded) == 5:
                if mapping[1].intersection(encoding) == mapping[1]:
                    mapping[3] = encoding
                elif 9 in mapping and mapping[9].intersection(encoding) == encoding:
                    mapping[5] = encoding
                else:
                    mapping[2] = encoding
            if len(encoded) == 6: 
                if mapping[1].intersection(encoding) != mapping[1]:
                    mapping[6] = encoding
                elif mapping[4].intersection(encoding) == mapping[4]:
                    mapping[9] = encoding
                else:
                    mapping[0] = encoding
        
sum = 0
part1 = 0
for line in input:
    numbers, output = line.split('|')
    mapping = {}
    encoded = numbers.strip().split(' ')    
    decode(sorted(encoded, key=len))
    number = ''
    output = output.strip().split(' ')
    for outp in output:
            num = set()
            for chr in outp:
                num.add(chr)
            if len(outp) == 2 or len(outp) == 3 or len(outp) == 4 or len(outp) == 7:
                part1 += 1        
            for i, k in enumerate(mapping):
                if mapping[i] == num:
                    number += str(i)
    sum += int(number)
    
print("Part 1: ", part1)
print("Part 2: ", sum)

