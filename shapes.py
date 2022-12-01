"""Python Fundamentals Final Project - shapes module."""
# Shreya Karmakar
from math import sqrt, pi


class Point:
    """Two-Dimensional Point(x, y)"""

    def __init__(self, x=0, y=0):
        """Initialize the Point instance"""
        self.x = x
        self.y = y

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, val):
        if not isinstance(val, int | float):
            raise TypeError('Invalid coordinate values for Point')
        self._x = val

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, val):
        if not isinstance(val, int | float):
            raise TypeError('Invalid coordinate values for Point')
        self._y = val

    def __str__(self):
        return f'Point at ({self.x}, {self.y})'

    def __repr__(self):
        return f'Point(x={self.x}, y={self.y})'

    @property
    def magnitude(self):
        """Return the magnitude of vector from (0,0) to self."""
        return sqrt(self.x ** 2 + self.y ** 2)

    def distance(self, point2):
        """Return the distance between the two points."""
        return sqrt((self.x - point2.x) ** 2 + (self.y - point2.y) ** 2)

    def __iter__(self):
        yield self.x
        yield self.y

    def __add__(self, other):
        if not isinstance(other, Point):
            return NotImplemented
        return Point(self.x + other.x, self.y + other.y)

    def __iadd__(self, other):
        if not isinstance(other, Point):
            return NotImplemented
        self.x += other.x
        self.y += other.y
        return self

    def __mul__(self, other):
        if not isinstance(other, int | float):
            return NotImplemented
        x = self.x * other
        y = self.y * other
        return Point(x, y)

    def __rmul__(self, other):
        if not isinstance(other, int | float):
            return NotImplemented
        x = self.x * other
        y = self.y * other

        return Point(x, y)

    def __imul__(self, other):
        if not isinstance(other, int | float):
            return NotImplemented
        self.x *= other
        self.y *= other
        return self

    def loc_from_tuple(self, coords):
        if not isinstance(coords, tuple):
            raise TypeError('Input to loc_from_tuple should be a tuple')
        self.x, self.y = coords
        return self

    @classmethod
    def from_tuple(cls, coords):
        if not isinstance(coords, tuple):
            raise TypeError('Input to Point.from_tuple should be a tuple')
        return cls(*coords)


class Circle:
    """Circle(center, radius) where center is a Point instance"""

    def __init__(self, center=None, radius=1):
        if not center:
            center = Point()
        self.center = center
        self.radius = radius

    def __repr__(self):
        return f'Circle(center=Point({self.center.x}, {self.center.y})' \
               f', radius={self.radius})'

    def __str__(self):
        return f'Circle with center at ({self.center.x}, {self.center.y})' \
               f' and radius {self.radius}'

    @property
    def area(self):
        """Calculate and return the area of the Circle"""
        return pi * self.radius ** 2

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
            raise ValueError('The radius cannot be negative!')
        self._radius = radius

    @property
    def center(self):
        return self._center

    @center.setter
    def center(self, center):
        if not isinstance(center, Point):
            raise TypeError('The center must be a Point!')
        self._center = center

    def __add__(self, other):
        if not isinstance(other, Circle):
            return NotImplemented
        center = self.center + other.center
        radius = self.radius + other.radius
        return Circle(center, radius)

    def __iadd__(self, other):
        if not isinstance(other, Circle):
            return NotImplemented
        self.center += other.center
        self.radius += other.radius
        return self

    def center_from_tuple(self, coords):
        if not isinstance(coords, tuple):
            raise TypeError('Input to center_from_tuple should be a tuple')
        x, y = coords
        self.center.x = x
        self.center.y = y
        return self

    @classmethod
    def from_tuple(cls, coords, radius=1):
        if not isinstance(coords, tuple):
            raise TypeError('Input to Circle.from_tuple should be a tuple')
        point = Point(*coords)
        return cls(point, radius)
