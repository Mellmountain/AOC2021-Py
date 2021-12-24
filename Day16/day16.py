
from io import DEFAULT_BUFFER_SIZE


def read_packet(index, data, depth):
    value = 0
    packet_version = int(data[index:index + 3], 2)
    index += 3
    packet_type_id = int(data[index:index + 3], 2)
    print(f'read version {packet_version} @ depth {depth}')
    index += 3
    literal = ""
    if packet_type_id == 4: #literal value
        read_literal = True
        while read_literal:
            index += 1
            literal += data[index:index + 4]
            index += 4
            if data[index - 5] == '0':
                read_literal = False
        value = int(literal, 2)
        print(f'read literal = {int(literal,2)}')
        return (packet_version, index, value)
    else: #operator packet
        if data[index] == '0':
            index += 1
            sub_packet_size = int(data[index: index + 15], 2)
            index += 15
            read_subpacket = True
            bytes_read = 0
            while(read_subpacket):
                (version, new_index, val) = read_packet(index, data, depth + 1)
                bytes_read += new_index - index
                if bytes_read == sub_packet_size:
                    read_subpacket = False 
                packet_version += version
                index = new_index
                if value == 0:
                    value = val
                else:
                    if packet_type_id == 0:
                        print(f'adding {value} and {val}')
                        value += val
                    if packet_type_id == 1:
                        print(f'multiplying {value} and {val}')
                        value *= val
                        print(f'=  {value}')
                    if packet_type_id == 2:
                        print(f'min of {value} and {val}')
                        value = min(value, val)
                        print(f'=  {value}')
                    if packet_type_id == 3:
                        print(f'max of {value} and {val}')
                        value = max(value, val)
                        print(f'=  {value}')
                    if packet_type_id == 5:
                        print(f'greater than {value} and {val}')
                        value = 1 if value > val else 0
                        print(f'=  {value == 1}')
                    if packet_type_id == 6:
                        print(f'less than {value} and {val}')
                        value = 1 if value < val else 0
                        print(f'=  {value == 1}')
                    if packet_type_id == 7:
                        print(f'equals {value} and {val}')
                        value = 1 if value == val else 0
                        print(f'=  {value == 1}')
        else:
            index += 1
            sub_packet_num = int(data[index: index + 11], 2)
            index += 11
            for i in range(sub_packet_num):
                (version, new_index, val) = read_packet(index, data, depth + 1)
                packet_version += version
                index = new_index
                if value == 0:
                    value = val
                else:
                    if packet_type_id == 0:
                        print(f'adding {value} and {val}')
                        value += val
                    if packet_type_id == 1:
                        print(f'multiplying {value} and {val}')
                        value *= val
                        print(f'=  {value}')
                    if packet_type_id == 2:
                        print(f'min of {value} and {val}')
                        value = min(value, val)
                        print(f'=  {value}')
                    if packet_type_id == 3:
                        print(f'max of {value} and {val}')
                        value = max(value, val)
                        print(f'=  {value}')
                    if packet_type_id == 5:
                        print(f'greater than {value} and {val}')
                        value = 1 if value > val else 0
                        print(f'=  {value == 1}')
                    if packet_type_id == 6:
                        print(f'less than {value} and {val}')
                        value = 1 if value < val else 0
                        print(f'=  {value == 1}')
                    if packet_type_id == 7:
                        print(f'equals {value} and {val}')
                        value = 1 if value == val else 0
                        print(f'=  {value == 1}')

    return (packet_version, index, value)

def convert_to_bin(data):
    return format(int(data.strip(), 16), f"0{len(data.strip()) * 4}b")


input = list(open('Day16\\input.txt').read().splitlines())

data = convert_to_bin(input[0])
#data = convert_to_bin('9C0141080250320F1802104A08')
#data = leading_zeros(data)
(version, index , value) = read_packet(0, data, 0)
print(f'version = {version} bytes read  = {index}, value is {value}')


#00111000000000000110111101000101001010010001001000000000
#00111000000000000110111101000101001010010001001000000000

