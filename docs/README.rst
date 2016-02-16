.. image:: https://travis-ci.org/chrissimpkins/hsh.svg?branch=master
    :target: https://travis-ci.org/chrissimpkins/hsh

Documentation: https://chrissimpkins.github.io/hsh/

Description
-------------

hsh is a cross-platform command line application that generates file hash digests and performs file integrity checks via file hash digest comparisons. It supports the following hash algorithms:

* MD5
* SHA1
* SHA224
* SHA256
* SHA384
* SHA512

Install
-------

Install with ``pip`` using the command:

.. code-block:: bash

    $ pip install hsh

or `download the source repository <https://github.com/chrissimpkins/hsh/tarball/master>`_, unpack it, and navigate to the top level of the repository.  Then enter:

.. code-block:: bash

    $ python setup.py install


Upgrade
-------

You can upgrade your hsh version with the command:

.. code-block:: bash

    $ pip install --upgrade hsh


Examples of hsh File Hash Digest Features
-----------------------------------------

Default SHA256 File Hash Digests
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: bash

    $ hsh somefile.txt
    SHA256 (somefile.txt) :
    5c2b47648ae96e60b5d02c573aefa6b01fb49d1b9e1ebd8a1b1a794cf522e6e3

Change the File Hash Digest Algorithm with a Command
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: bash

    $ hsh sha1 somefile.txt
    SHA1 (somefile.txt) :
    0e1fb609e951c85e01f4048f01f0b51256bb3917


Examples of hsh File Integrity Check Features
---------------------------------------------

Default SHA256 Digest File to File Comparisons
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: bash

    $ hsh firstfile.txt secondfile.txt

    SHA256 (firstfile.txt) :
    0dbe4bb7df0f6d271e8f1fc30ec586fdfb5218e5a615c9abd3843943b4779e9e
    SHA256 (secondfile.txt) :
    0dbe4bb7df0f6d271e8f1fc30ec586fdfb5218e5a615c9abd3843943b4779e9e

    The hash digests are identical.


Automated File to File Hash Digest Comparisons for Supported Hash Types
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: bash

    $ hsh firstfile.txt 0e1fb609e951c85e01f4048f01f0b51256bb3917

    SHA1 (firstfile.txt) :
    0e1fb609e951c85e01f4048f01f0b51256bb3917
    SHA1 (test) :
    0e1fb609e951c85e01f4048f01f0b51256bb3917

    The hash digests are identical.


File Hash Digest to File Hash Digest Comparisons
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: bash

    $ hsh da24f4932321286ac849f9145707f0e8 da24f4932321286ac849f9145707f0e9

    da24f4932321286ac849f9145707f0e8
    da24f4932321286ac849f9145707f0e9
    ===============================^

    The hash digests are NOT identical.

A diff string is displayed below the hash digests when they differ as shown in the example above.


Usage
-----

Command line syntax and available commands & options are available in `the documentation <https://chrissimpkins.github.io/hsh/usage.html>`_ or by entering the command:

.. code-block:: bash

    $ hsh --help


License
-------

`MIT License <https://github.com/chrissimpkins/hsh/blob/master/docs/LICENSE>`_


