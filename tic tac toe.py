#create a board
board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]
is_playing = True

winner = None


 

current_player = "X"

#display the board
def display_board():
    print(
        "\n ",board[0], "|", board[1], "|", board[2], "\n ",
        board[3], "|", board[4], "|", board[5], "\n ",
        board[6], "|", board[7], "|", board[8]
    )

def play_game():
    display_board()
    while is_playing:

        ask_position()

        change_player()

        check_game_over()

def ask_position():
    position = int(input("select a number beetwin 1 and 9 : "))
    position -= 1


def change_player():
    global current_player
    if current_player == "X":
        current_player = "O"
    else:
        current_player = "X"
    print (current_player)
change_player()

def check_game_over():
    return

play_game()