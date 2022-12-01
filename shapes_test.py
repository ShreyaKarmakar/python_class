"""Your Unit testing for Python Fundamentals Final Project"""
# Shreya Karmakar
import unittest
from shapes import Point, Circle


# Helper functions - use these for data verification when appropriate.
def point_data(point):
    """Return tuple of Point data for comparison."""
    return (point.x, point.y)


def circle_data(circle):
    """Return tuple of Circle data for comparison."""
    return (
        (circle.center.x, circle.center.y),
        circle.radius
    )


class PointTests(unittest.TestCase):

    def test_p01_create_point_no_data(self):
        """P-01. Create a Point with no arguments."""
        # Create a tuple of what the answer from point_data should be
        expected = (0, 0)
        # Create a default Point instance.
        point = Point()
        # Verify that the data of the new Point instance is correct.
        self.assertEqual(point_data(point), expected)

    def test_p02_create_point_with_data(self):
        """P-02. Create a Point with values."""
        expected = (2, 3)
        point = Point(2, 3)
        self.assertEqual(point_data(point), expected)

    def test_p03_point_modification(self):
        """P-03. Verify modification of x, y works."""
        expected = (-1, 5)
        point = Point()
        point.x, point.y = -1, 5
        self.assertEqual(point_data(point), expected)

    def test_p04_verify_point_input(self):
        """P-04. Verify error raised if x or y is not a number"""
        with self.assertRaises(TypeError):
            # Invalid x. Use '_' variable for flake8
            _ = Point("z")
        with self.assertRaises(TypeError):
            # Invalid y.
            _ = Point(3, "z")

    def test_p05_point_iterable(self):
        """P-05. Verify Point is iterable."""
        expected = (2, 3)
        point = Point(2, 3)
        # To be iterable, we should be able to "unpack" it.
        x, y = point
        self.assertEqual((x, y), expected)
        # Because it is not an iterator, it can be unpacked more than once.
        j, k = point
        self.assertEqual((j, k), expected)

    def test_p06_point_not_iterator(self):
        """P-06. Verify point is not an iterator"""
        point = Point(2, 3)
        x = iter(point)
        # Make sure that iter(point) does not return self.
        self.assertIs(x == point, False)
        # We should not be able to call next() on a Point instance.
        point = Point(2, 3)
        with self.assertRaises(TypeError):
            next(point)

    def test_p07_magnitude(self):
        """P-07. Verify Point magnitude property."""
        # If you have 32-bit Python, you might need to calculate this yourself
        expected = 3.605551275463989
        point = Point(2, 3)
        self.assertEqual(point.magnitude, expected)

    def test_p08_magnitude_changes(self):
        """P-08. Verify magnitude property changes after Point changed."""
        expected = 5
        point = Point(-1, 6)
        point.x, point.y = 3, 4
        self.assertEqual(point.magnitude, expected)

    def test_p09_distance(self):
        """P-09. Verify distance between two Point objects."""
        expected = 5
        point1 = Point(2, 3)
        point2 = Point(5, 7)
        self.assertEqual(point1.distance(point2), expected)

    def test_p10_point_str(self):
        """P-10. Verify Point str result."""
        expected = "Point at (2, 3)"
        point = Point(2, 3)
        self.assertEqual(str(point), expected)

    def test_p11_point_repr(self):
        """P-11. Verify Point repr result."""
        expected = "Point(x=2, y=3)"
        point = Point(2, 3)
        self.assertEqual(repr(point), expected)

    def test_p12_point_addition(self):
        """P-12. Verify Point addition."""
        expected1 = (2, 3)
        expected2 = (4, 5)
        expected3 = (6, 8)
        point1 = Point(2, 3)
        point2 = Point(4, 5)
        point3 = point1 + point2
        # Ensure original points unchanged
        self.assertEqual(point_data(point1), expected1)
        self.assertEqual(point_data(point2), expected2)
        # Verify new point is correct
        self.assertEqual(point_data(point3), expected3)

    def test_p13_point_plus_equal_addition(self):
        """P-13. Verify Point += mutating addition."""
        expected = (6, 8)
        point1 = Point(2, 3)
        # Save the id to make sure it doesn't change.
        id1 = id(point1)
        point2 = Point(4, 5)
        # Add using +=
        point1 += point2
        self.assertEqual(point_data(point1), expected)
        # Verify point2 has not changed
        expected = (4, 5)
        self.assertEqual(point_data(point2), expected)
        # Verify that point1 is the same object
        self.assertEqual(id(point1), id1)

    def test_p14_verify_addition_arguments(self):
        """P-14. Verify error if bad arguments to addition"""
        # Check for regular addition and += addition
        point1 = Point(3, 4)
        point2 = Point(5, 6)
        point3 = Point(8, 7)
        with self.assertRaises(TypeError):
            # Use '_' to avoid flake8 errors
            _ = point1 + 3
        with self.assertRaises(TypeError):
            _ = 4 + point2
        with self.assertRaises(TypeError):
            point3 += 3

    def test_p15_create_point_from_tuple(self):
        """P-15. Create a Point using from_tuple."""
        expected = (3, 4)
        point = Point.from_tuple((3, 4))
        self.assertEqual(point_data(point), expected)
        # verify keyword args
        expected = (6, -4)
        point = Point.from_tuple(coords=(6, -4))
        self.assertEqual(point_data(point), expected)

    def test_p16_error_point_from_tuple_no_args(self):
        """P-16. Verify error when using from_tuple with no arguments"""
        with self.assertRaises(TypeError):
            _ = Point.from_tuple()

    def test_p17_verify_from_tuple_input(self):
        """P-17. Verify error raised when from_tuple gets bad input"""
        with self.assertRaises(TypeError):
            _ = Point.from_tuple('a')

    # Remaining Point tests go here

    def test_p18_point_mod_loc_from_tuple(self):
        """P-18. Verify mod of x, y using loc_from_tuple."""
        # Test point.loc_from_tuple(loc)
        # when point is an existing Point instance and loc is a tuple.
        # Remember loc_from_tuple is not a classmethod.
        # Make sure data is correct and the id of the point has not changed.
        point = Point(3, 4)
        loc = (5, 6)
        p_id = id(point)
        # without keyword args
        point.loc_from_tuple(loc)
        self.assertEqual(point_data(point), loc)
        self.assertEqual(p_id, id(point))
        # with keyword args
        point.loc_from_tuple(coords=loc)
        self.assertEqual(point_data(point), loc)
        self.assertEqual(p_id, id(point))

    def test_p19_point_mod_loc_from_tuple_no_args(self):
        """P-19. Verify error when using loc_from_tuple with no arguments."""
        # Create a Point instance and test that using loc_from_tuple on
        # the point instance without any arguments raises an error.
        # Remember loc_from_tuple is not a classmethod.
        # NOT with try/except; use unittest.
        point = Point(3, 4)
        with self.assertRaises(TypeError):
            point.loc_from_tuple()

    def test_p20_verify_loc_from_tuple_input(self):
        """P-20. Verify error when loc_from_tuple gets bad input"""
        point = Point(x=5.25, y=8)
        with self.assertRaises(TypeError):
            point.loc_from_tuple(3)

        with self.assertRaises(TypeError):
            point.loc_from_tuple('a')

    def test_p21_number_mult_left(self):
        """P-21. Verify Point multiplied with number."""
        # Test point2 = 3 * point1
        # where point1 is an existing Point instance.
        # Make sure that point1 is not modified.
        expected1 = (2, 3)
        expected2 = (6, 9)
        point1 = Point(2, 3)
        point2 = 3 * point1
        # Ensure original points unchanged
        self.assertEqual(point_data(point1), expected1)
        # Verify new point is correct
        self.assertEqual(point_data(point2), expected2)

    def test_p22_number_mult_right(self):
        """P-22. Verify number multiplied with Point."""
        # Test point2 = point1 * 3
        # where point1 is an existing Point instance.
        # Make sure that point1 is not modified.
        expected1 = (2, 3)
        expected2 = (6, 9)
        point1 = Point(2, 3)
        point2 = point1 * 3
        # Ensure original points unchanged
        self.assertEqual(point_data(point1), expected1)
        # Verify new point is correct
        self.assertEqual(point_data(point2), expected2)

    def test_p23_number_mult_plus_equal(self):
        """P-23. Verify Point *= mutating multiply with number."""
        # Test point1 *= 3
        # where point1 is an existing Point instance.
        # Make sure that the point1 data is modified and is not a new Point.
        # Make sure that point1 is modified (not a new Point).
        expected = (6, 9)
        point1 = Point(2, 3)
        # Save the id to make sure it doesn't change.
        id1 = id(point1)
        # Multiple using *=
        point1 *= 3
        self.assertEqual(point_data(point1), expected)

        # Verify that point1 is the same object
        self.assertEqual(id(point1), id1)

    def test_p24_verify_multiply_bad_input(self):
        """P-24. Verify error multiplying bad input"""
        # Test all kinds of multiplication
        point1 = Point(3, 4)
        point2 = Point(5, 6)
        with self.assertRaises(TypeError):
            # Use '_' to avoid flake8 errors
            _ = point1 * point2
        with self.assertRaises(TypeError):
            _ = point1 * (1, 2)
        with self.assertRaises(TypeError):
            _ = 'a' * point2
        with self.assertRaises(TypeError):
            point1 *= point2


class CircleTests(unittest.TestCase):

    def test_c01_create_no_input(self):
        """C-01. Create default Circle with no arguments."""
        # Create a tuple of what the answer from circle_data should be
        expected = ((0, 0), 1)
        circle = Circle()
        self.assertEqual(circle_data(circle), expected)

    def test_c02_circle_point_objects_different(self):
        """C-02. Make sure Circle centers are different objects for default."""
        # In other words, they should have the same VALUES,
        # But NOT be the same objects.
        circle1 = Circle()
        circle2 = Circle()
        self.assertIsNot(circle1.center, circle2.center)
        self.assertEqual(circle_data(circle1), circle_data(circle2))

    def test_c03_create_point_and_radius_input(self):
        """C-03. Create Circle with Point and radius."""
        # Test with and without keyword arguments, one and both arguments
        # IRL I would split these up somewhat into more tests, but whatever...
        # I already numbered everything...
        # Create circle with only a point for center (default radius)
        expected = ((2, 3), 1)
        point = Point(2, 3)
        # Also make sure the circle's center is the same as the point input.
        point_id = id(point)
        circle = Circle(center=point)
        self.assertEqual(circle_data(circle), expected)
        self.assertEqual(point_id, id(circle.center))
        # Create circle with only radius input(default center).
        expected = ((0, 0), 2.5)
        circle = Circle(radius=2.5)
        self.assertEqual(circle_data(circle), expected)
        # Make sure radius=0 works (edge case of Circles)
        expected = ((0, 0), 0)
        circle = Circle(radius=0)
        self.assertEqual(circle_data(circle), expected)
        # Create circle using positional arguments only (no keywords)
        expected = ((2, 3), 1.5)
        circle = Circle(Point(2, 3), 1.5)
        self.assertEqual(circle_data(circle), expected)

    def test_c04_move_center(self):
        """C-04. Verify moving center Point of Circle works."""
        # If we use an existing Point instance for the center,
        # then if we move the point instance, the circle should also move.
        expected = ((6, 2), 1.5)
        point = Point()
        circle = Circle(point, 1.5)
        point.x = 6
        point.y = 2
        self.assertEqual(circle_data(circle), expected)

    def test_c05_change_radius(self):
        """C-05. Verify radius attribute change works."""
        expected = ((2, 3), 1.5)
        circle = Circle(center=Point(2, 3))
        circle.radius = 1.5
        self.assertEqual(circle_data(circle), expected)
        # Test edge case of zero radius
        expected = ((2, 3), 0)
        circle.radius = 0
        self.assertEqual(circle_data(circle), expected)

    def test_c06_area(self):
        """C-06. Verify area property."""
        # If you have 32-bit Python, you might need to calculate this yourself
        expected = 12.566370614359172
        circle = Circle(radius=2)
        self.assertEqual(circle.area, expected)

    def test_c07_area_changed(self):
        """C-07. Verify area changes correctly when radius changes."""
        # If you have 32-bit Python, you might need to calculate this yourself
        expected = 19.634954084936208
        circle = Circle(radius=2)
        circle.radius = 2.5
        self.assertEqual(circle.area, expected)
        # Test edge case -  technically this should be another test function
        expected = 0
        circle.radius = 0
        self.assertEqual(circle.area, expected)

    def test_c08_change_center(self):
        """C-08. Verify center attribute change works."""
        expected = ((2, 3), 1)
        # Create a default circle
        circle = Circle()
        # Change the center Point instance to a new Point instance
        circle.center = Point(2, 3)
        self.assertEqual(circle_data(circle), expected)

    def test_c09_diameter(self):
        """C-09. Verify diameter property works."""
        expected = 3
        circle = Circle(center=Point(2, 3), radius=1.5)
        self.assertEqual(circle.diameter, expected)
        # Verify diameter changes when radius changes
        # technically this should be another test function
        expected = 8
        circle.radius = 4
        self.assertEqual(circle.diameter, expected)

    def test_c10_diameter_changes(self):
        """C-10. Verify diameter changes causes radius change."""
        expected = ((2, 3), 1.5)
        circle = Circle(center=Point(2, 3))
        circle.diameter = 3
        self.assertEqual(circle_data(circle), expected)
        # Test edge case -  technically this should be another test function
        expected = ((2, 3), 0)
        circle.diameter = 0
        self.assertEqual(circle_data(circle), expected)

    # Remaining Circle tests go here

    def test_c11_circle_str(self):
        """C-11. Verify Circle str result."""
        # Test str(circle) result is exactly like instructions.
        expected = "Circle with center at (2.75, 3) and radius 1.5"
        point1 = Point(2.75, 3)
        # with keyword args
        circle = Circle(center=point1, radius=1.5)
        self.assertEqual(str(circle), expected)
        # without keyword args
        circle = Circle(point1, 1.5)
        self.assertEqual(str(circle), expected)

    def test_c12_circle_repr(self):
        """C-12. Verify Circle repr result."""
        # Test repr(circle) is exactly like instructions.
        expected = "Circle(center=Point(2.75, 3), radius=1.5)"
        point1 = Point(2.75, 3)
        circle = Circle(center=point1, radius=1.5)
        self.assertEqual(repr(circle), expected)

    def test_c13_illegal_center_creation(self):
        """C-13. Verify error if center is not a Point on creation."""
        # Test something like Circle(center=1)
        # Make sure an error is raised
        # NOT with try/except; use unittest.
        with self.assertRaises(TypeError):
            _ = Circle(center=1)
        with self.assertRaises(TypeError):
            _ = Circle(center=(1, 2))

    def test_c14_illegal_center_modification(self):
        """C-14. Verify error if changing center to something not a Point."""
        # Test something like circle.center = 2
        # Make sure an error is raised
        # NOT with try/except; use unittest.
        circle = Circle(center=Point(3, 4), radius=2)
        with self.assertRaises(TypeError):
            circle.center = 2
        with self.assertRaises(TypeError):
            circle.center = None
        with self.assertRaises(TypeError):
            circle.center = (1, 2)

    def test_c15_create_negative_radius(self):
        """C-15. Verify error on creation with radius < 0."""
        # Test something like Circle(center=Point(2, 3), radius=-2)
        # Make sure an error is raised
        # NOT with try/except; use unittest.
        with self.assertRaises(ValueError):
            _ = Circle(center=Point(2, 3), radius=-2)

    def test_c16_change_negative_radius(self):
        """C-16. Verify error when radius changes to be < 0."""
        # Test changing circle.radius = -2
        # Make sure an error is raised
        # NOT with try/except; use unittest.
        circle = Circle(Point(1, 2), 2)
        with self.assertRaises(ValueError):
            circle.radius = -2

    def test_c17_change_negative_diameter(self):
        """C-17. Verify error when diameter changes to be < 0."""
        # Test changing circle.diameter = -2
        # Make sure an error is raised
        # NOT with try/except; use unittest.
        circle = Circle(Point(1, 2), 2)
        with self.assertRaises(ValueError):
            circle.diameter = -2

    def test_c18_circle_addition(self):
        """C-18. Verify Circle addition."""
        # Create 2 circles, add them together, make sure
        # the new circle is correct and first 2 circles unchanged.
        circle1 = Circle(radius=2.5, center=Point(1, 1))
        circle2 = Circle(center=Point(2, 3), radius=1)
        id1, id2 = id(circle1), id(circle2)
        circle3 = circle1 + circle2
        # verify new circle is correct
        expected = ((3, 4), 3.5)
        self.assertEqual(circle_data(circle3), expected)
        # verify first 2 circles unchanged
        expected1 = ((1, 1), 2.5)
        self.assertEqual(circle_data(circle1), expected1)
        expected2 = ((2, 3), 1)
        self.assertEqual(circle_data(circle2), expected2)
        self.assertEqual(id(circle1), id1)
        self.assertEqual(id(circle2), id2)

    def test_c19_circle_plus_equal_addition(self):
        """C-19. Verify Circle += mutating addition."""
        # Create 2 circles, then do circle1 += circle2
        # Make sure circle1 is correct and is the same object.
        # Make sure circle2 is unchanged.
        circle1 = Circle(radius=2.5, center=Point(1, 1))
        circle2 = Circle(center=Point(2, 3), radius=1)
        id1 = id(circle1)
        circle1 += circle2
        expected1 = ((3, 4), 3.5)
        self.assertEqual(circle_data(circle1), expected1)
        self.assertEqual(id(circle1), id1)

        expected2 = ((2, 3), 1)
        self.assertEqual(circle_data(circle2), expected2)

    def test_c20_verify_circle_addition_input(self):
        """C-20. Verify error if addition given bad input"""
        point = Point(12, -7)
        circle1 = Circle(point, 5)
        with self.assertRaises(TypeError):
            _ = circle1 + (3, 4)

        with self.assertRaises(TypeError):
            _ = (2, 3) + circle1

        with self.assertRaises(TypeError):
            circle1 += (9, 3)

        with self.assertRaises(TypeError):
            circle1 += 'a'

    def test_c21_circle_create_from_tuple(self):
        """C-21. Test circle creation using from_tuple."""
        # Test something like Circle.from_tuple(coords=(3, 4), radius=2)
        circle = Circle.from_tuple(radius=2, coords=(3, 4))
        expected = ((3, 4), 2)
        self.assertEqual(circle_data(circle), expected)
        # without keyword args
        circle = Circle.from_tuple((3, 4), 2)
        self.assertEqual(circle_data(circle), expected)
        # Checking Circle center being a Point
        self.assertTrue(isinstance(circle.center, Point))

    def test_c22_circle_create_from_tuple_no_args(self):
        """C-22. Verify error using Circle.from_tuple with no arguments."""
        # Create a circle with Circle.from_tuple()
        # Verify an error occurs.
        with self.assertRaises(TypeError):
            _ = Circle.from_tuple()

    def test_c23_circle_create_from_tuple_only_tuple(self):
        """C-23. Test circle creation using from_tuple with only tuple."""
        # Test something like Circle.from_tuple(coords=(3, 4))
        circle = Circle.from_tuple(coords=(3, 4))
        expected = ((3, 4), 1)
        self.assertEqual(circle_data(circle), expected)
        # without keyword args
        circle2 = Circle.from_tuple((3, 4))
        self.assertEqual(circle_data(circle2), expected)

    def test_c24_verify_from_tuple_input(self):
        """C-24. Verify error raised when from_tuple gets bad input"""
        # Try to create a Circle with Circle.from_tuple where the
        # input is not a tuple, and verify the error is raised.
        with self.assertRaises(TypeError):
            _ = Circle.from_tuple(3)

    def test_c25_circle_modify_center_from_tuple(self):
        """C-25. Test circle modify with center_from_tuple method."""
        # Create a circle and a tuple t
        # Test circle.center_from_tuple(t)
        circle = Circle(Point(2, 3), 2)
        t = 4, 5
        id1 = id(circle)
        circle.center_from_tuple(coords=t)
        expected = (t, 2)
        self.assertEqual(circle_data(circle), expected)
        self.assertEqual(id(circle), id1)
        # without keyword args
        circle.center_from_tuple(t)
        expected = (t, 2)
        self.assertEqual(circle_data(circle), expected)
        self.assertEqual(id(circle), id1)

    def test_c26_circle_modify_center_from_tuple_no_args(self):
        """C-26. Verify error using center_from_tuple with no arguments."""
        # Create a circle and do circle.center_from_tuple()
        # Verify an error is raised.
        circle = Circle(Point(2, 3), 2)
        with self.assertRaises(TypeError):
            circle.center_from_tuple()

    def test_c27_verify_center_from_tuple(self):
        """C-27. Verify error using center_from_tuple with bad arguments."""
        circle = Circle(center=Point(12, -7), radius=5)
        with self.assertRaises(TypeError):
            circle.center_from_tuple('a')


if __name__ == "__main__":
    unittest.main()
