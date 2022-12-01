"""Test program for CSE-41273 Homework 2.
    Put this in the same directory as HW2.py,
    then run it from the command line:
    python HW2_test.py
"""
import unittest

from assignments.HW2 import (
    alternating,
    get_word_codes,
    last_n_elements,
    last_n_reversed,
    power_list,
    rotate_list,
    words_containing,
)


class AlternatingTests(unittest.TestCase):
    """Test matrix_fill function."""
    # MAKE SURE INPUT LISTS ARE NOT MODIFIED
    def test_alternating4(self):
        expected = [1, 5, 2, 6, 3, 7, 4, 8]
        list1 = [1, 2, 3, 4]
        list2 = [5, 6, 7, 8]
        exp1 = list(list1)
        exp2 = list(list2)
        result = alternating(list1, list2)
        self.assertEqual(result, expected)
        self.assertEqual(list1, exp1)
        self.assertEqual(list2, exp2)

    def test_alternating3(self):
        expected = [1, 2, 3, 4, 5, 6]
        list1 = [1, 3, 5]
        list2 = [2, 4, 6]
        exp1 = list(list1)
        exp2 = list(list2)
        result = alternating(list1, list2)
        self.assertEqual(result, expected)
        self.assertEqual(list1, exp1)
        self.assertEqual(list2, exp2)

    def test_alternating1(self):
        expected = [1, 2]
        list1 = [1]
        list2 = [2]
        exp1 = list(list1)
        exp2 = list(list2)
        result = alternating(list1, list2)
        self.assertEqual(result, expected)
        self.assertEqual(list1, exp1)
        self.assertEqual(list2, exp2)


class GetWordCodesTests(unittest.TestCase):
    """Test get_word_codes function."""

    def test_get_word_codes_list(self):
        words = ["hello", "bye", "yes", "no", "python"]
        expected = {
            'yes': [121, 101, 115], 'hello': [104, 101, 108, 108, 111],
            'python': [112, 121, 116, 104, 111, 110], 'no': [110, 111],
            'bye': [98, 121, 101]}
        exp = list(words)
        self.assertEqual(get_word_codes(words), expected)
        self.assertEqual(words, exp)

    def test_get_word_codes_string(self):
        expected = {
            'Hello World':
            [72, 101, 108, 108, 111, 32, 87, 111, 114, 108, 100]}
        self.assertEqual(get_word_codes(['Hello World']), expected)


class LastNElementsTests(unittest.TestCase):
    """Test last_n_elements function."""

    def test_last_n_elements_list(self):
        fruits = ['apples', 'grapes', 'peaches', 'apricots', 'bananas']
        exp = list(fruits)
        self.assertEqual(
            last_n_elements(fruits, 3), ['peaches', 'apricots', 'bananas'])
        self.assertEqual(fruits, exp)

    def test_last_n_elements_single(self):
        fruits = ['apples', 'grapes', 'peaches', 'apricots', 'bananas']
        self.assertEqual(last_n_elements(fruits, 1), ['bananas'])

    def test_last_n_elements_numbers(self):
        numbers = [41, 25, 54, 15, 76, 68, 32, 38]
        self.assertEqual(last_n_elements(numbers, 4), [76, 68, 32, 38])


class LastNReversedTests(unittest.TestCase):
    """Test last_n_reversed function."""

    def test_last_n_reversed_strings(self):
        fruits = ['apples', 'grapes', 'peaches', 'apricots', 'bananas']
        exp = list(fruits)
        self.assertEqual(
            last_n_reversed(fruits, 3), ['bananas', 'apricots', 'peaches'])
        self.assertEqual(last_n_reversed(fruits, 1), ['bananas'])
        self.assertEqual(fruits, exp)

    def test_last_n_reversed_numbers(self):
        numbers = [41, 25, 54, 15, 76, 68, 32, 38]
        self.assertEqual(last_n_reversed(numbers, 4), [38, 32, 68, 76])


class PowerListTests(unittest.TestCase):
    """Test power_list function."""

    def test_power_list(self):
        self.assertEqual(power_list([3, 2, 5]), [1, 2, 25])
        numbers = [78, 700, 82, 16, 2, 3, 9.5]
        self.assertEqual(
            power_list(numbers), [1, 700, 6724, 4096, 16, 243, 735091.890625])

    def test_unmodified_numbers(self):
        numbers = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]
        unchanged = list(numbers)
        expected = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048]
        pl = power_list(numbers)
        self.assertEqual(pl, expected)
        # ensure input not modified
        self.assertEqual(numbers, unchanged)


class RotateListTests(unittest.TestCase):
    """Test rotate_list function."""

    def test_rotate_number_list(self):
        numbers = [1, 2, 3, 4]
        saveit = id(numbers)
        self.assertEqual(rotate_list(numbers), 1)
        self.assertEqual(numbers, [2, 3, 4, 1])
        #  Make sure it is the same line
        self.assertEqual(id(numbers), saveit)
        # Make sure it works a second time on the same list
        self.assertEqual(rotate_list(numbers), 2)
        self.assertEqual(numbers, [3, 4, 1, 2])

    def test_rotate_single_list(self):
        number = [1]
        self.assertEqual(rotate_list(number), 1)
        self.assertEqual(number, [1])

    def test_rotate_string_list(self):
        fruits = ['apples', 'grapes', 'peaches', 'apricots', 'bananas']
        self.assertEqual(rotate_list(fruits), 'apples')
        self.assertEqual(
            fruits, ['grapes', 'peaches', 'apricots', 'bananas', 'apples'])


class WordsContainingTests(unittest.TestCase):
    """Test words_containing function."""

    # Test 1 make sure it matches upper and lower case
    def test_words_containing_upper_lower(self):
        sentence = "The cow jumped over the moon"
        result = words_containing(sentence, 't')
        expected = ['The', 'the']
        self.assertEqual(result, expected)

    # Test 2 make sure it gets all the words and no dups
    def test_words_containing_all(self):
        sentence = "The cow jumped over the moon"
        expected = ['cow', 'over', 'moon']
        result = words_containing(sentence, 'o')
        self.assertEqual(result, expected)

    # Test 3 Return empty list if no matches
    def test_words_containing_none(self):
        sentence = "The cow jumped over the moon"
        expected = []
        result = words_containing(sentence, 'x')
        self.assertEqual(result, expected)

    # Test 4 No error if sentence is empty
    def test_words_containing_empty(self):
        self.assertEqual(words_containing('', 'a'), [])


if __name__ == "__main__":
    unittest.main()
