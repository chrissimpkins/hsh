#!/usr/bin/env python
# encoding: utf-8

import sys
import hashlib
from Naked.toolshed.file import FileReader
from Naked.toolshed.system import file_exists, stdout, stderr

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
        self.files = 0
        self.hashes = 0
        self.error = False
        self.error_number = 0
        self.error_one = ""
        self.error_two = ""
        self.filepath_one = ""
        self.filepath_two = ""
        self.hash_one = ""
        self.hash_two = ""
        self.hash_type = ""

    def compare(self, arg_list):
        for argument in arg_list:
            if file_exists(argument):
                if self.files == 0:
                    self.filepath_one = argument
                else:
                    self.filepath_two = argument
                self.files += 1
            elif self.is_hash(argument):
                if self.hashes == 0:
                    self.hash_one = argument
                else:
                    self.hash_two = argument
                self.hashes += 1
            else:
                self.error = True
                if self.error_number == 0:
                    self.error_one = argument
                else:
                    self.error_two = argument
                self.error_number += 1

        if self.error == True:
            if self.error_number == 1:
                stderr(self.error_one + " does not appear to be a file path or hash digest.  Please try again.")
                sys.exit(1)
            else:
                stderr(self.error_one + " does not appear to be a file path or hash digest.")
                stderr(self.error_two + " does not appear to be a file path or hash digest.")
                stderr("Please try again.")
                sys.exit(1)
        else:
            if self.hashes == 2 and self.files == 0:
                if self.hash_to_hash() == True:
                    stdout(" ")
                    stdout("The hash digests are identical.")
                else:
                    stdout(" ")
                    stdout("The hash digests are NOT identical.")
            elif self.hashes == 1 and self.files == 1:
                result_dict = self.file_to_hash()
                stdout(result_dict['type'] + " (" + self.filepath_one + ") :")
                stdout(result_dict['filehash'])
                stdout(result_dict['type'] + " (test) :")
                stdout(self.hash_one)
                stdout(" ")
                if result_dict['is_equal'] == True:
                    stdout("The hash digests are identical.")
                else:
                    stdout("The hash digests are NOT identical.")
            elif self.hashes == 0 and self.files == 2:
                result_dict = self.file_to_file()
                stdout(result_dict['type'] + " (" + self.filepath_one + ") :")
                stdout(result_dict['filehash1'])
                stdout(result_dict['type'] + " (" + self.filepath_two + ") :")
                stdout(result_dict['filehash2'])
                stdout(" ")
                if result_dict['is_equal'] == True:
                    stdout("The hash digests are identical.")
                else:
                    stdout("The hash digests are NOT identical.")


    def is_hash(self, test_hash):
        hash_length = len(test_hash)

        if hash_length == 32:
            self.hash_type = "md5"
            return True
        elif hash_length == 40:
            self.hash_type = "sha1"
            return True
        elif hash_length == 56:
            self.hash_type = "sha224"
            return True
        elif hash_length == 64:
            self.hash_type = "sha256"
            return True
        elif hash_length == 96:
            self.hash_type = "sha384"
            return True
        elif hash_length == 128:
            self.hash_type = "sha512"
            return True
        else:
            return False

    def hash_to_hash(self):
        if self.hash_one == self.hash_two:
            return True
        else:
            return False

    def file_to_hash(self):
        data = self._read_file(self.filepath_one)

        if self.hash_type == "md5":
            hash_digest = hashlib.md5(data).hexdigest()
            return {'type': 'MD5', 'filehash': hash_digest, 'is_equal': hash_digest == self.hash_one}
        elif self.hash_type == "sha1":
            hash_digest = hashlib.sha1(data).hexdigest()
            return {'type': 'SHA1', 'filehash': hash_digest, 'is_equal': hash_digest == self.hash_one}
        elif self.hash_type == "sha224":
            hash_digest = hashlib.sha224(data).hexdigest()
            return {'type': 'SHA224', 'filehash': hash_digest, 'is_equal': hash_digest == self.hash_one}
        elif self.hash_type == "sha256":
            hash_digest = hashlib.sha256(data).hexdigest()
            return {'type': 'SHA256', 'filehash': hash_digest, 'is_equal': hash_digest == self.hash_one}
        elif self.hash_type == "sha384":
            hash_digest = hashlib.sha384(data).hexdigest()
            return {'type': 'SHA384', 'filehash': hash_digest, 'is_equal': hash_digest == self.hash_one}
        elif self.hash_type == "sha512":
            hash_digest = hashlib.sha512(data).hexdigest()
            return {'type': 'SHA512', 'filehash': hash_digest, 'is_equal': hash_digest == self.hash_one}

    def file_to_file(self):
        data_file_one = self._read_file(self.filepath_one)
        data_file_two = self._read_file(self.filepath_two)

        hash_digest_one = hashlib.sha256(data_file_one).hexdigest()
        hash_digest_two = hashlib.sha256(data_file_two).hexdigest()

        return {'type': 'SHA256', 'filehash1': hash_digest_one, 'filehash2': hash_digest_two, 'is_equal': hash_digest_one == hash_digest_two}

    #------------------------------------------------------------------------------
    # PRIVATE METHODS
    #------------------------------------------------------------------------------
    def _read_file(self, filepath):
        fr = FileReader(filepath)
        return fr.read_bin()
