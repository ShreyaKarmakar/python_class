"""Homework 5 for CSE-41273"""
# Shreya Karmakar
# 1998
# ^^^^ Replace the 0000 with a different random 4 digit number
# Do not use 2222.
import functools
import math
from collections import Counter


# Part 1, Circle class.
class Circle:
    """Class to create Circle objects"""

    def __init__(self, radius=1):
        """Circle initializer"""
        self.history = []
        self.radius = radius

    def __repr__(self):
        return f'Circle(radius={self.radius})'

    def __str__(self):
        return f'Circle whose radius is {self.radius}'

    @property
    def area(self):
        """Calculate and return the area of the Circle"""
        return math.pi * self.radius ** 2

    @property
    def diameter(self):
        """Calculate and return the diameter of the Circle"""
        return self.radius * 2

    @diameter.setter
    def diameter(self, diameter):
        """Set the diameter"""
        self.radius = diameter / 2

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, radius):
        if radius < 0:
            raise ValueError('Radius cannot be negative!')
        self._radius = radius
        self.history.append(self._radius)


# Part 2. BankAccount class.
@functools.total_ordering
class BankAccount:
    """ Simple BankAccount class """

    def __init__(self, balance=0):
        """Initialize account with balance"""
        self.balance = balance

    def __repr__(self):
        return f'BankAccount(balance={self.balance:0.2f})'

    def __str__(self):
        return f'Account with balance of ${self.balance:0.2f}'

    def __bool__(self):
        return self.balance > 0

    def __eq__(self, other):
        return self.balance == other.balance

    def __lt__(self, other):
        return self.balance < other.balance

    def deposit(self, amount):
        """Deposit amount to this account"""
        self.balance += amount

    def withdraw(self, amount):
        """Withdraw amount from this account"""
        self.balance -= amount


# Part 3 - my_counter
def my_counter(any_integer):
    """Crazy way to use the Counter from collections.
        Take the input of any_integer, multiply it by 8888, then
        multiply that by my_number, which is the 4-digit number from
        line 3 of this file. Take that result to the third power (**3).
        Then return the string with the digit that is the most common
        of the digits of the result as follows:
        'The most common digit is x, occurring y times'
    """
    # REPLACE THE 0000 WITH THE 4-DIGIT NUMBER FROM LINE 3 OF THIS FILE.
    my_number = 1998
    res = any_integer * 8888 * my_number
    res = res ** 3
    counter = Counter(str(res))
    digit, times = counter.most_common(1)[0]
    return f'The most common digit is {digit}, occurring {times} times'
