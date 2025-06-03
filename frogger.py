"""
File:    frogger.py
Author:  Joseph Cassarino
Date:    11/22/2024
Section: 11
E-mail:  jcassar1@umbc.edu
Description:
  This program is a turn-based adaptation of frogger.
"""

import os


frog = '\U0001318F'

frog_border = f'---{frog}---{frog}---{frog}---{frog}---{frog}---'

# Prompts the user to select a game file, and opens that file to be used throughout the program.
def select_game_file():
    root, directories, files = next(os.walk('.'))

    frog_files = [f for f in files if f.endswith('.frog')]

    if not frog_files:
        print('No .frog files found in the current directory.')
        return None


    print(frog_border)
    print("Welcome to Python Frogger!\n")
    print("Please select a game file: ")
    print(frog_border + '\n')

    frog_file_index = 1

    for file in frog_files:
        print(f'[{frog_file_index}] - {file}')
        frog_file_index += 1

    print(f'\n{frog_border}')

    file_choice = input("Please enter an option or file name: ")

    if not file_choice.isdigit():
        print("Invalid choice. Please enter an int.")
        return select_game_file()

    file_choice = int(file_choice) - 1

    if 0 <= file_choice < len(frog_files):
        return open(frog_files[file_choice], 'r')

    else:
        print('Invalid selection. Please try again.')
        return select_game_file()

# Uses the game file to populate a 2d list representing the game board
def board_setup(game_file):
    game_file.seek(0)
    lines = game_file.readlines()

    board_width = (lines[0].strip().split())[1]

    board = []

    i = 1
    top_row = []
    while i <= int(board_width):
        top_row.append(' ')
        i += 1

    board.append(top_row)

    for i in range(len(lines)-2):
        new_row = lines[i+2].strip()
        board.append(list(new_row))

    i = 1
    bottom_row = []
    while i <= int(board_width):
        bottom_row.append(' ')
        i += 1
    board.append(bottom_row)

    return board

# Uses the game file to assign speeds to their respective rows in a dictionary
def row_speeds(game_file):
    game_file.seek(0)
    lines = game_file.readlines()

    speeds = lines[1].strip().split()

    speed_dict = {}
    for i in range(len(speeds)):
        speed_dict[i+1] = speeds[i]

    return speed_dict

# Uses the game file to get the max number of jumps permitted
def jump_limit(game_file):

    game_file.seek(0)
    lines = game_file.readlines()

    jumps = (lines[0].strip().split())[2]

    return jumps

# Uses the board to build a coordinate grid for the frog. X represents the frog, and o represents an empty spot.
# Frog is placed at width // 2, which is as close to the middle as you can get.
def frog_setup(board):

    y = len(board)
    x = len(board[0]) if y > 0 else 0

    frog_x = x // 2

    frog_position = [['o' for position in range(x)] for position in range(y)]

    if y > 0:
        frog_position[0][frog_x] = 'X'

    return frog_position

# Updates the board every turn, based on the speeds assigned to each row.
def update_board(board, speeds):

    rows = len(board)

    for i in range(1,rows-1):
        new_row = board[i][-(int(speeds[i])):] + board[i][:-(int(speeds[i]))]
        board[i] = new_row

    return board

# Uses the data held in the frog_position and board lists to make the board that is shown to the user.
# Takes the frog's position and "overlays" it on top of the board list.
# This allows both lists to remain unchanged when putting the frog on top of the board.
def display_board(board, frog_position):

    rows = len(board)
    columns = len(board[0]) if rows > 0 else 0

    combined_board = []

    for i in range(rows):

        combined_row = []

        for t in range(columns):

            if frog_position[i][t] == 'X':
                combined_row.append('0')

            else:
                combined_row.append(board[i][t])
        combined_board.append(combined_row)

    for row in combined_board:
        print(''.join(row))

    return combined_board

# Takes in the user's chosen action and moves the frog across the frog_position list accordingly
# If the user chooses to jump, it calls frog_jump
def move_frog(frog_position, move, jumps):

    rows = len(frog_position)
    columns = len(frog_position[0]) if rows > 0 else 0

    current_y, current_x = 0, 0

    for i in range(rows):
        for t in range(columns):
            if frog_position[i][t] == 'X':
                current_y, current_x = i, t

    moves = {
        "w": (-1, 0),
        "a": (0, -1),
        "s": (1, 0),
        "d": (0, 1)
    }

    if move in moves:
        y_change, x_change = moves[move]
        new_row = current_y + y_change
        new_column = current_x + x_change

        if 0 <= new_row < rows and 0 <= new_column < columns:

            frog_position[current_y][current_x] = "o"
            frog_position[new_row][new_column] = "X"

        else:
            print("Invalid move: Out of bounds")

    elif move.split()[0] == 'j':
        jump_y = int(move.split()[1])
        jump_x = int(move.split()[2]) - 1
        frog_position, jumps = frog_jump(frog_position, jump_y, jump_x, jumps)


    else:
        print("Invalid move: Unknown key")

    return frog_position, jumps

# Allows the frog to jump to a position one row and any number of columns away>
# Must be within the bounds of the board
def frog_jump(frog_position, jump_y, jump_x, jumps):

    if jumps <= 0:
        print('No more jumps left! You cannot jump anymore.')
        return frog_position

    current_y, current_x = -1, -1
    for i in range(len(frog_position)):
        for t in range(len(frog_position[i])):
            if frog_position[i][t] == 'X':
                current_y, current_x = i, t

    if abs(jump_y - current_y) > 1 or jump_y < 0 or jump_y >= len(frog_position):
        print("Invalid jump! You can only jump to the same row, one row above, or one row below.")
        return frog_position

    if jump_x < 0 or jump_x >= len(frog_position[0]):
        print("Invalid jump! Target out of range.")
        return frog_position

    frog_position[current_y][current_x] = 'o'
    frog_position[jump_y][jump_x] = 'X'

    jumps -= 1
    print(f'Jumps left: {jumps}')

    return frog_position, jumps

# Checks the frog's position against the board to see if the frog has collided with an X or not.
# Also checks if the frog is at the safe row on the bottom.
# If the frog is on the same spot as an X, then the player fails
# If the frog is on the bottom row, the player wins
def win_loss_check(board, frog_position, move):

    rows = len(board)
    columns = len(board[0]) if rows > 0 else 0

    frog_y, frog_x = 0 , 0
    for i in range(rows):
        for t in range(columns):
            if frog_position[i][t] == "X":
                frog_y = i
                frog_x = t

    if frog_y == rows - 1:
        print('Victory! Frog lives to cross another day')
        return False

    if board[frog_y][frog_x] == 'X':
        print('Frog has failed to cross the road.')
        return False

    else:
        return True

# Calls all "setup" functions to build the base state of the game.
# Begins a while loop that repeats everything that happens in a turn.
# This loop is only broken once the player wins or loses.
def play_frogger():

    # Setting up the game
    game_file = select_game_file()

    speeds = row_speeds(game_file)

    jumps = int(jump_limit(game_file))

    board = board_setup(game_file)

    frog_position = frog_setup(board)

    print(f'{frog_border}')

    display_board(board, frog_position)

    game = win_loss_check(board, frog_position, None)

    turn = 0

    while game is True:

        turn += 1

        print(f'{frog_border}')

        print(f'Turn {turn}')

        print("How would you like to move this turn?")
        print("[W] - [A] - [S] - [D] - [J]")
        move = input()

        print(f'{frog_border}')

        new_frog_position, jumps = move_frog(frog_position, move, jumps)

        updated_board = update_board(board, speeds)

        display_board(updated_board, new_frog_position)

        game = win_loss_check(updated_board, new_frog_position, move)

        if not game:
            print('Game over!')



if __name__ == '__main__':
    play_frogger()