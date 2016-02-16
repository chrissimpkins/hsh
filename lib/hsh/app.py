#!/usr/bin/env python
# -*- coding: utf-8 -*-

# ------------------------------------------------------------------------------
# hsh
# Copyright 2016 Christopher Simpkins
# MIT license
# ------------------------------------------------------------------------------

import sys

from commandlines import Command

from hsh.library.hash import Hasher, HashChecker, file_exists
from hsh.settings import help as hsh_help
from hsh.settings import usage as hsh_usage
from hsh.settings import app_name, major_version, minor_version, patch_version


def main():

    c = Command()

    if c.does_not_validate_missing_args():
        print(hsh_usage)
        sys.exit(1)

    if c.is_help_request():  # User requested hsh help information
        print(hsh_help)
        sys.exit(0)
    elif c.is_usage_request():   # User requested hsh usage information
        print(hsh_usage)
        sys.exit(0)
    elif c.is_version_request():  # User requested hsh version information
        version_display_string = app_name + ' ' + major_version + '.' + minor_version + '.' + patch_version
        print(version_display_string)
        sys.exit(0)

    primary_command = c.subcmd.lower()  # make the subcommand case-independent

    if primary_command == "sha1":
        if c.argc > 1:
            file_list = c.argv[1:]
            for file in file_list:
                if file_exists(file):
                    hasher = Hasher()
                    sha_hash = hasher.sha1(file)
                    print("SHA1 (" + file + ") :")
                    print(sha_hash)
                else:
                    sys.stderr.write(file + " does not appear to be an existing file path.\n")
        else:
            sys.stderr.write("You did not include a file in your command.  Please try again.\n")
            sys.exit(1)
    elif primary_command == "sha224":
        if c.argc > 1:
            file_list = c.argv[1:]
            for file in file_list:
                if file_exists(file):
                    hasher = Hasher()
                    sha_hash = hasher.sha224(file)
                    print("SHA224 (" + file + ") :")
                    print(sha_hash)
                else:
                    sys.stderr.write(file + " does not appear to be an existing file path.\n")
        else:
            sys.stderr.write("You did not include a file in your command.  Please try again.\n")
            sys.exit(1)
    elif primary_command == "sha256":
        if c.argc > 1:
            file_list = c.argv[1:]
            for file in file_list:
                if file_exists(file):
                    hasher = Hasher()
                    sha_hash = hasher.sha256(file)
                    print("SHA256 (" + file + ") :")
                    print(sha_hash)
                else:
                    sys.stderr.write(file + " does not appear to be an existing file path.\n")
        else:
            sys.stderr.write("You did not include a file in your command.  Please try again.\n")
            sys.exit(1)
    elif primary_command == "sha384":
        if c.argc > 1:
            file_list = c.argv[1:]
            for file in file_list:
                if file_exists(file):
                    hasher = Hasher()
                    sha_hash = hasher.sha384(file)
                    print("SHA384 (" + file + ") :")
                    print(sha_hash)
                else:
                    sys.stderr.write(file + " does not appear to be an existing file path.\n")
        else:
            sys.stderr.write("You did not include a file in your command.  Please try again.\n")
            sys.exit(1)
    elif primary_command == "sha512":
        if c.argc > 1:
            file_list = c.argv[1:]
            for file in file_list:
                if file_exists(file):
                    hasher = Hasher()
                    sha_hash = hasher.sha512(file)
                    print("SHA512 (" + file + ") :")
                    print(sha_hash)
                else:
                    sys.stderr.write(file + " does not appear to be an existing file path.\n")
        else:
            sys.stderr.write("You did not include a file in your command.  Please try again.\n")
            sys.exit(1)
    elif primary_command == "md5":
        if c.argc > 1:
            file_list = c.argv[1:]
            for file in file_list:
                if file_exists(file):
                    hasher = Hasher()
                    sha_hash = hasher.md5(file)
                    print("MD5 (" + file + ") :")
                    print(sha_hash)
                else:
                    sys.stderr.write(file + " does not appear to be an existing file path.\n")
        else:
            sys.stderr.write("You did not include a file in your command.  Please try again.\n")
            sys.exit(1)
    elif primary_command == "check":
        if c.argc == 3:  # primary command + 2 arguments
            hc = HashChecker()
            hc.compare(c.argv[1:])  # pass the argument list excluding the primary command
        elif c.argc < 3:
            sys.stderr.write("You did not include a file or hash digest for comparison.  Please try again.\n")
            sys.exit(1)
        elif c.argc > 3:
            sys.stderr.write("Too many arguments.  Please include two arguments for comparison.\n")
            sys.exit(1)
    elif c.argc == 1:  # single file hash digest request with default SHA256 settings
        file = c.arg0
        if file_exists(file):
            hasher = Hasher()
            sha_hash = hasher.sha256(file)
            print("SHA256 (" + file + ") :")
            print(sha_hash)
        else:
            sys.stderr.write(c.arg0 + " does not appear to be an existing file path. Please try again.\n")
            sys.exit(1)
    elif c.argc == 2:  # exactly two arguments, perform comparison between them by default
        hc = HashChecker()
        hc.compare(c.argv)  # pass the entire argument list because there is no primary command

    else:
        print("Could not complete the command that you entered.  Please try again.")
        sys.exit(1)


if __name__ == '__main__':
    main()
