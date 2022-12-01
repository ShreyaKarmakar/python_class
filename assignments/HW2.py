"""Homework 2 for CSE-41273"""
# Shreya Karmakar


# Function 1
def last_n_elements(sequence, n):
    """Given a sequence and a number n, return the last n elements of the
        sequence."""
    return sequence[-n::]


# Function 2
def last_n_reversed(sequence, n):
    """Given a sequence and a number n, return the last n elements of the
        sequence in reversed order."""
    return sequence[-1:-n-1:-1]


# Function 3
def words_containing(sentence, letter):
    """ Given a sentence, returns list of words that contain the letter.
        Letter given is lowercase. Sentence can be mixed case, and the
        case should be ignored for searching.
    """
    return [word
            for word in sentence.split()
            if letter.lower() in word.lower()]


# Function 4
def power_list(numbers):
    """Given a list of numbers, return a new list where each element is the
        corresponding element of the list to the power of its list index."""
    return [num**index for index, num in enumerate(numbers)]


# Function 5
def rotate_list(some_list):
    """Take a list as input and remove the first item from the list and add it
        to the end of the list. Return the item moved."""
    first_item = some_list[0]
    some_list.remove(first_item)
    some_list.append(first_item)
    return first_item


# Function 6
def alternating(iterable1, iterable2):
    """Return list of one item at a time from each given iterable,
        alternating between them."""
    return [ele for elements in zip(iterable1, iterable2) for ele in elements]


# Function 7
def get_word_codes(words):
    """Given a list of words, return a dictionary where the words are keys,
        and the value is a list of the character codes of the letters
        of the word that is its key."""
    return {key: [ord(c) for c in key] for key in words}
