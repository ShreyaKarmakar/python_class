""" Homework assignment for week 3 """
# Shreya Karmakar


def len_safe(object):
    """Return length of object or -1 if object has no length.
       So no matter what object it is given, an error should never
       be raised to the user. Returned value -1 is a number,
       not a string.
    """
    try:
        return len(object)
    except TypeError:
        return -1


def list_pairs(in_list):
    """Take a list as input and return a list of pairs (2-tuples). Each pair
        contains an item from the list and the following item."""
    next_list = in_list[1:]
    return list(zip(in_list, next_list))


def unique(sequence):
    """Yield elements of sequence in order, skipping duplicate values."""
    visited = set()
    for e in sequence:
        if e in visited:
            continue
        else:
            yield e
            visited.add(e)
