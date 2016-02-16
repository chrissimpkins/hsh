#!/usr/bin/env python
# encoding: utf-8

import sys
import os
import unittest
import pexpect
from hsh.library.hash import HashChecker


class HashCheckerClassTest(unittest.TestCase):

    def setUp(self):
        self.testfile1_path = "testdir1/hashtest.txt"     # main test file
        self.testfile2_path = "testdir1/hashtest-mod.txt" # modified version of the testfile1
        self.testfile3_path = "testdir1/hashtest-dup.txt" # duplicate of the testfile1
        self.hashtest_md5_hash = "e1eadba7c29a7c251073da9de91a08c0"
        self.hashtest_md5_hash_bad = "e1eadba7c29a7c251073da9de91a08c1" # slightly modified
        self.hashtest_sha1_hash = "e5dd269504b4400ee18d723077d9de761695699e"
        self.hashtest_sha1_hash_bad = "e5dd269504b4400ee18d723077d9de761695699d" # slightly modified
        self.hashtest_sha224_hash = "22ad9b21f5f46d7734a2562f45d3ad598914976798aed542195859b8"
        self.hashtest_sha224_hash_bad = "22ad9b21f5f46d7734a2562f45d3ad598914976798aed542195859b2" # slightly modified
        self.hashtest_sha256_hash = "beed7da44e4597faa81ffea24ba508efaf25d9df75019fec37b4d673174c5757"
        self.hashtest_sha256_hash_bad = "beed7da44e4597faa81ffea24ba508efaf25d9df75019fec37b4d673174c5756" # slightly modified
        self.hashtest_sha384_hash = "e31fdb3c9913879c7ef5848df430da0889c710add335e09ed4939a6229c1a188fa486efe8ec7f50b4da396edb59cf683"
        self.hashtest_sha384_hash_bad = "e31fdb3c9913879c7ef5848df430da0889c710add335e09ed4939a6229c1a188fa486efe8ec7f50b4da396edb59cf682" # slightly modified
        self.hashtest_sha512_hash = "e9ccee5c828cf89ea44f33ea633c73cde4d4d5e28c1084eabed5d04414029e13f9523dd1a616fa3d1cd90b92d068d1a6ff23a326916c07751d15d7c46a680bd4"
        self.hashtest_sha512_hash_bad = "e9ccee5c828cf89ea44f33ea633c73cde4d4d5e28c1084eabed5d04414029e13f9523dd1a616fa3d1cd90b92d068d1a6ff23a326916c07751d15d7c46a680bd2" # slightly modified
        self.fake_hash = "thisisbogus"

    def tearDown(self):
        pass

    # ------------------------------------------------------------------------------
    # Test Appropriate Detection of Hash Digests and Assignment of Test Hash Algo Type
    # ------------------------------------------------------------------------------

    def test_is_hash_md5(self):
        hc = HashChecker()
        self.assertTrue(hc.is_hash(self.hashtest_md5_hash))
        self.assertEqual(hc.hash_type, "md5")

    def test_is_hash_sha1(self):
        hc = HashChecker()
        self.assertTrue(hc.is_hash(self.hashtest_sha1_hash))
        self.assertEqual(hc.hash_type, "sha1")

    def test_is_hash_sha224(self):
        hc = HashChecker()
        self.assertTrue(hc.is_hash(self.hashtest_sha224_hash))
        self.assertEqual(hc.hash_type, "sha224")

    def test_is_hash_sha256(self):
        hc = HashChecker()
        self.assertTrue(hc.is_hash(self.hashtest_sha256_hash))
        self.assertEqual(hc.hash_type, "sha256")

    def test_is_hash_sha384(self):
        hc = HashChecker()
        self.assertTrue(hc.is_hash(self.hashtest_sha384_hash))
        self.assertEqual(hc.hash_type, "sha384")

    def test_is_hash_sha512(self):
        hc = HashChecker()
        self.assertTrue(hc.is_hash(self.hashtest_sha512_hash))
        self.assertEqual(hc.hash_type, "sha512")

    def test_is_not_hash_bogusstring(self):
        hc = HashChecker()
        self.assertFalse(hc.is_hash(self.fake_hash))
        self.assertEqual(hc.hash_type, "")

    # ------------------------------------------------------------------------------
    # Hash to Hash Comparison
    # ------------------------------------------------------------------------------

    # test successful comparison
    def test_hash_to_hash_success_expected(self):
        hc = HashChecker()
        hc.hash_one = self.hashtest_md5_hash
        hc.hash_two = self.hashtest_md5_hash
        self.assertTrue(hc.hash_to_hash())

    # test failed comparison
    def test_hash_to_hash_fail_expected(self):
        hc = HashChecker()
        hc.hash_one = self.hashtest_md5_hash
        hc.hash_two = self.hashtest_sha1_hash
        self.assertFalse(hc.hash_to_hash())

    # ------------------------------------------------------------------------------
    # File to Hash Comparison
    # ------------------------------------------------------------------------------

    # test MD5 success
    def test_hash_to_file_md5_success_expected(self):
        hc = HashChecker()
        hc.hash_type = "md5"
        hc.filepath_one = self.testfile1_path
        hc.hash_one = self.hashtest_md5_hash
        ret_val = hc.file_to_hash()
        self.assertEqual(ret_val['type'], "MD5")
        self.assertEqual(ret_val['filehash'], self.hashtest_md5_hash)
        self.assertTrue(ret_val['is_equal'])

    # test MD5 failure
    def test_hash_to_file_md5_failure_expected(self):
        hc = HashChecker()
        hc.hash_type = "md5"
        hc.filepath_one = self.testfile1_path
        hc.hash_one = self.hashtest_md5_hash_bad
        ret_val = hc.file_to_hash()
        self.assertEqual(ret_val['type'], "MD5")
        self.assertEqual(ret_val['filehash'], self.hashtest_md5_hash)
        self.assertFalse(ret_val['is_equal'])

    # test SHA1 success
    def test_hash_to_file_sha1_success_expected(self):
        hc = HashChecker()
        hc.hash_type = "sha1"
        hc.filepath_one = self.testfile1_path
        hc.hash_one = self.hashtest_sha1_hash
        ret_val = hc.file_to_hash()
        self.assertEqual(ret_val['type'], "SHA1")
        self.assertEqual(ret_val['filehash'], self.hashtest_sha1_hash)
        self.assertTrue(ret_val['is_equal'])

    # test SHA1 failure
    def test_hash_to_file_sha1_failure_expected(self):
        hc = HashChecker()
        hc.hash_type = "sha1"
        hc.filepath_one = self.testfile1_path
        hc.hash_one = self.hashtest_sha1_hash_bad
        ret_val = hc.file_to_hash()
        self.assertEqual(ret_val['type'], "SHA1")
        self.assertEqual(ret_val['filehash'], self.hashtest_sha1_hash)
        self.assertFalse(ret_val['is_equal'])

    # test SHA224 success
    def test_hash_to_file_sha224_success_expected(self):
        hc = HashChecker()
        hc.hash_type = "sha224"
        hc.filepath_one = self.testfile1_path
        hc.hash_one = self.hashtest_sha224_hash
        ret_val = hc.file_to_hash()
        self.assertEqual(ret_val['type'], "SHA224")
        self.assertEqual(ret_val['filehash'], self.hashtest_sha224_hash)
        self.assertTrue(ret_val['is_equal'])

    # test SHA224 failure
    def test_hash_to_file_sha224_failure_expected(self):
        hc = HashChecker()
        hc.hash_type = "sha224"
        hc.filepath_one = self.testfile1_path
        hc.hash_one = self.hashtest_sha224_hash_bad
        ret_val = hc.file_to_hash()
        self.assertEqual(ret_val['type'], "SHA224")
        self.assertEqual(ret_val['filehash'], self.hashtest_sha224_hash)
        self.assertFalse(ret_val['is_equal'])

    # test SHA256 success
    def test_hash_to_file_sha256_success_expected(self):
        hc = HashChecker()
        hc.hash_type = "sha256"
        hc.filepath_one = self.testfile1_path
        hc.hash_one = self.hashtest_sha256_hash
        ret_val = hc.file_to_hash()
        self.assertEqual(ret_val['type'], "SHA256")
        self.assertEqual(ret_val['filehash'], self.hashtest_sha256_hash)
        self.assertTrue(ret_val['is_equal'])

    # test SHA256 failure
    def test_hash_to_file_sha256_failure_expected(self):
        hc = HashChecker()
        hc.hash_type = "sha256"
        hc.filepath_one = self.testfile1_path
        hc.hash_one = self.hashtest_sha256_hash_bad
        ret_val = hc.file_to_hash()
        self.assertEqual(ret_val['type'], "SHA256")
        self.assertEqual(ret_val['filehash'], self.hashtest_sha256_hash)
        self.assertFalse(ret_val['is_equal'])

    # test SHA384 success
    def test_hash_to_file_sha384_success_expected(self):
        hc = HashChecker()
        hc.hash_type = "sha384"
        hc.filepath_one = self.testfile1_path
        hc.hash_one = self.hashtest_sha384_hash
        ret_val = hc.file_to_hash()
        self.assertEqual(ret_val['type'], "SHA384")
        self.assertEqual(ret_val['filehash'], self.hashtest_sha384_hash)
        self.assertTrue(ret_val['is_equal'])

    # test SHA384 failure
    def test_hash_to_file_sha384_failure_expected(self):
        hc = HashChecker()
        hc.hash_type = "sha384"
        hc.filepath_one = self.testfile1_path
        hc.hash_one = self.hashtest_sha384_hash_bad
        ret_val = hc.file_to_hash()
        self.assertEqual(ret_val['type'], "SHA384")
        self.assertEqual(ret_val['filehash'], self.hashtest_sha384_hash)
        self.assertFalse(ret_val['is_equal'])

    # test SHA512 success
    def test_hash_to_file_sha512_success_expected(self):
        hc = HashChecker()
        hc.hash_type = "sha512"
        hc.filepath_one = self.testfile1_path
        hc.hash_one = self.hashtest_sha512_hash
        ret_val = hc.file_to_hash()
        self.assertEqual(ret_val['type'], "SHA512")
        self.assertEqual(ret_val['filehash'], self.hashtest_sha512_hash)
        self.assertTrue(ret_val['is_equal'])

    # test SHA512 failure
    def test_hash_to_file_sha512_failure_expected(self):
        hc = HashChecker()
        hc.hash_type = "sha512"
        hc.filepath_one = self.testfile1_path
        hc.hash_one = self.hashtest_sha512_hash_bad
        ret_val = hc.file_to_hash()
        self.assertEqual(ret_val['type'], "SHA512")
        self.assertEqual(ret_val['filehash'], self.hashtest_sha512_hash)
        self.assertFalse(ret_val['is_equal'])

    # ------------------------------------------------------------------------------
    # File to File Comparison
    # ------------------------------------------------------------------------------

    def test_file_to_file_success_expected(self):
        hc = HashChecker()
        hc.filepath_one = self.testfile1_path
        hc.filepath_two = self.testfile3_path # a duplicate of the above file
        ret_val = hc.file_to_file()
        self.assertEqual(ret_val['type'], "SHA256")
        self.assertEqual(ret_val['filehash1'], self.hashtest_sha256_hash)
        self.assertEqual(ret_val['filehash2'], self.hashtest_sha256_hash)
        self.assertTrue(ret_val['is_equal'])

    def test_file_to_file_failure_expected(self):
        hc = HashChecker()
        hc.filepath_one = self.testfile1_path
        hc.filepath_two = self.testfile2_path # a slightly modified version of above file (should change hash)
        ret_val = hc.file_to_file()
        self.assertEqual(ret_val['type'], "SHA256")
        self.assertEqual(ret_val['filehash1'], self.hashtest_sha256_hash)
        self.assertFalse(ret_val['is_equal'])


