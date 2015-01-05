# hsh

## Simple file hash digests and file integrity checks

Documentation: [https://github.com/chrissimpkins/hsh](https://github.com/chrissimpkins/hsh)

## About
hsh is a cross-platform command line application that generates file hash digests and performs file integrity checks via file hash digest comparisons. It supports the following hash algorithms:

- MD5
- SHA1
- SHA224
- SHA256
- SHA384
- SHA512

## Examples of hsh Features

### File Hash Digests

#### Default File Hash Digests (SHA256)

```
$ hsh somefile.txt
SHA256 (somefile.txt) :
5c2b47648ae96e60b5d02c573aefa6b01fb49d1b9e1ebd8a1b1a794cf522e6e3
```

#### Other Algorithms Available with a Command

```
$ hsh sha1 somefile.txt
SHA1 (somefile.txt) :
0e1fb609e951c85e01f4048f01f0b51256bb3917
```

### File Integrity Checks

#### File to File Comparisons

```
$ hsh firstfile.txt secondfile.txt

SHA256 (firstfile.txt) :
0dbe4bb7df0f6d271e8f1fc30ec586fdfb5218e5a615c9abd3843943b4779e9e
SHA256 (secondfile.txt) :
0dbe4bb7df0f6d271e8f1fc30ec586fdfb5218e5a615c9abd3843943b4779e9e

The hash digests are identical.
```

#### File to Hash Digest Comparisons

Include one of the supported file hash digest types as an argument and `hsh` automatically detects the hash algorithm and performs the test with your file:

```
$ hsh firstfile.txt 0e1fb609e951c85e01f4048f01f0b51256bb3917

SHA1 (firstfile.txt) :
0e1fb609e951c85e01f4048f01f0b51256bb3917
SHA1 (test) :
0e1fb609e951c85e01f4048f01f0b51256bb3917

The hash digests are identical.
```

#### Hash Digest to Hash Digest Comparisons

```
$ hsh da24f4932321286ac849f9145707f0e8 da24f4932321286ac849f9145707f0e9

da24f4932321286ac849f9145707f0e8
da24f4932321286ac849f9145707f0e9
===============================^

The hash digests are NOT identical.
```

A diff indicator is displayed below the hash digests when they differ.

## How to Install `hsh`

You can install `hsh` with the Python package manager, pip:

```
$ pip install hsh
```

or download the source, unpack it, navigate to the top level source directory, and run the following command:

```
$ python setup.py install
```

## How to Upgrade `hsh`

You can upgrade to a more recent release of `hsh` with the Python package manager, pip:

```
$ pip install --upgrade hsh
```

or repeat the installation from source instructions in the 'How to Install `hsh`' section above.

## Requirements

`hsh` requires a Python install on your system.  It has been tested in cPython v2.7.x & 3.4.x as well as in pypy v2.4.x (Python v2.7.8).

## Issue Reporting

Issue reporting is available on the GitHub repository.  [Here are the instructions](https://chrissimpkins.github.io/hsh/issues.html).

## Usage

Command line syntax and available commands & options are available in the [Usage documentation](https://chrissimpkins.github.io/hsh/usage.html) or with the following command:

```
$ hsh --help
```

## FAQ

The [FAQ](https://chrissimpkins.github.io/hsh/faq.html) has additional information about hash digests and the interpretation of their comparisons as well as a link to more information for those interested in further reading.

---
[MIT License](https://github.com/chrissimpkins/crypto/blob/master/docs/LICENSE) | Built with the [Naked Framework](https://pypi.python.org/pypi/Naked)




