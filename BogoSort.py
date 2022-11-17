from random import shuffle, randint


def is_sorted(data) -> bool:
    """Determine whether the data is sorted."""
    return all(a <= b for a, b in zip(data, data[1:]))


def bogosort(data: list) -> list:
    """ Shuffle data until sorted. """
    while not is_sorted(data):
        shuffle(data)
    return data


def randomlist(length: int):
    tab = []
    for i in range(length):
        tab.append(randint(0, length))
    return tab
