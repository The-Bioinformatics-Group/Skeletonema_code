#!/usr/bin/env python

# Licence: 

# Usage:

import sys

try:
    import argparse
except ImportError:
	sys.stderr.write("[Error] The python module 'argparse' is not installed\n")
	sys.stderr.write("[--] Would you like to install it now using 'sudo easy_install' [Y/N]? ")
	answer = sys.stdin.readline()
	if answer[0].lower() == "y":
		sys.stderr.write("[--] Running 'sudo easy_install argparse'\n")
		from subprocess import call
		call(["sudo", "easy_install", "argparse"])
	else:
		sys.exit("[Error] Exiting due to missing dependency 'argparser'")
														        
parser = argparse.ArgumentParser(prog=sys.argv[0], description="ADD A DESCRIPTION OF YOUR PROGRAM HERE.")
parser.add_argument("-v", "--verbose", action="store_true", help="Be more verbose")
args = parser.parse_args()

def main():
	### Remove the next line and add your own code instead ###
	print "Try '%s -h'" % sys.argv[0]


if __name__ == "__main__":
    main()
