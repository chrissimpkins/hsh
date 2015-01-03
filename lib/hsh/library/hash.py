#!/usr/bin/env python
# encoding: utf-8

import sys
import hashlib
from Naked.toolshed.file import FileReader

class Hasher(object):
    def __init__(self):
        pass

    #------------------------------------------------------------------------------
    # PUBLIC METHODS
    #------------------------------------------------------------------------------
    def md5(self, filepath):
        data = self._read_file(filepath)
        return hashlib.md5(data).hexdigest()

    def sha1(self, filepath):
        data = self._read_file(filepath)
        return hashlib.sha1(data).hexdigest()

    def sha224(self, filepath):
        data = self._read_file(filepath)
        return hashlib.sha224(data).hexdigest()

    def sha256(self, filepath):
        data = self._read_file(filepath)
        return hashlib.sha256(data).hexdigest()

    def sha384(self, filepath):
        data = self._read_file(filepath)
        return hashlib.sha384(data).hexdigest()

    def sha512(self, filepath):
        data = self._read_file(filepath)
        return hashlib.sha512(data).hexdigest()

    #------------------------------------------------------------------------------
    # PRIVATE METHODS
    #------------------------------------------------------------------------------

    def _read_file(self, filepath):
        fr = FileReader(filepath)
        return fr.read_bin()


class HashChecker(object):
    def __init__(self):
        pass
