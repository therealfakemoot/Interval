from functools import total_ordering

class ValidationError(Exception):pass

@total_ordering
class Interval(object):
    '''Interval is a type that allows specifying whether an interval is left
    or right open/closed. It supports rich comparisons with other Intervals,
    assuming the values passed as start and end are comparable with each other.

    a < b : Tests whether a precedes b.
    a ^ b : Tests whether a overlaps with b.
    '''

    def __init__(self, (start, leftopen), (end, rightopen)):
        if start > end:
            raise ValidationError('Start value must preceed end value.')
        self.start = start
        self.lopen = leftopen
        self.end = end
        self.ropen = rightopen

    def __str__(self):
        if self.lopen:
            l = '('
        else:
            l = '['

        if self.ropen:
            r = ')'
        else:
            r = ']'

        return "{l}{start},{end}{r}".format(l=l,r=r, start=self.start, end=self.end)

    def __eq__(self, other):
        return (self.start,self.end) == (other.start,other.end) and (self.lopen, self.ropen) == (other.lopen, other.ropen)

    def __nonzero__(self):
        return (self.lopen or self.ropen) and (self.start == self.end)

    def __add__(self, other):
        if self & other:
            return Interval((self.start, self.lopen), (other.end, other.ropen))
        else:
            raise ValueError('Addition is not supported for non-overlapping intervals.')

    def __lt__(self, other):
        if self.ropen or other.lopen:
            return self.start <= other.start
        else:
            return self.start < other.start

    def __and__(self, other):
        if self == other:
            return True
        if self.ropen or other.lopen:
            return self.end >= other.start
        else:
            return self.end > other.start
