from ASCII_Art import end


def get_human_coordinates(board, current_player):
    guess = ""
    # Lists for translating input coordinates to board coordinates
    horizontal_axis = ["1", "2", "3"]
    vertical_axis = ["a", "b", "c"]

    while True:
        guess = input("Please choose a location!")

        # Handle quit
        if guess.lower() == "quit":
            end()
            quit()

        # Validation
        if (len(guess) == 2) and (guess[0].lower() in vertical_axis) and (guess[1] in horizontal_axis):
            # Translate coordinates to list indexes
            column = horizontal_axis.index(guess[1])
            row = vertical_axis.index(guess[0].lower())

            # Check if guessed coordinate is occupied
            if board[row][column] != ".":
                print("Coordinate already occupied!")
            else:
                # Output tuple
                return (row, column)

        else:
            print("Invalid coordinate, please try again!")

if __name__ == "__main__":
    # run this file to test you have implemented correctly the function
    board_1 = [
        ["X", "X", "."],
        ["X", ".", "."],
        ["X", "X", "."],
    ]
    coordinates = get_human_coordinates(board_1, "X")
    print(coordinates) # the only possible returned value can be (0,2) or (1,1) or (1, 2) or (2,2) because they are the only valid ones