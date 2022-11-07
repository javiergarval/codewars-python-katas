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

    field[row][column] = 2

    counter = 0
    for i in range(0, 4):
        if continues_horizontally(row, column + i, field):
            counter += 1
            field[row][column + i] = 2
            if continues_vertically(row + 1, column + i, field):
                return False

        if continues_vertically(row + i, column, field):
            counter += 1
            field[row + i][column] = 2
            if continues_horizontally(row + i, column + 1, field):
                return False

    if not categorize_ship():
        return False

    counter = 0
    return True


def continues_horizontally(row, column, field):
    return column < 10 and field[row][column] == 1


def continues_vertically(row, column, field):
    return row < 10 and field[row][column] == 1


def validate_battlefield(field):
    if not len(field) == 10 and not len(field[0]) == 10:
        return False

    result = False
    for row in range(10):
        for column in range(10):
            if not field[row][column] == 1:
                continue
            result = find_ship(row, column, field)
    return result and battleship_count == 1 and cruiser_count == 2 and destroyer_count == 3 and submarine_count == 4
