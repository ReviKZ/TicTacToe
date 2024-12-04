def get_winning_player(board):
    if board[0][0] == board[0][1] == board[0][2] != '.':  # across the top
        return board[0][0]
    elif board[1][0] == board[1][1] == board[1][2] != '.':  # across the middle
        return board[1][0]
    elif board[2][0] == board[2][1] == board[2][2] != '.':  # across the bottom
        return board[2][0]
    elif board[2][0] == board[1][0] == board[0][0] != '.':  # down the left side
        return board[0][0]
    elif board[2][1] == board[1][1] == board[0][1] != '.':  # down the middle
        return board[0][1]
    elif board[2][2] == board[1][2] == board[0][2] != '.':  # down the right side
        return board[0][2]
    elif board[0][0] == board[1][1] == board[2][2] != '.':  # diagonal
        return board[0][0]
    elif board[2][0] == board[1][1] == board[0][2] != '.':  # diagonal
        return board[2][0]


if __name__ == "__main__":
  # run this file to test you have implemented correctly the function
  board_1 = [
    ["X", "O", "."],
    ["X", "O", "."],
    ["X", "X", "O"],
  ]
  print(get_winning_player(board_1)) # should return "X"

  board_2 = [
    ["X", "O", "O"],
    ["X", "O", "."],
    ["O", "X", "X"],
  ]
  print(get_winning_player(board_2)) # should return "O"

  board_3 = [
    ["O", "O", "."],
    ["O", "X", "."],
    [".", "X", "."],
  ]
  print(get_winning_player(board_3)) # should return None