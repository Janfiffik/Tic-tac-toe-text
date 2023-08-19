import random
import field as f
import time
P1 = "O"
P2 = "X"


def start_first():
    player1 = random.choice(range(2))
    if player1 == 0:
        p1 = P1
        p2 = P2
    else:
        p1 = P2
        p2 = P1
    return p1, p2


def game_on():
    game_is_on = True
    while game_is_on:
        game = (input("Do you want continue? Y/N\n")).upper()
        if game == "N":
            game_is_on = False
        else:
            game_is_on = True
        return game_is_on


def check_rows(game_field, char):
    for row in game_field:
        char_count = 0
        for i in row:
            if i == char:
                char_count += 1
                if char_count == 3:
                    print(f"Player: {char} wins.")
                    return False
            else:
                char_count = 0

    else:
        return True


def check_diagonal(game_field, char):  # Nedokoncene
    row = 0
    col = 0
    count = 0
    row1 = 2
    col1 = 0
    count1 = 0
    for j in range(len(game_field)):
        for i in game_field[row][col]:
            if i == char:
                count += 1
                row += 1
                col += 1
                if count == 3:
                    print(f"Player: {char} wins.")
                    return False

    for j in range(len(game_field)):
        for i in game_field[row1][col1]:
            if i == char:
                count1 += 1
                row1 -= 1
                col1 += 1
                if count1 == 3:
                    print(f"Player: {char} wins.")
                    return False
    else:
        return True


def check_columns(game_is_on, game_field, char):
    end_loop = True
    while end_loop:
        for i in range(len(game_field)):
            count = 0
            for j in range(len(game_field[i])):
                if game_field[j][i] == char:
                    count += 1
                    if count == 3:
                        print(f"Player: {char} wins")
                        return False
                else:
                    count = 0
                if not end_loop:
                    break
        else:
            return True

    return game_is_on


def check_empty(game_field, char):
    field = True
    while field:
        try:
            row = int(input("Enter row. Max 3 :\n")) - 1
            col = int(input("Enter column. Max 3:\n")) - 1
            if game_field[row][col] != "_":
                print("Position is not empty.\nTry again :)")
                continue
            game_field[row][col] = char
        except:
            print("You are out of field, field is 3X3")
            continue
        return game_field


def check_tie(field):
    count = 0
    for row in field:
        for i in row:
            if i == "_":
                count += 1
    if count == 0:
        print("It is tie :)")
        return False
    else:
        return True


def gameplay(players, game_field):
    game_is_on = True
    while game_is_on:
        char1 = players[0]
        char2 = players[1]

        print(f"Player: ____{char1}____ turn.")
        game_field = check_empty(game_field, char1)
        f.show_playground(game_field)
        game_on_row1 = check_rows(game_field, char1)
        game_on_column1 = check_columns(game_is_on, game_field, char1)
        game_diagonal1 = check_diagonal(game_field, char1)
        game_tie1 = check_tie(game_field)
        if not game_on_row1 or not game_on_column1 or not game_tie1 or not game_diagonal1:
            break
        time.sleep(1)

        print(f"Player: ____{char2}____ turn.")
        game_field = check_empty(game_field, char2)
        f.show_playground(game_field)
        game_on_row2 = check_rows(game_field, char2)
        game_on_column2 = check_columns(game_is_on, game_field, char2)
        game_tie2 = check_tie(game_field)
        game_diagonal2 = check_diagonal(game_field, char2)
        if not game_on_row2 or not game_on_column2 or not game_tie2 or not game_diagonal2:
            break
        time.sleep(1)
