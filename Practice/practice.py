# Make a list of 20 random integers from 1-50.
# Make a second list the same way.
# Print all of the reocurring numbers.
# Print all of the even numbers.

import random
# numbers1 = []
# numbers2 = []

# for numbers in range(20):
#     numbers1.append(random.randint(1, 50))
# for numbers in range(20):
#     numbers2.append(random.randint(1, 50))

# print(numbers1)
# print(numbers2)

# print('Recurring: ', end='')
# for numbers in numbers2:
#     if numbers in numbers1:
#         print(numbers, end=', ')

# print('Even: ', end='')
# for numbers in numbers1 or numbers2:
#     if numbers % 2 == 0:
#         print(numbers, end=', ')


# Make a number guessing game.

# counter = 0
# guess = 0
# secret = random.randint(1, 100)

# while guess != secret:
#     guess = int(input('What is your guess?: '))
#     counter = counter + 1

#     if guess > secret:
#         print('Go down.')

#     elif guess < secret:
#         print('Go up.')

#     else:
#         print('Correct! Answer found in', counter, 'guesses.')

# print('GAME OVER')


# Ask user for name and gpa and then print.

# file = open('gpa.txt', 'r')
# existing = file.read()
# name = input('Enter your name: ')
# gpa = float(input('Enter your gpa: '))

# if name in existing:
#     print('Error, name already exists.')
# else:
#     file = open('gpa.txt', 'a')

#     file.write(f'{name}, ')
#     file.write(f'{gpa}\n')


# Tic Tac Toe Game

# def display_board(board):
#     for r in range(0, 3):
#         for c in range(0, 3):
#             print(board[r][c], end=' ')
#         print()


# def winner(board, current_player):
#     for r in range(3):
#         if board[r][0] == current_player and board[r][1] == current_player and board[r][2] == current_player:
#             return True
#     for c in range(3):
#         if board[0][c] == current_player and board[1][c] == current_player and board[2][c] == current_player:
#             return True


# board = [
#     ['-', '-', '-'],
#     ['-', '-', '-'],
#     ['-', '-', '-']
# ]

# current_player = 'X'
# moves = 0


# while True:
#     display_board(board)

#     print(current_player, 'plays')

#     row = int(input('Row: '))
#     col = int(input('Column: '))

#     if row > 0 and row < 4 and col > 0 and row < 4:
#         if board[row - 1][col - 1] == '-':
#             board[row - 1][col - 1] = current_player
#             moves += 1

#             if winner(board, current_player):
#                 display_board
#                 print(current_player, 'wins!')
#                 break

#             if moves == 9:
#                 display_board
#                 print("It is a tie.")
#                 break

#             if current_player == 'X':
#                 current_player = 'O'
#             else:
#                 current_player = 'X'

#         else:
#             print("Space not availible.")

#     else:
#         print("Invalid option.")


# Hangman Game

# word = ["one", "two", "three"]

# last = len(word) - 1
# r = random.randint(0, last)
# secret = word[r]
# print(secret)

# wrong = []
# correct = []

# while True:

#     guess = input("Guess a letter: ")
#     moves = 0

#     if guess in secret:
#         if guess not in correct:
#             correct.append(guess)
#             moves += 1
#             print(correct)
#             continue

#         else:
#             if guess not in wrong:
#                 wrong.append(guess)
#                 print(wrong)
#                 moves += 1
#                 continue

#     if moves == 5:
#         print("Game Over!")
#         break


# Tic Tac Toe again

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


board = [
    ['-', '-', '-'],
    ['-', '-', '-'],
    ['-', '-', '-']
]

current_player = 'X'

while True:

    display_board(board)

    row = input("Enter row: ")
    col = input("Enter column: ")

    if row > 0 and row < 4 and col > 0 and col < 4:
        if board[row - 1][col - 1] == '-':
            board[row - 1][col - 1] = current_player
            display_board(board)

            if winner(board, current_player):
                print(current_player, 'wins!')
                display_board
                break

            if current_player == 'X':
                current_player = 'O'
