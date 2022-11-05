def moving_zeros_to_the_end(l):
    return sorted(l, key=lambda x: not x)
