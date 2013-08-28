Interval is a general purpose library for providing a [mathematical interval](http://en.wikipedia.org/wiki/Interval_(mathematics) type that supports sorting and intersection checks.

#Installation
````
git clone git@github.com:therealfakemoot/Interval.git
cd Interval/
python setup.py install
```

#Usage
Interval objects support the concept of being left or right closed or open. They are intended for use with pairs of same-type values. Under the hood, Interval simply calls < and <= on the start and end parameters for its comparisons, meaning that types that do not support these operations or are not meaningful to compare in this way will produce erroenous or unexpected behavior.

##Example
```py
from interval.core import Interval

a = Interval((0, True), (5, True))
b = Interval((5, True), (10, True))
a + b == Interval((0, True), (10, True))
```

This can be used with non-integer data types as well.

```py
from interval.core import Interval
import datetime

a = datetime.datetime(datetime.datetime.now())
td = datetime.timedelta(10)
b = a + td
c = b + td
date_intervalA = Interval((a, True), (b, True))
date_intervalB = Interval((b, True), (c, True))
date_intervalA + date_intervalB == Interval((a, True), (c, True))
```

Note that these examples only show 'normal' non-failing operations. Non-overlapping intervals cannot be added together, but can still be compared for intersection and precedence.
