from interval.core import Interval
from interval.core import ValidationError

from nose.tools import raises, ok_, eq_


def _add_intervals(a, b):
    return a + b


def test_invalid_interval_additions():
    i = Interval((0, False), (1, False))

    vals = [Interval((-1, True), (0, False)),
            Interval((-1, False), (0, False)),
            Interval((1, False), (2, True)),
            Interval((1, False), (2, False)),
            Interval((3, True), (4, False)),
            Interval((3, False), (4, True)),
            Interval((3, False), (4, False))
            ]

    for v in vals:
        yield raises(ValueError)(_add_intervals), i, v


def test_false_interval_intersections():
    i = Interval((0, True), (1, True))

    vals = [Interval((-1, True), (0, True)),
            Interval((-1, True), (0, False)),
            Interval((1, True), (2, True)),
            Interval((1, False), (2, True)),
            Interval((-2, True), (-1, True)),
            Interval((2, True), (3, True))
            ]

    results = [True] * 5 + [False]

    intersect = lambda a, b, v: eq_(a & b, v,
                                    msg="{} & {} == {}".format(a, b, v))

    for v, r in zip(vals, results):
        yield intersect, i, v, r
