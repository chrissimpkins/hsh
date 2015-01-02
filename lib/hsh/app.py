#!/usr/bin/env python
# encoding: utf-8

#------------------------------------------------------------------------------
# hsh
# Copyright 2015 Christopher Simpkins
# MIT license
#------------------------------------------------------------------------------

#------------------------------------------------------------------------------------
# c.cmd = Primary command (hsh <primary command>)
# c.cmd2 = Secondary command (hsh <primary command> <secondary command>)
#
# c.arg_to_cmd = first positional argument to the primary command
# c.arg_to_cmd2 = first positional argument to the secondary command
#
# c.option(option_string, [bool argument_required]) = test for option with optional positional argument to option test
# c.option_with_arg(option_string) = test for option and mandatory positional argument to option
# c.flag(flag_string) = test for presence of a "option=argument" style flag
#
# c.arg(arg_string) = returns the next positional argument to the arg_string argument
# c.flag_arg(flag_string) = returns the flag assignment for a "--option=argument" style flag
#------------------------------------------------------------------------------------

# Application start
def main():
    import sys
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

    # [[ Example usage ]] ------------------------------->>>
    # if c.cmd == 'hello':
    #     if c.cmd2 = 'world':
    # 	      if c.option('--print'):
    # 		      print('Hello World!')
    # elif c.cmd == 'spam':
    #     if c.option_with_arg('--with'):
    # 		  friend_of_spam = c.arg('--with')    # user enters hsh spam --with eggs
    # 		  print('spam and ' + friend_of_spam) # prints 'spam and eggs'
    # elif c.cmd == 'naked':
    #     if c.flag("--language"):
    #         lang = c.flag_arg("--language")     # user enters hsh naked --language=python
    #         print("Naked & " + lang)            # prints 'Naked & python'
    # End example --------------------------------------->>>

    primary_command = c.cmd.lower() #convert to lowercase to support user entry of upper case (e.g. SHA256) as primary command

    if primary_command == "sha1":
        if c.argc > 1:
            if c.argc == 1:
                pass #single file
            else:
                pass #multiple files
        else:
            stdout("nope")
    elif primary_command == "sha224":
        print("sha224")
    elif primary_command == "sha256":
        print("sha256")
    elif primary_command == "sha384":
        print("sha384")
    elif primary_command == "sha512":
        print("sha512")
    elif primary_command == "md5":
        print("md5")
    elif primary_command == "check":
        pass # checksum comparison between files or file and explicit hash digest (determined by length of digest)
    elif c.argc == 1:
        pass # single argument, perform default SHA256 hash digest generation
    elif c.argc == 2: # exactly two arguments, perform default comparison between them
        pass


    #------------------------------------------------------------------------------------------
    # [ DEFAULT MESSAGE FOR MATCH FAILURE ]
    #  Message to provide to the user when all above conditional logic fails to meet a true condition
    #------------------------------------------------------------------------------------------
    else:
        print("Could not complete the command that you entered.  Please try again.")
        sys.exit(1) #exit

if __name__ == '__main__':
    main()
