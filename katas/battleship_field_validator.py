"""
Kata: https://www.codewars.com/kata/52bb6539a4cf1b12d90005b7/train/python
"""

battleship_count = 0
cruiser_count = 0
destroyer_count = 0
submarine_count = 0
counter = 0


def categorize_ship():
    global battleship_count
    global cruiser_count
    global destroyer_count
    global submarine_count

    if counter == 1:
        if submarine_count > 4:
            return False
        submarine_count += 1
    if counter == 2:
        if destroyer_count > 3:
            return False
        destroyer_count += 1
    if counter == 3:
        if cruiser_count > 2:
            return False
        cruiser_count += 1
    if counter == 4:
        if battleship_count > 1:
            return False
        battleship_count += 1

    return True


def find_ship(row, column, field):
    global counter

    if check_diagonally(row, column, field):
        return False

    counter = 1

    if check_horizontally(row, column + 1, field):
        for i in range(1, 4):
            if not check_horizontally(row, column + i, field):
                break
            if check_vertically(row + 1, column + i, field):
                return False
            if check_diagonally(row, column + i, field):
                return False
            counter += 1
            mark_point_as_visited(row, column + i, field)

    if check_vertically(row + 1, column, field):
        for i in range(1, 4):
            if not check_vertically(row + i, column, field):
                break
            if check_horizontally(row + i, column + 1, field):
                return False
            if check_diagonally(row + i, column, field):
                return False
            counter += 1
            mark_point_as_visited(row + i, column, field)

    if not categorize_ship():
        return False

    return True


def mark_point_as_visited(row, column, field):
    field[row][column] = 2


def check_diagonally(row, column, field):
    if not (0 <= row < 10) and not (0 <= column < 10):
        return False

    if 0 <= row - 1 < 10 and 0 <= column - 1 < 10 and field[row - 1][column - 1] == 1:
        return True

    if 0 <= row + 1 < 10 and 0 <= column - 1 < 10 and field[row + 1][column - 1] == 1:
        return True

    if 0 <= row - 1 < 10 and 0 <= column + 1 < 10 and field[row - 1][column + 1] == 1:
        return True

    if 0 <= row + 1 < 10 and 0 <= column + 1 < 10 and field[row + 1][column + 1] == 1:
        return True

    return False


def check_horizontally(row, column, field):
    return 0 <= column < 10 and field[row][column] == 1


def check_vertically(row, column, field):
    return 0 <= row < 10 and field[row][column] == 1


def validate_battlefield(field):
    global battleship_count
    global cruiser_count
    global destroyer_count
    global submarine_count
    global counter

    battleship_count = 0
    cruiser_count = 0
    destroyer_count = 0
    submarine_count = 0
    counter = 0

    if not len(field) == 10 and not len(field[0]) == 10:
        return False

    result = False
    for row in range(10):
        for column in range(10):
            if not field[row][column] == 1:
                continue
            result = find_ship(row, column, field)
    return result and battleship_count == 1 and cruiser_count == 2 and destroyer_count == 3 and submarine_count == 4
