#!/bin/sh

NOSE_FLAGS="--verbosity=2"
TEST_COMMAND="nosetests"

# Testing scripts
HASHER_CLASS="test_hasher_class.py"
HASH_CHECKER_CLASS="test_hashchecker_class.py"

# Test Runner

if [ "$1" = "all" ];then
	"$TEST_COMMAND" "$NOSE_FLAGS" "$HASHER_CLASS" "$HASH_CHECKER_CLASS"
elif [ "$1" = "hasher" ];then
	"$TEST_COMMAND" "$NOSE_FLAGS" "$HASHER_CLASS"
elif [ "$1" = "check" ]; then
	"$TEST_COMMAND" "$NOSE_FLAGS" "$HASH_CHECKER_CLASS"
else
	echo "Enter 'all' or a command suite to test."
	exit 1
fi
