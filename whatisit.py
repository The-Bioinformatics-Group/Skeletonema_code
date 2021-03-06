#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#	Copyright (C) 2017 Mats Töpel. mats.topel@marine.gu.se
#
#	Citation: If you use this version of the program, please cite;
#	
#	"Mats Töpel (2017) Open Laboratory Notebook. 
#	https://github.com/The-Bioinformatics-Group"
#
#	This program is free software: you can redistribute it and/or modify
#	it under the terms of the GNU General Public License as published by
#	the Free Software Foundation, either version 3 of the License, or
#	(at your option) any later version.
#	
#	This program is distributed in the hope that it will be useful,
#	but WITHOUT ANY WARRANTY; without even the implied warranty of
#	MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#	GNU General Public License for more details.
#
#	You should have received a copy of the GNU General Public License
#	along with this program.  If not, see <http://www.gnu.org/licenses/>.


# Usage: ./whatisit.py -f example/*.fastq -r example/RO5_Chloroplast.fst

import sys
from whatisit.mapping import bowtie2
from whatisit.files import file_name_base
import argparse

parser = argparse.ArgumentParser(prog=sys.argv[0], description="ADD A DESCRIPTION OF YOUR PROGRAM HERE.")
parser.add_argument("-f", "--fastq", help="Fastq file(s) with sequence data", required=True, nargs="*")
parser.add_argument("-r", "--references", help="Reference sequences in Fasta format", required=True, nargs="*")
parser.add_argument("-n", "--ncbi", help="Reference sequences in Fasta format (i.e. NCBI genome db", nargs="*")
parser.add_argument("--output_reads", help="Store the reads not mapping to the reference", default = False)
parser.add_argument("-p", "--threads", help="Number of alignment threads to launch", default = "1")
parser.add_argument("-v", "--verbose", action="store_true", help="Be more verbose")
args = parser.parse_args()

def main():
	
	# Run analysis
	x = 0
	for i in range(0, len(args.fastq), 2):
		# Mapp to references
		for db in args.references:
			bowtie2(args.fastq[x], args.fastq[x+1], db, args.threads, args.output_reads)
		x += 2

if __name__ == "__main__":
    main()
