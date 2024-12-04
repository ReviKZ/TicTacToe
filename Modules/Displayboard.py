def display_board(board):
    print(f"""
    0| 1 | 2 | 3 |
    -+---+---+---+
    A| {board[0][0]} | {board[0][1]} | {board[0][2]} |
    -+---+---+---+
    B| {board[1][0]} | {board[1][1]} | {board[1][2]} |
    -+---+---+---+
    C| {board[2][0]} | {board[2][1]} | {board[2][2]} |
    -+---+---+---+
    """)
