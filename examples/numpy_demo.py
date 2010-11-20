"""

Create a numpy array of 64 bit floats

>>> a=[1,2,3,4]

indexing starts at zero
and covers the open interval [first,last)

>>> a[0:]
[1, 2, 3, 4]

>>> a[:]
[1, 2, 3, 4]

>>> a[-1]
4

index ranges are called "slices"

>>> a[0:2]
[1, 2]

you can index relative to beginning or end

>>> a[-2:]
[3, 4]

and slices are objects

>>> endslice=slice(-2,None)
>>> a[endslice]
[3, 4]
"""

if __name__ == "__main__":
    import numpy as np
    import doctest
    doctest.testmod()
