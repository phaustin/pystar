"""


Here is a python tuple

>>> a=(1,2,3,4)

indexing starts at zero
and covers the open interval [first,last)

>>> a[0:]
(1, 2, 3, 4)

>>> a[:]
(1, 2, 3, 4)

>>> a[-1]
4

index ranges are called "slices"

>>> a[0:2]
(1, 2)

you can index relative to beginning or end

>>> a[-2:]
(3, 4)

and slices are objects

>>> endslice=slice(-2,None)
>>> a[endslice]
(3, 4)

tuples are immutable

>>> a[0]=9
Traceback (most recent call last):
  File "<ipython console>", line 1, in <module>
TypeError: 'tuple' object does not support item assignment


tuples can be used as dictionary keys

>>> the_dict={}
>>> the_dict[(0,1,2)]='first entry'
>>> the_dict
{(0, 1, 2): 'first entry'}



"""

if __name__ == "__main__":
    import doctest
    doctest.testmod()
