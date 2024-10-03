# Create Board which will be updated during the game
board = [[1, 2, 3],
[4, 5, 6],
[7, 8, 9]]

board0 = board[0]
board1 = board[1]
board2 = board[2]

print(board0)
print(board1)
print(board2)

def check_win(current_board):
    # 1. Check Rows
    for i in range(len(current_board)):
        if current_board[i][0] == current_board[i][1] and current_board[i][1] == current_board[i][2]:
            print('Congrats! You won!')
            return True
    # 2. Check Columns
    for j in range(len(current_board)):
        if current_board[0][j] == current_board[1][j] and current_board[1][j] == current_board[2][j]:
            print('Congrats! You won!')
            return True
    # 3. Check Diagonals
    if (current_board[0][0] == current_board[1][1] and current_board[1][1] == current_board[2][2]) or (current_board[0][2] == current_board[1][1] and current_board[1][1] == current_board[2][0]):
        print('Congrats! You won!')
        return True

    return False

def update_board(old_board, number):
    new_board = old_board
    if 1 <= number <= 3:
        ind = old_board[0].index(number)
        new_board[0][ind] = 'X'
    elif 4 <= number <= 6:
        ind = old_board[1].index(number)
        new_board[1][ind] = 'X'
    else:
        ind = old_board[2].index(number)
        new_board[2][ind] = 'X'
    return new_board
    

current_board = board
while not check_win(current_board):
    players_choice = int(input('Where do you want to put your mark? Select a number!'))
    current_board = update_board(current_board, players_choice)
    print(current_board[0])
    print(current_board[1])
    print(current_board[2])