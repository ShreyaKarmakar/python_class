"""Homework 1 for CSE-41273"""


# Shreya Karmakar #
# ^^^^^^ Lines beginning with a # are comments
# Please read the instructions that came with this file.
# If you do not follow instructions, you will not be successful.


# Function 1
def silly_case(in_string):
    """Given a mixed-case (possibly multi-line) string, convert it to a
        new string such that each word starts with a lower case letter,
        and the remaining letters of the word are uppercase.
        Return the silly case string."""
    ans = []
    for word in in_string.split():
        modified_word = word[0].lower() + word[1:].upper()
        ans.append(modified_word)
    return " ".join(ans)


# Function 2
def dash_stringify(word_list):
    """Given a list of word strings, return a single string with all the
        strings together, with ' - ' in between the words."""
    # Put the code here
    return " - ".join(word_list)


# Function 3
def is_perfect_square(number):
    """Given a number, return True if it is a perfect square,
        else return False"""
    # Put the code here
    ans = number ** 0.5
    return ans.is_integer()


# Function 4
def comfort_level(temperature):
    """Given a temperature in Fahrenheit, return a string that is a
        comment on the comfort level"""
    # Put the code here
    if temperature < 60:
        ans = "Too cold"
    elif temperature < 70:
        ans = "A bit chilly"
    elif temperature > 82:
        ans = "Too hot"
    elif temperature > 74:
        ans = "A bit warm"
    else:
        ans = "A comfortable temperature"
    return ans


# Function 5
def fstring_practice(numbers, divisor):
    """Given a list of numbers and a divisor, return a list of strings:
        number divided by divisor is result
        for each number in the input list of numbers.
        See instructions for more details."""
    ans = []
    for num in numbers:
        ans.append(f'{num} divided by {divisor} is {num / divisor}')
    return ans


# Function 6
def string_info(in_string):
    """Given a string (multi-line probably), return a dictionary such that:
        Each key is a line number of a line of the string, starting at 1.
        The corresponding value is a tuple containing 3 items:
            the line,
            number of characters in the line,
            number of words in the line
        See the instructions for more details."""
    ans = {}
    for line_no, line in enumerate(in_string.splitlines(), 1):
        ans[line_no] = (line, len(line), len(line.split()))
    return ans


# Function 7
def get_earliest(date1, date2):
    """Given 2 date strings in "MM/DD/YYYY" format, return earliest one."""
    # Put the code here
    mon1, day1, year1 = [int(x) for x in date1.split('/')]
    mon2, day2, year2 = [int(x) for x in date2.split('/')]
    # comparing year
    if year1 == year2:
        if mon1 == mon2:
            if day1 > day2:
                return date2
            else:
                return date1
        elif mon1 > mon2:
            return date2
        else:
            return date1
    elif year1 > year2:
        return date2
    else:
        return date1
