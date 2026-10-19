# In Class Examples:
# Hangman Game
import random


def create_display_from_secret(secret, correct):
    display = secret[0]
    for i in range(1, len(secret)-1):
        if secret[i] in correct:
            display = display + secret[i]
        else:
            display = display + '_'
    display = display + secret[-1]
    return display


words = ['programming', 'debugging',
         'inheritance', 'polymorphism', 'composition']

last = len(words) - 1
r = random.randint(0, last)
secret = words[r]

wrong = []
correct = []

display = create_display_from_secret(secret, correct)

while True:
    print(display)

    guess = input("Guess a letter: ")

    if len(guess) > 1:
        print("Enter one letter only.")
        continue

    if guess in secret:
        if guess not in correct:
            correct.append(guess)
    else:
        if guess not in wrong:
            wrong.append(guess)

    display = create_display_from_secret(secret, correct)

    if display == secret:
        print("Found")
        break

    if len(wrong) == 6:
        print("You are hanged")
        break

print("GAME OVER")


# Tic Tac Toe

def display_board(board):
    for r in range(0, 3):
        for c in range(0, 3):
            print(board[r][c], end='')
        print()


board = [
    ['-', '-', '-'],
    ['-', '-', '-'],
    ['-', '-', '-']
]

current_user = 'X'

while True:
    display_board(board)

    print(f'{current_user} plays')
    row = int(input("Row: "))
    col = int(input("Column: "))

    if row > 0 and row < 4 and col > 0 and col < 4:
        if board[row-1][col-1] == '-':
            board[row-1][col-1] = current_user

            if current_user == 'X':
                current_user = 'O'
            else:
                current_user = 'X'

        else:
            print(f'Cell at {row}:{col} is not availible')
    else:
        print("invalid row/column.")
