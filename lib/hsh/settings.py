#!/usr/bin/env python
# encoding: utf-8

# ------------------------------------------------------------------------------
# Application Name
# ------------------------------------------------------------------------------
app_name = 'hsh'

# ------------------------------------------------------------------------------
# Version Number
# ------------------------------------------------------------------------------
major_version = "1"
minor_version = "1"
patch_version = "0"

# ------------------------------------------------------------------------------
# Debug Flag (switch to False for production release code)
# ------------------------------------------------------------------------------
debug = False

# ------------------------------------------------------------------------------
# Usage String
# ------------------------------------------------------------------------------
usage = """
REPORT HASH DIGEST
  hsh [filepath]
  hsh <command> [filepath]

FILE INTEGRITY CHECKS
  hsh [hash digest string 1] [hash digest string 2]
  hsh [filepath] [hash digest string]
  hsh [filepath 1] [filepath 2]
"""

# ------------------------------------------------------------------------------
# Help String
# ------------------------------------------------------------------------------
help = """
-------------------------------------------------
hsh
Simple file hash digests & file integrity checks
Copyright 2016 Christopher Simpkins
MIT license
Source: https://github.com/chrissimpkins/hsh
Docs: https://chrissimpkins.github.io/hsh/
-------------------------------------------------

ABOUT
  hsh generates MD5, SHA1, SHA224, SHA256, SHA384, and SHA512 hash digests for files and performs file integrity checks based upon hash digest string to hash digest string, file path to hash digest string, and file path to file path comparisons.

USAGE
  REPORT HASH DIGEST
    hsh [filepath]
    hsh <command> [filepath]

  FILE INTEGRITY CHECKS
    hsh [hash digest string 1] [hash digest string 2]
    hsh [filepath] [hash digest string]
    hsh [filepath 1] [filepath 2]

COMMANDS
    md5            report MD5 hash digest for file
    sha1           report SHA1 hash digest for file
    sha224         report SHA224 hash digest for file
    sha256         report SHA256 hash digest for file
    sha384         report SHA384 hash digest for file
    sha512         report SHA512 hash digest for file

OPTIONS
    -h --help      display help documentation
       --usage     display usage documentation
    -v --version   display application version

DESCRIPTION
  Hash digests are generated with the SHA256 algorithm by default. To modify this, add an explicit primary command argument (see COMMANDS above).

  Hash digest comparisons are performed with any file path and/or file hash digest string argument combination.  hsh supports comparisons of MD5, SHA1, SHA224, SHA256, SHA384, and SHA512 hash digests.  When you include a file hash digest string to compare with a file on a local file path, hsh generates the appropriate hash digest for the file path argument based upon the length of your file hash digest string argument.  When the hash digests differ, a diff indicator is displayed below the hash digest strings.  The = character indicates matching positions and the ^ character indicates positions that do not match.
"""
