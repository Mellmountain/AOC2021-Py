input = list(open('Day03\\input.txt').read().splitlines())

gamma_rate = ''
epsilon_rate = ''
oxygen_rating = input.copy()
oxygen_remove = []
CO2_rating = input.copy()
CO2_remove = []


for i in range(0, len(input[0])):
    ones = 0
    for line in input:
        if line[i] == '1':
            ones += 1
    if ones > (len(input) - ones):
        gamma_rate += '1'    
        epsilon_rate += '0'
        
    elif ones < (len(input) - ones):
        gamma_rate += '0'
        epsilon_rate += '1'
        
    ones = 0
    for ox in oxygen_rating:
        if ox[i] == '1':
            ones += 1
        
    if len(oxygen_rating) > 1:
        if ones >= (len(oxygen_rating) - ones):
            for rating in oxygen_rating:
                if rating[i] == '0':
                    oxygen_remove.append(rating)
        else:
            for rating in oxygen_rating:
                if rating[i] == '1':
                    oxygen_remove.append(rating)

    ones = 0
    for co2 in CO2_rating:
        if co2[i] == '1':
            ones += 1
    
    if len(CO2_rating) > 1:
        if ones >= (len(CO2_rating) - ones):
            for rating in CO2_rating:
                if rating[i] == '1':
                    CO2_remove.append(rating)
        else:
            for rating in CO2_rating:
                if rating[i] == '0':
                    CO2_remove.append(rating)

    oxygen_rating = [rating for rating in oxygen_rating if rating not in oxygen_remove]
    oxygen_remove = []
    CO2_rating = [rating for rating in CO2_rating if rating not in CO2_remove]
    CO2_remove = []


print("Part 1: ", int(gamma_rate, 2) * int(epsilon_rate, 2))
print("Part 2: ", int(oxygen_rating[0], 2) * int(CO2_rating[0], 2))