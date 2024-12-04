from ASCII_Art import menu


def get_menu_option():
    menu()
    print('''
                        Please choose a mode:

                        1. Human vs Human
                        2. Random AI vs Random AI
                        3. Human vs Random AI
                        4. Human vs Unbeatable AI

  ''')
    inp = ""
    while True:
        inp = input("> ")
        if inp not in ["1", "2", "3", "4"]:
            print("This doesn't look like a number in the range.")
        else:
            return int(inp)


if __name__ == "__main__":
    # run this file to test you have implemented correctly the function
    option = get_menu_option()
    print(option) # if the user selected 1, it should print 1