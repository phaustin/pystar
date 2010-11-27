Python example repository
=========================

+ This repository contains restructured text files
  and python unit tests that demonstrate basic python
  commands

+ To run the doctests and unit tests::

    ~/repos/git phil@tern% git clone git@github.com:phaustin/pystar.git
    Cloning into pystar...
    ~/repos/git phil@tern% cd pystar
    ~/repos/git/pystar phil@tern% nosetests -v --with-doctest --doctest-tests examples tests
    Doctest: examples.lists_demo ... ok
    Doctest: examples.numpy_demo ... ok
    test_loops.test_list1 ... ok
    Doctest: test_loops ... ok

    ----------------------------------------------------------------------
    Ran 4 tests in 0.182s

+ Built documentation can be browsed at http://phaustin.github.com/pystar-doc using
  using the   gh-pages.py script developed by 
  `Fernando Perez  <http://www.mail-archive.com/numpy-discussion@scipy.org/msg28272.html>`_
  for the `datarray-doc <https://github.com/fperez/datarray-doc/blob/master/readme.rst>`_

+ To add/modifiy examples and tests:

  - git clone git@github.com:phaustin/pystar.git
 
  - git clone git@github.com:phaustin/pystar-doc.git

  - cd pystar/doc  and edit rst files

  - from pystar/doc run::

      python gh-pages.py version_number

    to build the html pages and copy them to pystar-doc

  - if pages look ok, push pystar-doc back to github

