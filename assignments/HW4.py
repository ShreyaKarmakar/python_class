"""Homework 4 for CSE-41273"""
# Shreya Karmakar
import datetime
from math import sqrt


# Part 1
class Person:
    """Person with first and last name."""

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def __repr__(self):
        return f'Person(first_name="{self.first_name}"' \
               f', last_name="{self.last_name}")'

    def __str__(self):
        return self.__repr__()

    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'

    @property
    def name(self):
        return f'{self.last_name}, {self.first_name}'


# Part 2
class Point:
    """2-D Point objects."""

    def __init__(self, x=0, y=0):
        """Initialize the Point instance"""
        self.x = x
        self.y = y

    def __str__(self):
        return f'Point at ({self.x}, {self.y})'

    def __repr__(self):
        return f'Point(x={self.x}, y={self.y})'

    @property
    def magnitude(self):
        """Return the magnitude of vector from (0,0) to self."""
        return sqrt(self.x ** 2 + self.y ** 2)


# Part 3
class Vehicle:
    """A simple class representing a vehicle"""

    def __init__(self, make, model, year, price, color):
        if not isinstance(year, int):
            raise TypeError('Input year must be an integer!')

        if not isinstance(price, (int, float)):
            raise TypeError('Input price must be a number!')

        self.make = make
        self.model = model
        self.year = year
        self.price = price
        self.color = color

    def __repr__(self):
        return f"Vehicle('{self.make}', '{self.model}', {self.year}," \
               f" {self.price}, '{self.color}')"

    def __str__(self):
        return f'This is a {self.year} {self.color} {self.make} {self.model}' \
               f' costing ${self.price:0.2f}'

    @property
    def current_year(self):
        return datetime.datetime.now().year

    @property
    def current_value(self):
        """Return the current year"""
        age = self.current_year - self.year + 1
        if age > 7:
            price = self.price * 0.1
        else:
            price = self.price - 0.125 * self.price * age
        return price
