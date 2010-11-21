"""

Create a numpy array of 32 bit floats
and square it

>>> import numpy as np
>>> a=np.array([1,2,3,4],dtype=np.float32)
>>> a**2.
array([  1.,   4.,   9.,  16.], dtype=float32)


Create an vector of 100 values spaced evenly between
5 and 75:

>>> a=np.linspace(5,75,100)

Find the index of the value closes to 28.5

>>> the_diff=(a - 28.5)**2.
>>> np.argmin(the_diff)
33
>>> a[33]
28.333333333333332


how many values are there between 20 and 30,
inclusive?

>>> hit = np.logical_and(a >= 20, a <= 30)
>>> np.sum(hit)
14

what is their median?

>>> np.median(a[hit])
25.151515151515152

"""

if __name__ == "__main__":
    import doctest
    doctest.testmod()
