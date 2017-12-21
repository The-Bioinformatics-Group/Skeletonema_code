#!/usr/bin/env python

# Licence: 

# Usage:

import sys
from whatisit.mapping import bowtie2
from whatisit.files import file_name_base

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
parser.add_argument("-f", "--fastq", help="Fastq file(s) with sequence data", required=True, nargs="*")
parser.add_argument("-r", "--references", help="Reference sequences in Fasta format", required=True)
parser.add_argument("-v", "--verbose", action="store_true", help="Be more verbose")
args = parser.parse_args()

def main():
	
	# Run mapping analysis
	x = 0
	for i in range(0, len(args.fastq), 2):
		bowtie2(args.fastq[x], args.fastq[x+1], args.references, file_name_base(args.fastq[x]))
		x += 2

if __name__ == "__main__":
    main()
