"""Homework 6 for CSE-41273"""

# Shreya Karmakar
# You need to import something from itertools:
from itertools import cycle


# 1. separate
# Define your own arguments to match the instructions.
def separate(string, sort=False):
    """Return a list of all characters in given string.
        If keyword argument sort is True, then return them sorted."""
    ans = list(string.lower())
    if sort:
        ans = sorted(ans)
    return ans


# 2. number of non-vowels
def number_non_vowels(string):
    """Returns the number of non-vowels in the input string,
        but not counting whitespace."""
    unwanted = 'aeiou '
    updated_chars = [let for let in string if let.lower() not in unwanted]
    return len(updated_chars)


# 3. special_nums
def special_nums():
    """Return a generator that yields, in order, the numbers that:
        Are in the range from 1 to 450 and are evenly divisible by 10 and 6."""
    for i in range(1, 450 + 1):
        if i % 10 == 0 and i % 6 == 0:
            yield i
        else:
            continue


# 4. evens
def evens(sequence):
    """Return a generator that returns all the input numbers that are even."""
    for num in sequence:
        if num % 2 == 0:
            yield num
        else:
            continue


# 5. continuous_nums
def continuous_nums(num):
    """Return a generator that returns the numbers from 1 to num
        continuously."""

    return cycle([x for x in range(1, num + 1)])


# 6. reverse_iter
def reverse_iter(iterable):
    """Return a generator that yields items from iterable in reverse order"""
    yield from iterable[::-1]


# 7. ReverseIter class
class ReverseIter:
    """Class whose instances iterate the initial iterable in reverse order"""

    def __init__(self, seq):
        self.seq = seq
        self.last = len(seq) - 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.last < 0:
            raise StopIteration()
        ans = self.seq[self.last]
        self.last -= 1
        return ans
