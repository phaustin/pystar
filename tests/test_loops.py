"""Test suite for looping

>>> a=[1,2,3,4]
>>> b=[i**2 for i in a]
>>> b
[1, 4, 9, 16]

"""

from nose.tools import assert_equal
from numpy.testing import assert_almost_equal

def test_list1():
    text=['5.1','3.e6','-12.5']
    real_nums=[float(i) for i in text]
    assert_almost_equal(real_nums,[5.1,3.e6,-12.5])

if __name__=="__main__":
    import doctest
    doctest.testmod()

