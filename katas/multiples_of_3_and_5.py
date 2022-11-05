def multiples_of_3_and_5(number):
    multiples_of_3_and_5 = []
    for digit in range(number):
        if digit % 3 == 0 or digit % 5 == 0:
            multiples_of_3_and_5.append(digit)
    return sum(multiples_of_3_and_5)
