def is_board_full(board):
    x_count = sum([i.count("X")for i in board])
    o_count = sum([j.count("O")for j in board])
    taken = x_count+o_count
    if taken == 9:
        return True
    else:
        return False


if __name__ == "__main__":
  # run this file to test you have implemented correctly the function
  board_1 = [
    ["X", "O", "."],
    ["X", "O", "."],
    ["X", "X", "O"],
  ]
  print(is_board_full(board_1)) # should return False

  board_2 = [
    [".", "O", "O"],
    [".", "O", "X"],
    [".", "X", "X"],
  ]
  print(is_board_full(board_2)) # should return False

  board_3 = [
    ["O", "O", "X"],
    ["O", "X", "O"],
    ["O", "X", "X"],
  ]
  print(is_board_full(board_3)) # should return True