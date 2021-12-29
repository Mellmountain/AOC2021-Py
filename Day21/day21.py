class Player:
    def __init__(self, start):
        self.position = start
        self.score = 0

#Sample
p1 = Player(5)
p2 = Player(9)
rolls = 0

def solve_part1():
    global rolls
    die = 1
    turn = 0
    while True:
        #Player 1:
        rolled = 0
        for i in range(3):
            rolled += die % 100 if die % 100 != 0 else 100 
            die += 1
            rolls += 1

        p1.score += (p1.position + rolled) % 10 if (p1.position + rolled) % 10 != 0 else 10
        p1.position = (p1.position + rolled) % 10 if (p1.position + rolled) % 10 != 0 else 10
        #print(f'[turn {t}]: player 1 rolled {rolled} and moved to {p1.position} for total score of {p1.score}')

        if p1.score >= 1000:
            break

        rolled = 0
        for i in range(3):
            rolled += die % 100 if die % 100 != 0 else 100 
            die += 1
            rolls += 1

        p2.score += (p2.position + rolled) % 10 if (p2.position + rolled) % 10 != 0 else 10
        p2.position = (p2.position + rolled) % 10 if (p2.position + rolled) % 10 != 0 else 10
        #print(f'[turn {t}]: player 2 rolled {rolled} and moved to {p2.position} for total score of {p2.score}')
        
        if p2.score >= 1000:
            break

game_states = {}
def solve_part2(p1_turn, p1_pos, p2_pos, p1_score, p2_score):
    
    if (p1_turn, p1_pos, p2_pos, p1_score, p2_score) in game_states:
        return game_states[(p1_turn, p1_pos, p2_pos, p1_score, p2_score)]
    else:
        if p1_score >= 21:
            return (1, 0)
        elif p2_score >= 21:
            return (0, 1)
        else:
            if p1_turn:
                new_pos = 0
                result = (0, 0)
                for i in range(1, 4):
                    for j in range(1, 4):
                        for k in range(1, 4):
                            new_pos = ((p1_pos + i + j + k) - 1) % 10 + 1 #hacky way of not having 0
                            (p1_wins, p2_wins) = solve_part2(False, new_pos, p2_pos, p1_score + new_pos, p2_score)
                            result = (p1_wins + result[0], p2_wins + result[1])

            else:
                new_pos = 0
                result = (0, 0)
                for i in range(1, 4):
                    for j in range(1, 4):
                        for k in range(1, 4):
                            new_pos = ((p2_pos + i + j + k) - 1) % 10 + 1
                            (p1_wins, p2_wins) = solve_part2(True, p1_pos, new_pos, p1_score, p2_score + new_pos)
                            result = (p1_wins + result[0], p2_wins + result[1])
        game_states[(p1_turn, p1_pos, p2_pos, p1_score, p2_score)] = result
    return result

solve_part1()
print("Part 1 :", rolls * min(p1.score, p2.score))
result = solve_part2(True, 5, 9, 0, 0)
print("Part 2 :", max(result[0], result[1]))
