def check_rows(board):
    for i in range(0, len(board)):
        tot = sum(board[i])
        if tot == -5:
            return True
    return False

def check_cols(board):
    total = [sum(x) for x in zip(*board)]
    for i in range(0, len(total)):
        if total[i] == -5:
            return True
    return False

def winning_board(board):
    if check_cols(board) or check_rows(board):
        return True
    return False

def score_board(board):
    sum = 0
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] != -1:
                sum += board[i][j]
    return sum

input = list(open('Day04\\input.txt').read().splitlines())
numbers = None
boards = []
board = []

for line in input:
    if not numbers:
        numbers = [int(x) for x in line.split(',')]
    else:
        if line:
            board.append([int(x) for x in line.split()])
        else:
            if board:
                boards.append(board)
            board = []

first_winner_id = 0
last_winner_id = 0
first_winner = None
last_winner = None

for num in numbers:
    for board in boards:
        if not winning_board(board):
            for i in range(5):
                for j in range(5):
                    if board[i][j] == num:
                        board[i][j] = -1        
        
            if winning_board(board):
                if not first_winner:
                    first_winner_id = num
                    first_winner = board
                last_winner_id = num
                last_winner = board

print("Part 1: ", score_board(first_winner) * first_winner_id)
print("Part 2: ", score_board(last_winner) * last_winner_id)