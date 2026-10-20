# Tic Tac Toe Game
def display_board(board):
    for r in range(0, 3):
        for c in range(0, 3):
            print(board[r][c], end=' ')
        print()


def winner(board, current_player):
    for r in range(3):
        if board[r][0] == current_player and board[r][1] == current_player and board[r][2] == current_player:
            return True

    for c in range(3):
        if board[0][c] == current_player and board[1][c] == current_player and board[2][c] == current_player:
            return True

    if board[0][0] == current_player and board[1][1] == current_player and board[2][2] == current_player:
        return True

    if board[2][0] == current_player and board[1][1] == current_player and board[0][2] == current_player:
        return True


board = [
    ['-', '-', '-'],
    ['-', '-', '-'],
    ['-', '-', '-']
]

current_player = 'X'
taken_spaces = 0


while True:
    display_board(board)

    print(current_player, 'plays')

    row = int(input('What row?: '))
    column = int(input('What column?: '))

    if row > 0 and row < 4 and column > 0 and column < 4:
        if board[row-1][column-1] == '-':
            board[row-1][column-1] = current_player
            taken_spaces += 1

            if winner(board, current_player):
                display_board(board)
                print(current_player, "wins!")
                break

            if taken_spaces == 9:
                display_board(board)
                print("It is a tie.")
                break

            if current_player == 'X':
                current_player = 'O'
            else:
                current_player = 'X'

        else:
            print('Space is not availible')
    else:
        print('Invalid choice')


# Convert binary number to decimal format.

binary = input("Type a binary value: ")
letter = 0

# Set the max power value, as len(binary) - 1 let's call it pow_val
pow_val = len(binary) - 1

# Init total to zero
total = 0

# Loop for each letter in binary
while True:

    if binary[letter] == '1':
        decimal = 2 ** pow_val
        total = total + pow_val

    pow_val = pow_val - 1
    letter = letter + 1
    break

print("Total Value: ", decimal)
