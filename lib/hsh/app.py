#!/usr/bin/env python
# encoding: utf-8

#------------------------------------------------------------------------------
# hsh
# Copyright 2015 Christopher Simpkins
# MIT license
#------------------------------------------------------------------------------

# Application start
def main():
    import sys
    from hsh.library.hash import Hasher, HashChecker
    from Naked.commandline import Command
    from Naked.toolshed.file import FileReader
    from Naked.toolshed.system import file_exists, dir_exists, stdout, stderr

    #------------------------------------------------------------------------------------------
    # [ Instantiate command line object ]
    #   used for all subsequent conditional logic in the CLI application
    #------------------------------------------------------------------------------------------
    c = Command(sys.argv[0], sys.argv[1:])
    #------------------------------------------------------------------------------------------
    # [ Command Suite Validation ] - early validation of appropriate command syntax
    # Test that user entered at least one argument to the executable, print usage if not
    #------------------------------------------------------------------------------------------
    if not c.command_suite_validates():
        from hsh.settings import usage as hsh_usage
        print(hsh_usage)
        sys.exit(1)
    #------------------------------------------------------------------------------------------
    # [ NAKED FRAMEWORK COMMANDS ]
    # Naked framework provides default help, usage, and version commands for all applications
    #   --> settings for user messages are assigned in the lib/hsh/settings.py file
    #------------------------------------------------------------------------------------------
    if c.help():      # User requested hsh help information
        from hsh.settings import help as hsh_help
        print(hsh_help)
        sys.exit(0)
    elif c.usage():   # User requested hsh usage information
        from hsh.settings import usage as hsh_usage
        print(hsh_usage)
        sys.exit(0)
    elif c.version(): # User requested hsh version information
        from hsh.settings import app_name, major_version, minor_version, patch_version
        version_display_string = app_name + ' ' + major_version + '.' + minor_version + '.' + patch_version
        print(version_display_string)
        sys.exit(0)
    #------------------------------------------------------------------------------------------
    # [ PRIMARY COMMAND LOGIC ]
    #   Enter your command line parsing logic below
    #------------------------------------------------------------------------------------------

    primary_command = c.cmd.lower() #convert to lowercase to support user entry of upper case (e.g. SHA256) as primary command

    if primary_command == "sha1":
        if c.argc > 1:
            file_list = c.argv[1:]
            for file in file_list:
                if file_exists(file):
                    hasher = Hasher()
                    sha_hash = hasher.sha1(file)
                    stdout("SHA1 (" + file + ") :")
                    stdout(sha_hash)
                else:
                    stderr(file + " does not appear to be an existing file path.")
        else:
            stderr("You did not include a file in your command.  Please try again.")
    elif primary_command == "sha224":
        if c.argc > 1:
            file_list = c.argv[1:]
            for file in file_list:
                if file_exists(file):
                    hasher = Hasher()
                    sha_hash = hasher.sha224(file)
                    stdout("SHA224 (" + file + ") :")
                    stdout(sha_hash)
                else:
                    stderr(file + " does not appear to be an existing file path.")
        else:
            stderr("You did not include a file in your command.  Please try again.")
    elif primary_command == "sha256":
        if c.argc > 1:
            file_list = c.argv[1:]
            for file in file_list:
                if file_exists(file):
                    hasher = Hasher()
                    sha_hash = hasher.sha256(file)
                    stdout("SHA256 (" + file + ") :")
                    stdout(sha_hash)
                else:
                    stderr(file + " does not appear to be an existing file path.")
        else:
            stderr("You did not include a file in your command.  Please try again.")
    elif primary_command == "sha384":
        if c.argc > 1:
            file_list = c.argv[1:]
            for file in file_list:
                if file_exists(file):
                    hasher = Hasher()
                    sha_hash = hasher.sha384(file)
                    stdout("SHA384 (" + file + ") :")
                    stdout(sha_hash)
                else:
                    stderr(file + " does not appear to be an existing file path.")
        else:
            stderr("You did not include a file in your command.  Please try again.")
    elif primary_command == "sha512":
        if c.argc > 1:
            file_list = c.argv[1:]
            for file in file_list:
                if file_exists(file):
                    hasher = Hasher()
                    sha_hash = hasher.sha512(file)
                    stdout("SHA512 (" + file + ") :")
                    stdout(sha_hash)
                else:
                    stderr(file + " does not appear to be an existing file path.")
        else:
            stderr("You did not include a file in your command.  Please try again.")
    elif primary_command == "md5":
        if c.argc > 1:
            file_list = c.argv[1:]
            for file in file_list:
                if file_exists(file):
                    hasher = Hasher()
                    sha_hash = hasher.md5(file)
                    stdout("MD5 (" + file + ") :")
                    stdout(sha_hash)
                else:
                    stderr(file + " does not appear to be an existing file path.")
        else:
            stderr("You did not include a file in your command.  Please try again.")
    elif primary_command == "check":
        if c.argc == 3: # primary command + 2 arguments
            hc = HashChecker()
            hc.compare(c.argv[1:]) # pass the argument list excluding the primary command
        elif c.argc < 3:
            stderr("You did not include a file or hash digest for comparison.  Please try again.")
        elif c.argc > 3:
            stderr("Too many arguments.  Please include two arguments for comparison.")
    elif c.argc == 1: # single file hash digest request with default SHA256 settings
        file = c.arg0
        if file_exists(file):
            hasher = Hasher()
            sha_hash = hasher.sha256(file)
            stdout("SHA256 (" + file + ") :")
            stdout(sha_hash)
        else:
            stderr(c.arg0 + " does not appear to be an existing file path. Please try again.")
    elif c.argc == 2: # exactly two arguments, perform comparison between them by default
        hc = HashChecker()
        hc.compare(c.argv) # pass the entire argument list because there is no primary command

    #------------------------------------------------------------------------------------------
    # [ DEFAULT MESSAGE FOR MATCH FAILURE ]
    #  Message to provide to the user when all above conditional logic fails to meet a true condition
    #------------------------------------------------------------------------------------------
    else:
        print("Could not complete the command that you entered.  Please try again.")
        sys.exit(1) #exit


if __name__ == '__main__':
    main()
