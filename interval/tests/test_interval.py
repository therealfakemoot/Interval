from interval.core import Interval
from interval.core import ValidationError

from nose.tools import raises, eq_, ok_

from unittest import TestCase


@raises(ValidationError)
def test_invalid_interval_creation():
    Interval((1, True), (0, True))


class OpenInterval(TestCase):
    def setUp(self):
        self.i = Interval((0, True), (2, True))

    def test_equal_intervals(self):
        eq_(self.i, self.i, msg="{} == {}".format(self.i, self.i))

    def test_unequal_intervals(self):
        i = Interval((0, True), (1, True))
        ok_(not self.i == i, msg="{} != {}".format(self.i, i))

    def test_preceding_interval(self):
        i = Interval((2, True), (3, True))
        ok_(self.i < i, msg="{} < {}".format(self.i, i))

    def test_overlapping_interval(self):
        i = Interval((2, True), (3, True))
        ok_(self.i & i, msg="{} & {}".format(self.i, i))

    def test_non_overlapping_interval(self):
        i = Interval((3, True), (4, True))
        ok_(not self.i & i, msg="not {} & {}".format(self.i, i))

    def test_sequential_interval_addition(self):
        i = Interval((2, True), (3, True))
        result = Interval((0, True), (3, True))
        eq_(self.i + i, result, msg="{}+{}={}".format(self.i, i, self.i + i))

    def test_nonsequential_interval_addition(self):
        i = Interval((-2, True), (0, True))
        result = Interval((-2, True), (0, True))
        eq_(i + self.i, result, msg="{}+{}={}".format(i, self.i, i + self.i))


class LeftClosedInterval(OpenInterval):
    def setUp(self):
        self.i = Interval((0, False), (2, True))

    def test_interval_addition(self):
        i = Interval((2, False), (3, True))
        result = Interval((0, False), (3, True))
        eq_(self.i + i, result, msg="{}+{}={}".format(self.i, i, self.i + i))


class RightClosedInterval(OpenInterval):
    def setUp(self):
        self.i = Interval((0, True), (2, False))

    def test_nonsequential_interval_addition(self):
        i = Interval((-2, True), (0, True))
        result = Interval((-2, True), (0, True))
        eq_(i + self.i, result, msg="{}+{}={}".format(i, self.i, i + self.i))


class ClosedInterval(OpenInterval):
    def setUp(self):
        self.i = Interval((0, False), (2, False))

    @raises(ValueError)
    def test_interval_addition(self):
        i = Interval((2, False), (3, True))
        result = Interval((0, True), (3, True))
        eq_(self.i + i, result, msg="{} + {}".format(self.i, i))
