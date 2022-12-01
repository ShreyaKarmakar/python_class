""" Homework week 6 answers"""
from itertools import cycle, repeat


# 1. separate - version 1
def separate(string, sort=False):
    """Return a list of all characters in given string.
        If keyword argument sort is True, then return them sorted."""
    if sort:
        return sorted(string.casefold())  # Or .lower()
    else:
        return list(string.casefold())


# 1. separate - version 2
def separate2(string, sort=False):
    """Return a list of all characters in given string.
        If keyword argument sort is True, then return them sorted."""
    chars = list(string.casefold())  # Or .lower()
    if sort:
        chars.sort()
    return chars


# 1. separate - version 3
def separate3(string, sort=False):
    """Return a list of all characters in given string.
        If keyword argument sort is True, then return them sorted."""
    chars = []
    chars.extend(string.casefold())  # Or .lower()
    if sort:
        chars.sort()
    return chars


# 2. number of non-vowels
def number_non_vowels(string):
    """Returns the number of non-vowels in the input string,
    but not counting whitespace."""
    # The spli() method ignores *all* whitespace, so this will not count
    # tab characters or the newline in multi-line strings. If you use
    # split(' '), then you would be counting those characters also.
    # The same goes for not removing spaces and putting a space in with
    # the vowels string.
    no_spaces = ''.join(string.casefold().split())
    # Whenver we find a non-vowel character, send the number 1 into sum()
    return sum(
        1 for character in no_spaces
        if character not in 'aeiou'
    )


# 2. number of non-vowels; version 2
# Slightly less performant if the string is long, as it makes an
# entire new list before it is done.
def number_non_vowels2(string):
    """Returns the number of non-vowels in the input string,
    but not counting whitespace."""
    l_string = string.casefold().split()
    # Create a string that contains all non-vowels, then get its length.
    return len([
        character
        for word in l_string
        for character in word
        if character not in 'aeiou'
    ])


# 3. special_nums - using yield, another efficient version.
# Because we know the numbers are always diviible by 30.
# This is my favorite - One line and very clear.
def special_nums():
    """Return a generator that yields, in order, the numbers that:
        Are in the range from 1 to 300 and are evenly divisible by 10 and 6."""
    yield from range(30, 451, 30)


# 3. special_nums. The efficient answer.
def special_nums2():
    """Return a generator that yields, in order, the numbers that:
        Are in the range from 1 to 300 and are evenly divisible by 10 and 6."""
    return (
        n
        for n in range(30, 451, 30)
    )


# 3. special_nums
# Using a generator expression. The explicit answer.
def special_nums3():
    """Return a generator that yields, in order, the numbers that:
        Are in the range from 1 to 450 and are evenly divisible by 10 and 6."""
    return (
        n
        for n in range(1, 451)
        if n % 10 == 0 and n % 6 == 0
    )


# 3. special_nums - using yield individually
def special_nums4():
    """Return a generator that yields, in order, the numbers that:
        Are in the range from 1 to 300 and are evenly divisible by 10 and 6."""
    for i in range(30, 451, 30):
        yield i


# 4. evens
def evens(sequence):
    """Return a generator that returns all the input numbers that are even."""
    return (num for num in sequence if num % 2 == 0)


# 4. evens - Alternative 1
def evens2(sequence):
    """Return a generator that returns all the input numbers that are even."""
    for num in sequence:
        if num % 2 == 0:
            yield num


# 5. continuous_nums using cycle
def continuous_nums(num):
    """Return a generator that returns the numbers from 1 to num
        continuously."""
    return cycle(range(1, num+1))


# 5. continuous_nums using cycle
def continuous_nums2(num):
    """Return a generator that returns the numbers from 1 to num
        continuously."""
    return repeat(range(1, num+1))


# 6. reverse_iter.
# This is a nice, clean, Pythonic-looking version.
def reverse_iter(iterable):
    """Return a generator that yields items from iterable in reverse order."""
    yield from iterable[::-1]


# 6. reverse_iter Version 2
# Since using slice, iterable[::-1] (as in other alternates) makes
# a new list, this is arguably a better alternative.
def reverse_iter2(iterable):
    """Return a generator that yields items from iterable in reverse order."""
    for n in range(1, len(iterable)+1):
        yield iterable[-n]
    # Or we could use range(len(nums)-1, -1, -1) and yield iterable[n]


# 6. reverse_iter Version 3.
# A different kind of iterator, using a generator expression.
def reverse_iter3(iterable):
    """Return a generator that yields items from iterable in reverse order."""
    return (item for item in iterable[::-1])


# 7. ReverseIter class
class ReverseIter:
    """Class whose instances iterate the initial iterable in reverse order."""

    def __init__(self, iterable):
        """Initialize the instance."""
        self.iterable = iterable
        self.index = len(self.iterable)

    def __next__(self):
        """Return the next item from the iterable, in reverse order."""
        if self.index == 0:
            raise StopIteration
        self.index -= 1
        return self.iterable[self.index]

    def __iter__(self):
        """Return self, since we are an iterator."""
        return self
