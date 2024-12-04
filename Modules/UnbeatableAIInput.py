import random
from RandomAIInput import get_random_ai_coordinates


def winning_move_available(board, current_player):
    # Check if there are two matching tokens in a row/column/diagonal

    # Check the rows:
    for row in board:
        # Check if there is a free coordinate
        if "." in row:
            # If two cells match return coordinates of the third
            if row.count(current_player) == 2:
                return (board.index(row), row.index("."))

    # Check the columns the same way
    for column_number in range(0, 3):
        column = [board[0][column_number], board[1][column_number], board[2][column_number]]
        if "." in column:
            if column.count(current_player) == 2:
                return (column.index("."), column_number)

    # Check the two axis the same way
    diagonal1 = [board[0][0], board[1][1], board[2][2]]
    diagonal2 = [board[0][2], board[1][1], board[2][0]]

    if "." in diagonal1:
        if diagonal1.count(current_player) == 2:
            return (diagonal1.index("."), diagonal1.index("."))

    if "." in diagonal2:
        if diagonal2.count(current_player) == 2:
            index = diagonal2.index(".")
            if index == 0:
                return (0, 2)
            elif index == 1:
                return (1, 1)
            elif index == 2:
                return (2, 0)
    return None


def get_unbeatable_ai_coordinates(board, current_player, count):

    # Win the game if possible in one move
    if winning_move_available(board, "O") is not None:
        return winning_move_available(board, "O")
    # Keep the other player from winning
    if winning_move_available(board, "X") is not None:
        return winning_move_available(board, "X")

    # On AI's first round put in middle cell if not taken
    if count == 1:
        if board[1][1] == ".":
            return (1, 1)
        # Otherwise choose a corner location
        else:
            choices = [0, 2]
            coordinates = random.choices(choices, k=2)
            return coordinates

    # Logic for AI's second round
    # Put O in row or column where O is already located if X takes middle cell
    if count == 3:
        if board[1][1] == "X":
            corner_coordinates = [(0, 0), (0, 2), (2, 0), (2, 2)]
            for row, column in corner_coordinates:
                if board[row][column] == ".":
                    return (row, column)
        # If AI already has the middle cell, prevent AI from picking a corner location
        elif board[1][1] == "O":
            corner_coordinates = [(1, 0), (0, 1), (2, 1), (1, 2)]
            for row, column in corner_coordinates:
                if board[row][column] == ".":
                    return (row, column)

    # If no direct paths to victory are found, return random coordinates
    return get_random_ai_coordinates(board, current_player)


if __name__ == "__main__":
    # run this file to test you have implemented correctly the function
    board_1 = [
        ["X", ".", "."],
        [".", "X", "."],
        [".", ".", "O"],
    ]
    print(get_unbeatable_ai_coordinates(board_1, "X", 4)) # the printed coordinate should always be (0, 0)

    board_2 = [
        ["X", "O", "O"],
        ["X", "X", "O"],
        ["O", "O", "X"],
    ]
    print(get_unbeatable_ai_coordinates(board_2, "O", 9)) # the printed coordinate should always be (1, 1)

    board_3 = [
        [".", ".", "."],
        [".", ".", "."],
        [".", ".", "."],
    ]
    print(get_unbeatable_ai_coordinates(board_3, "X", 0)) # the printed coordinate should be either (0, 2) or (2, 0)