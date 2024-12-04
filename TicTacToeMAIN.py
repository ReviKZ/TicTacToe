import os
import time
from Modules import ASCII_Art
from Modules.Displayboard import display_board
from Modules.MenuDisplay import get_menu_option
from Modules.EmptyBoard import get_empty_board
from Modules.HumanInput import get_human_coordinates
from Modules.RandomAIInput import get_random_ai_coordinates
from Modules.UnbeatableAIInput import get_unbeatable_ai_coordinates
from Modules.CheckForWin import get_winning_player
from Modules.CheckBoardFull import is_board_full

HUMAN_VS_HUMAN = 1
RANDOM_AI_VS_RANDOM_AI = 2
HUMAN_VS_RANDOM_AI = 3
HUMAN_VS_UNBEATABLE_AI = 4


def cls():
    os.system('cls' if os.name == 'nt' else 'clear')


def play_again():
    answer = input("Would you like to play again? (y/n)")
    if answer.lower() == "y":
        main()
    else:
        cls()
        ASCII_Art.end()
        quit()


def main():
    cls()
    game_mode = get_menu_option()
    board = get_empty_board()
    is_game_running = True
    count = 0
    players = ["X", "O"]

    # Main gameplay loop
    while is_game_running:
        cls()
        print(f"Round number {count + 1}\n")
        display_board(board)

        # Change players
        current_player = players[count % 2]
        print(f"\nCurrent player is {current_player}\n")

        if game_mode == 1:
            row, column = get_human_coordinates(board, current_player)
            board[row][column] = current_player
        elif game_mode == 2:
            time.sleep(1)
            row, column = get_random_ai_coordinates(board, current_player)
            board[row][column] = current_player
        elif game_mode == 3:
            if current_player == "X":
                row, column = get_human_coordinates(board, current_player)
                board[row][column] = current_player
            else:
                row, column = get_random_ai_coordinates(board, current_player)
                board[row][column] = current_player
        elif game_mode == 4:
            if current_player == "X":
                row, column = get_human_coordinates(board, current_player)
                board[row][column] = current_player
            else:
                row, column = get_unbeatable_ai_coordinates(board, current_player, count)
                board[row][column] = current_player

        if get_winning_player(board) is not None:
            cls()
            display_board(board)
            if get_winning_player(board) == "X":
                ASCII_Art.x_wins()
            elif get_winning_player(board) == "O":
                ASCII_Art.o_wins()
            play_again()

        its_a_tie = is_board_full(board)
        if its_a_tie is True:
            cls()
            display_board(board)
            ASCII_Art.tie()
            play_again()

        count += 1


if __name__ == "__main__":
    main()
