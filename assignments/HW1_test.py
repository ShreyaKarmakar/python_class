"""Test program for CSE-41273 Homework 1.
    Put this in the same directory as HW1.py,
    then run from the command line:
    python HW1_test.py
"""
from textwrap import dedent
import unittest

from assignments.HW1 import (
    comfort_level,
    dash_stringify,
    fstring_practice,
    get_earliest,
    is_perfect_square,
    silly_case,
    string_info,
)


class ComfortLevelTests(unittest.TestCase):
    """Test the comfort_level function, ignoring case."""

    def test_too_cold(self):
        self.assertEqual(comfort_level(59).lower(), "too cold")

    def test_chilly(self):
        self.assertEqual(comfort_level(60).lower(), "a bit chilly")
        self.assertEqual(comfort_level(69).lower(), "a bit chilly")

    def test_comfortable(self):
        self.assertEqual(
            comfort_level(70).lower(), "a comfortable temperature")
        self.assertEqual(
            comfort_level(74).lower(), "a comfortable temperature")

    def test_warm(self):
        self.assertEqual(comfort_level(75).lower(), "a bit warm")
        self.assertEqual(comfort_level(82).lower(), "a bit warm")

    def test_too_hot(self):
        self.assertEqual(comfort_level(83).lower(), "too hot")


class DashStringifyTests(unittest.TestCase):
    """Test the dash_stringify function."""

    def test_fruits(self):
        expected = 'Orange - Lemon - Lime - Cherry - Peach - Apricot'
        fruits = ['Orange', 'Lemon', 'Lime', 'Cherry', 'Peach', 'Apricot']
        self.assertEqual(dash_stringify(fruits), expected)

    def test_one_item_list(self):
        self.assertEqual(dash_stringify(['A Fruit']), 'A Fruit')


class FstringPracticeTests(unittest.TestCase):
    """Test the fstring_practice function"""

    def test_fstring_empty_input(self):
        self.assertEqual(fstring_practice([], 2), [])

    def test_fstring_numbers1(self):
        expected = [
            '7 divided by 3 is 2.3333333333333335',
            '12 divided by 3 is 4.0',
            '45 divided by 3 is 15.0',
            '32 divided by 3 is 10.666666666666666'
        ]
        numbers = [7, 12, 45, 32]
        self.assertEqual(fstring_practice(numbers, 3), expected)

    def test_fstring_numbers2(self):
        expected = [
            '7 divided by 4 is 1.75',
            '12 divided by 4 is 3.0',
            '45 divided by 4 is 11.25',
            '32 divided by 4 is 8.0'
        ]
        numbers = [7, 12, 45, 32]
        self.assertEqual(fstring_practice(numbers, 4), expected)

    def test_fstring_numbers3(self):
        expected = [
            '7 divided by 8 is 0.875',
            '12 divided by 8 is 1.5',
            '45 divided by 8 is 5.625',
            '32 divided by 8 is 4.0'
        ]
        numbers = [7, 12, 45, 32]
        self.assertEqual(fstring_practice(numbers, 8), expected)


class GetEarliestTests(unittest.TestCase):
    """Test the get_earliest function"""

    def test_oldest_same_month_day(self):
        self.assertEqual(
            get_earliest("01/27/1832", "01/27/1756"), '01/27/1756')

    def test_oldest_years(self):
        self.assertEqual(
            get_earliest("02/29/1972", "12/21/1946"), '12/21/1946')
        self.assertEqual(
            get_earliest("12/21/1946", "02/29/1972"), '12/21/1946')
        self.assertEqual(
            get_earliest("01/25/2001", "12/01/2000"), '12/01/2000')

    def test_oldest_same_years(self):
        self.assertEqual(
            get_earliest("03/24/1946", "02/21/1946"), '02/21/1946')
        self.assertEqual(
            get_earliest("06/21/1958", "06/24/1958"), '06/21/1958')
        self.assertEqual(
            get_earliest("06/24/1958", "06/21/1958"), '06/21/1958')
        self.assertEqual(
            get_earliest("01/25/2000", "12/01/2000"), '01/25/2000')

    def test_oldest_same_date(self):
        self.assertEqual(
            get_earliest("03/17/2007", "03/17/2007"), '03/17/2007')


class PerfectSquareTests(unittest.TestCase):
    """Test the is_perfect_square function."""

    def test_is_119025_perfect_square(self):
        self.assertIs(is_perfect_square(119025), True)

    def test_is_81_perfect_square(self):
        self.assertIs(is_perfect_square(81), True)

    def test_is_16_perfect_square(self):
        self.assertIs(is_perfect_square(16), True)

    def test_is_49_perfect_square(self):
        self.assertIs(is_perfect_square(49), True)

    def test_is_1000_perfect_square(self):
        self.assertIs(is_perfect_square(1000), False)

    def test_is_20_perfect_square(self):
        self.assertIs(is_perfect_square(20), False)

    def test_is_333_perfect_square(self):
        self.assertIs(is_perfect_square(333), False)


class SillyCaseTests(unittest.TestCase):
    """Test the silly_case function."""

    def test_silly_string(self):
        expected = 'tHIS iS a sTRING'
        string = "This is a string"
        self.assertEqual(silly_case(string), expected)

    def test_silly_poem(self):
        poem = """\
        It matters not how strait the gate,
        How charged with punishments the scroll.
        I am the master of my fate:
        I am the captain of my soul."""
        expected = 'iT mATTERS nOT hOW sTRAIT tHE gATE,\nhOW cHARGED wITH' +\
            ' pUNISHMENTS tHE sCROLL.\ni aM tHE mASTER oF mY fATE:\ni aM' +\
            ' tHE cAPTAIN oF mY sOUL.'
        self.assertEqual(silly_case(dedent(poem)), expected)


class StringInfoTests(unittest.TestCase):
    """Test the string_info function"""

    def test_string_info_poem(self):
        poem = """\
        It matters not how strait the gate,
        How charged with punishments the scroll.
        I am the master of my fate:
        I am the captain of my soul."""
        expected = {
            1: ('It matters not how strait the gate,', 35, 7),
            2: ('How charged with punishments the scroll.', 40, 6),
            3: ('I am the master of my fate:', 27, 7),
            4: ('I am the captain of my soul.', 28, 7)
        }
        self.assertEqual(string_info(dedent(poem)), expected)

    def test_string_info_strange(self):
        strange = """\
        Line one is sort of normal,
        Line two   has some    strangeness"""
        expected = {
            1: ('Line one is sort of normal,', 27, 6),
            2: ('Line two   has some    strangeness', 34, 5)
        }
        self.assertEqual(string_info(dedent(strange)), expected)

    def test_string_info_one(self):
        self.assertEqual(string_info("One"), {1: ('One', 3, 1)})

    def test_string_info_empty(self):
        self.assertEqual(string_info(""), {})


if __name__ == "__main__":
    unittest.main()
