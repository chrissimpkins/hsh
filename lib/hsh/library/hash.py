#!/usr/bin/env python
# encoding: utf-8

import sys
import hashlib
from Naked.toolshed.file import FileReader
from Naked.toolshed.system import file_exists, stdout, stderr

#------------------------------------------------------------------------------
# Hasher class - generate MD5 and SHA hash digests from files
#------------------------------------------------------------------------------
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


#------------------------------------------------------------------------------
# HashChecker class - compares hash digests by
#   - digest vs. digest
#   - digest vs. file
#   - file vs. file
#------------------------------------------------------------------------------
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

    #------------------------------------------------------------------------------
    # PUBLIC METHOD
    #------------------------------------------------------------------------------
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
                stderr(" ")
                stderr(self.error_one + " does not appear to be a file path or supported hash digest.  Please try again.")
                sys.exit(1)
            else:
                stderr(" ")
                stderr(self.error_one + " does not appear to be a file path or supported hash digest.")
                stderr(self.error_two + " does not appear to be a file path or supported hash digest.")
                stderr("Please try again.")
                sys.exit(1)
        else:
            if self.hashes == 2 and self.files == 0:
                if self.hash_to_hash() == True:
                    stdout(" ")
                    stdout("The hash digests are identical.")
                else:
                    stdout(" ")
                    stdout(self.hash_one)
                    stdout(self.hash_two)
                    stdout(self.differ(self.hash_one, self.hash_two))
                    stdout(" ")
                    stdout("The hash digests are NOT identical.")
            elif self.hashes == 1 and self.files == 1:
                result_dict = self.file_to_hash()
                stdout(result_dict['type'] + " (" + self.filepath_one + ") :")
                stdout(result_dict['filehash'])
                stdout(result_dict['type'] + " (test) :")
                stdout(self.hash_one)
                if result_dict['is_equal'] == True:
                    stdout(" ")
                    stdout("The hash digests are identical.")
                else:
                    stdout(self.differ(result_dict['filehash'], self.hash_one))
                    stdout(" ")
                    stdout("The hash digests are NOT identical.")
            elif self.hashes == 0 and self.files == 2:
                result_dict = self.file_to_file()
                stdout(result_dict['type'] + " (" + self.filepath_one + ") :")
                stdout(result_dict['filehash1'])
                stdout(result_dict['type'] + " (" + self.filepath_two + ") :")
                stdout(result_dict['filehash2'])
                if result_dict['is_equal'] == True:
                    stdout(" ")
                    stdout("The hash digests are identical.")
                else:
                    stdout(self.differ(result_dict['filehash1'], result_dict['filehash2']))
                    stdout(" ")
                    stdout("The hash digests are NOT identical.")

    #------------------------------------------------------------------------------
    # PRIVATE METHODS
    #------------------------------------------------------------------------------

    # determine whether the string is an expected hash digest length, assume the algorithm type based upon length
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

    # compare hash digest CL argument to hash digest CL argument (direct string comparison)
    def hash_to_hash(self):
        if self.hash_one == self.hash_two:
            return True
        else:
            return False

    # compare hash digest generated from file CL argument to a test hash digest string CL argument
    def file_to_hash(self):
        # create Hasher object to read file and generate appropriate hash digest
        hasher = Hasher()

        if self.hash_type == "md5":
            hash_digest = hasher.md5(self.filepath_one)
            return {'type': 'MD5', 'filehash': hash_digest, 'is_equal': hash_digest == self.hash_one}
        elif self.hash_type == "sha1":
            hash_digest = hasher.sha1(self.filepath_one)
            return {'type': 'SHA1', 'filehash': hash_digest, 'is_equal': hash_digest == self.hash_one}
        elif self.hash_type == "sha224":
            hash_digest = hasher.sha224(self.filepath_one)
            return {'type': 'SHA224', 'filehash': hash_digest, 'is_equal': hash_digest == self.hash_one}
        elif self.hash_type == "sha256":
            hash_digest = hasher.sha256(self.filepath_one)
            return {'type': 'SHA256', 'filehash': hash_digest, 'is_equal': hash_digest == self.hash_one}
        elif self.hash_type == "sha384":
            hash_digest = hasher.sha384(self.filepath_one)
            return {'type': 'SHA384', 'filehash': hash_digest, 'is_equal': hash_digest == self.hash_one}
        elif self.hash_type == "sha512":
            hash_digest = hasher.sha512(self.filepath_one)
            return {'type': 'SHA512', 'filehash': hash_digest, 'is_equal': hash_digest == self.hash_one}

    # compare file CL argument to file CL argument by generating SHA256 hash digest for each file and comparing
    def file_to_file(self):
        hasher = Hasher()
        hash_digest_one = hasher.sha256(self.filepath_one)
        hash_digest_two = hasher.sha256(self.filepath_two)

        return {'type': 'SHA256', 'filehash1': hash_digest_one, 'filehash2': hash_digest_two, 'is_equal': hash_digest_one == hash_digest_two}

    # create a diff indicator for the non-matched positions on the hash strings (called from compare() function above)
    def differ(self, file_hash, test_hash):
        diff_list = []
        i = 0
        if len(file_hash) == len(test_hash):
            for x in file_hash:
                if test_hash[i] == x:
                    diff_list.append('=')
                else:
                    diff_list.append('^')
                i += 1
            return ''.join(diff_list)
        else:
            return " "




