import random


def get_random_ai_coordinates(board, current_player):
    free_spaces = []

    # Loop through the board
    for row in range(len(board)):
        for column in range(len(board[row])):
            # Add empty coordinates to free_spaces list
            if board[row][column] == ".":
                free_spaces.append((row, column))

    if len(free_spaces) == 0:
        return None
    # Return random free coordinate
    else:
        return random.choice(free_spaces)


if __name__ == "__main__":
    # run this file to test you have implemented correctly the function
    board_1 = [
      ["O", "O", "."],
      ["X", "O", "."],
      ["X", "X", "O"],
    ]
    print(get_random_ai_coordinates(board_1, "X")) # the printed coordinate should be only (0,2) or (1,2)
    print(get_random_ai_coordinates(board_1, "X")) # the printed coordinate should be only (0,2) or (1,2)
    print(get_random_ai_coordinates(board_1, "X")) # the printed coordinate should be only (0,2) or (1,2)

    board_2 = [
      ["O", "X", "X"],
      ["X", "O", "X"],
      ["X", "O", "X"],
    ]
    print(get_random_ai_coordinates(board_2, "O")) # the printed coordinate should be None