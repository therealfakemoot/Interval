from interval.core import Interval
from interval.core import ValidationError

from nose.tools import raises

from unittest import TestCase

@raises(ValidationError)
def test_invalid_interval_creation():
    Interval((1, True),(0, True))

class OpenInterval(TestCase):
    def setUp(self):
        self.i = Interval((0, True), (2, True))

    def test_equal_intervals(self):
        i = Interval((0, True), (2, True))
        assert self.i == i

    def test_unequal_intervals(self):
        i = Interval((0, True), (1, True))
        assert self.i != i

    def test_preceding_interval(self):
        i = Interval((2, True), (3, True))
        assert self.i < i

    def test_overlapping_interval(self):
        i = Interval((2, True), (3, True))
        assert self.i & i

    def test_non_overlapping_interval(self):
        i = Interval((3, True), (4, True))
        assert not self.i & i

class LeftClosedInterval(OpenInterval):
    def setUp(self):
        self.i = Interval((0, False), (2, True))

    def test_equal_intervals(self):
        i = Interval((0, False), (2, True))
        assert self.i == i
        
class RightClosedInterval(OpenInterval):
    def setUp(self):
        self.i = Interval((0, True), (2, False))

    def test_equal_intervals(self):
        i = Interval((0, True), (2, False))
        assert self.i == i

class ClosedInterval(OpenInterval):
    def setUp(self):
        self.i = Interval((0, False), (2, False))

    def test_equal_intervals(self):
        i = Interval((0, False), (2, False))
        assert self.i == i
