def is_odd(number):
    return number % 2 != 0


def is_even(number):
    return number % 2 == 0


def opposites_attract(flower1, flower2):
    """
    Otra opción: return (flower1 + flower2) % 2
    """
    return (is_odd(flower1) and is_even(flower2)) or (is_even(flower1) and is_odd(flower2))
