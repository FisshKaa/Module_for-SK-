def welcome():
    print("-"*25)
    print("""Приветствуем вас
            в игре
'Крестики -Нолики'""")
    print("-" * 25)
    print("""формат ввода: x y 
x - номер строки
н - номер столбца """)

    print("-" * 25)

def board_game():
    print(f"      0   1   2")
    for i in range(3):
        row_info = "  ".join(table[i])
        print(f"{i}    {row_info}")

def answear():
    while True:
        cord = input("      Введите 2 координаты через пробел: ").split()

        if len(cord) != 2:
            print(" Введите 2 координаты! ")
            continue

        x, y = cord

        if not(x.isdigit()) or not(y.isdigit()):
            print(" Введите числа! ")
            continue

        x, y = int(x), int(y)

        if 0 > x or x > 2 or 0 > y or y > 2:
            print(" Координаты вне диапазона! ")
            continue

        if table[x][y] != " ":
            print(" Клетка занята! ")
            continue

        return x, y

def check_win():
    win_cord = (((0, 0), (0, 1), (0, 2)), ((1, 0), (1, 1), (1, 2)), ((2, 0), (2, 1), (2, 2)),
                ((0, 2), (1, 1), (2, 0)), ((0, 0), (1, 1), (2, 2)), ((0, 0), (1, 0), (2, 0)),
                ((0, 1), (1, 1), (2, 1)), ((0, 2), (1, 2), (2, 2)))
    for cord in win_cord:
        symbols = []
        for c in cord:
            symbols.append(table[c[0]][c[1]])
        if symbols == ["X", "X", "X"]:
            print("Выиграли Крестики!!!")
            return True
        if symbols == ["0", "0", "0"]:
            print("Выиграли Нолики!!!")
            return True
    return False




welcome()
table = [[" ", " ", " "] for i in range(3)]
step = 0
while True:
    step += 1
    board_game()

    if step % 2 == 1:
        print(" Ходит Крестик ")
    else:
        print(" Ходит Нолик ")

    x, y = answear()

    if step % 2 == 1:
        table[x][y] = "X"
    else:
        table[x][y] = "O"

    if check_win():
        break

    if step == 9:
        print("Ничья")
        break

