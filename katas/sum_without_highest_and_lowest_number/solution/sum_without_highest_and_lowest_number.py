def sum_without_highest_and_lowest_number(array):
    if not array or len(array) <= 2:
        return 0
    return sum(sorted(array)[1:-1])
