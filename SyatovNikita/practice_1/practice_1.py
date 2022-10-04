# `random` module is used to shuffle field, see:
# https://docs.python.org/3/library/random.html#random.shuffle

import random

# Empty tile, there's only one empty cell on a field:
EMPTY_MARK = 'x'

# Dictionary of possible moves if a form of:
# key -> delta to move the empty tile on a field.
MOVES = {
    'w': -4,
    's': 4,
    'a': -1,
    'd': 1,
}

def shuffle_field():
    """
    This function is used to create a field at the very start of the game.

    :return: list with 16 randomly shuffled tiles,
        one of which is a empty space.
    """
    CORRECT_POSITION = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, EMPTY_MARK)
    MOVE_KEYS = ('w', 's', 'a', 'd')

    field = list(CORRECT_POSITION)
    for i in range(100):
        perform_move(field, random.choice(MOVE_KEYS))

    return list(field)


def print_field(field):
    """
    This function prints field to user.

    :param field: current field state to be printed.
    :return: None
    """
    i = 0
    while i < 16:
        print(str(field[i]) + "\t" + str(field[i+1]) + "\t" + str(field[i+2]) + "\t" + str(field[i+3]))
        i += 4


def is_game_finished(field):
    """
    This function checks if the game is finished.

    :param field: current field state.
    :return: True if the game is finished, False otherwise.
    """
    finish_field = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, EMPTY_MARK]
    for i in range(0, 15):
        if field[i] == finish_field[i]:
            continue
        else:
            return False
    return True


def perform_move(field, key):
    """
    Moves empty-tile inside the field.

    :param field: current field state.
    :param key: move direction.
    :return: new field state (after the move)
        or `None` if the move can't me done.
    """
    id = field.index(EMPTY_MARK)
    if (id + MOVES[key]) < 0:
        return None
    elif (id + MOVES[key]) > len(field):
        return None
    elif (id % 4 == 0) and (MOVES[key] == -1):
        return None
    elif ((id + MOVES[key]) % 4 == 0) and (MOVES[key] == 1):
        return None
    else:
        field[id] = field[id + MOVES[key]]
        field[id + MOVES[key]] = EMPTY_MARK
        return field



def handle_user_input():
    """
    Handles user input.

    List of accepted moves:
        'w' - up,
        's' - down,
        'a' - left,
        'd' - right

    :return: <str> current move.
    """
    move = input("enter next step:\n")
    if move not in MOVES.keys():
        print("Error")
        handle_user_input()
        return 0

    return str(move)


def main():
    """
    The main function. It starts when the program is called.

    It also calls other functions.
    :return: None
    """
    field = shuffle_field()
    while not is_game_finished(field):
        print_field(field)
        move = handle_user_input()
        if move != 0:
            perform_move(field, move)
    print("WIN!!!!")

if __name__ == '__main__':
    main()
