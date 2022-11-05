def flatten_map(result):
    return [item for sublist in result for item in sublist]


def obtain_row(snail_map):
    rows = len(snail_map)
    result = snail_map[::rows]
    del snail_map[::rows]
    return flatten_map(result)


def obtain_column(snail_map):
    result = []
    rows = len(snail_map)
    columns = len(snail_map[0])
    for row in range(rows):
        result.append(snail_map[row][columns - 1])
        del snail_map[row][columns - 1]
    return result


def obtain_row_reversed(snail_map):
    rows = len(snail_map) - 1
    result = snail_map[rows]
    del snail_map[rows]
    return reversed(result)


def obtain_column_reversed(snail_map):
    result = []
    rows = len(snail_map)
    for row in range(rows):
        result.append(snail_map[row][0])
        del snail_map[row][0]
    return reversed(result)


def snail(snail_map):
    if not snail_map:
        return []

    result = []

    while len(snail_map) > 1:
        result.extend(obtain_row(snail_map))
        result.extend(obtain_column(snail_map))
        result.extend(obtain_row_reversed(snail_map))
        result.extend(obtain_column_reversed(snail_map))

    result.append(snail_map[0][0])
    return result
