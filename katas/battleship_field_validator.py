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
            raise ValueError
        submarine_count += 1
    if counter == 2:
        if destroyer_count > 3:
            raise ValueError
        destroyer_count += 1
    if counter == 3:
        if cruiser_count > 2:
            raise ValueError
        cruiser_count += 1
    if counter == 4:
        if battleship_count > 1:
            raise ValueError
        battleship_count += 1


def find_ship(row, column, field):
    global counter

    field[row][column] = 2
    counter += 1

    if column + 1 < 10 and field[row][column + 1]:
        for i in range(1, 4):
            if column + i < 10 and field[row][column + i]:  # Horizontal
                counter += 1
                field[row][column + i] = 2
                if field[row + 1][column + i]:
                    raise ValueError

    if row + 1 < 10 and field[row + 1][column]:
        for i in range(1, 4):
            if row + i < 10 and field[row + i][column]:  # Vertical
                counter += 1
                field[row + i][column] = 2
                if field[row + i][column + 1]:
                    raise ValueError

    categorize_ship()

    counter = 0


def validate_battlefield(field):
    if not len(field) == 10 and not len(field[0]) == 10:
        return False

    for row in range(10):
        for column in range(10):
            if not field[row][column] == 1:
                continue
            try:
                find_ship(row, column, field)
            except ValueError:
                return False

    return True
