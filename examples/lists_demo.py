"""

examples at
http://effbot.org/zone/python-list.htm

Here is a python list

>>> a=[1,2,3,4]

Lists are mutable:

>>> a.append(5)
>>> a
[1, 2, 3, 4, 5]
>>> a.pop(-1)
5
>>> a
[1, 2, 3, 4]
>>> a.reverse()
>>> a
[4, 3, 2, 1]

Lists can't be used as dictionary keys

>>> the_dict={}
>>> the_dict[[0,1,2]]='first entry'
Traceback (most recent call last):
  File "<ipython console>", line 1, in <module>
TypeError: list objects are unhashable


"""

if __name__ == "__main__":
    import doctest
    doctest.testmod()
