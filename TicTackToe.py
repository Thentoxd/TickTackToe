import math
import time

game_status = "ACTIVE"
player_turn = 1
move = ""


board = [
    ["", "", ""], # 1
    ["", "", ""], # 2
    ["", "", ""]  # 3

    # A   B   C
]

def translate_code_to_board_index(code):
    letter = code[0]
    number = int(code[1])

    if letter == "A":
        return number - 1, 0
    elif letter == "B":
        return number - 1, 1
    elif letter == "C":
        return number - 1, 2
    else:
        return "null"

def translate_board_index_to_code(board_index):
    if board_index[1] == 0:
        return "A" + str(int(board_index[0]) + 1)
    elif board_index[1] == 1:
        return "B" + str(int(board_index[0]) + 1)
    elif board_index[1] == 2:
        return "C" + str(int(board_index[0]) + 1)

def input_code_to_board(code):
    translation = translate_code_to_board_index(code)

    if player_turn == 1:
        board[translation[0]][translation[1]] = "X"
    elif player_turn == 2:
        board[translation[0]][translation[1]] = "O"

def get_value_from_code(code):
    translation = translate_code_to_board_index(code)

    return board[translation[0]][translation[1]]

def get_code_relative_to(board_code, x_displacement, y_displacement):
    board_index = translate_code_to_board_index(board_code)

    return translate_board_index_to_code((board_index[0] + x_displacement, board_index[1] + -y_displacement))

def get_displacement(board_code_start, board_code_finish):
    board_index_start = translate_code_to_board_index(board_code_start)
    board_index_finish = translate_code_to_board_index(board_code_finish)

    x_displacement = (int(board_index_finish[0]) - int(board_index_start[0]))
    y_displacement = -(int(board_index_finish[1] - int(board_index_start[1])))

    return x_displacement, y_displacement


def is_valid_row(board_code_start, board_code_finish):
    if is_corner(board_code_start) and is_corner(board_code_finish) and int(board_code_start[1]) != int(board_code_finish[1]): # Diagonal Row
        displacement = get_displacement(board_code_start, board_code_finish)

        x_displacement = displacement[0]
        y_displacement = displacement[1]

        final_value = (y_displacement * y_displacement) + (x_displacement * x_displacement)

        return math.sqrt(final_value) == math.sqrt(8)

    return int(board_code_start[1]) == int(board_code_finish[1]) or str(board_code_start[0]) == str(board_code_finish[0]) # Straight Row

def get_codes_in_row(board_code_start, board_code_finish):
    displacement = get_displacement(board_code_start, board_code_finish)
    x_displacement = displacement[0]
    y_displacement = displacement[1]

    if is_corner(board_code_start) and is_corner(board_code_finish) and int(board_code_start[1]) != int(board_code_finish[1]): # Diagonal
        board_start_translation = translate_code_to_board_index(board_code_start)
        middle_value = (int((board_start_translation[0] + (x_displacement / 2))), int((board_start_translation[1] - (y_displacement / 2))))

        middle_value = translate_board_index_to_code(middle_value)

        return board_code_start, middle_value, board_code_finish

    elif int(board_code_start[1]) == int(board_code_finish[1]) or str(board_code_start[0]) == str(board_code_finish[0]):
        board_code_start_translation = translate_code_to_board_index(board_code_start)
        board_code_finish_translation = translate_code_to_board_index(board_code_finish)

        board_start_x = board_code_start_translation[0]
        board_start_y = board_code_start_translation[1]
        board_finish_x = board_code_finish_translation[0]
        board_finish_y = board_code_finish_translation[1]

        middle_code = None

        if board_start_x == board_finish_x:
            middle_code = translate_board_index_to_code(((board_finish_x - board_start_x), board_start_y))

        elif board_start_y == board_finish_y:
            middle_code = translate_board_index_to_code(((board_start_y - board_finish_y), board_start_x))

        return board_code_start, middle_code, board_code_finish



def is_corner(board_code):
    letter = board_code[0]
    number = int(board_code[1])

    if letter == "A" or letter == "C" and number == 1 or number == 3:
        return True

    return False
def print_board():
    print("")
    print("A    " + get_value_from_code("A1") + "  |   " + get_value_from_code("A2") + "  |   " + get_value_from_code("A3") + "  |")
    print("B    " + get_value_from_code("B1") + "  |   " + get_value_from_code("B2") + "  |   " + get_value_from_code("B3") + "  |")
    print("C    " + get_value_from_code("C1") + "  |   " + get_value_from_code("C2") + "  |   " + get_value_from_code("C3") + "  |")
    print("")
    print("    1" + "  |  " + "2" + "  | " + "  3 |")

    print(board)

print("Welcome to Tick Tack Toe!")

print(str(get_codes_in_row("C1", "A3")))

while game_status == "ACTIVE":
    print("It's Player " + str(player_turn) + "'s turn!")
    time.sleep(1)
    print_board()

    print("")
    input_code_to_board(input("What is your move? ").upper())

    if player_turn == 2:
        player_turn = 1
    elif player_turn == 1:
        player_turn = 2

