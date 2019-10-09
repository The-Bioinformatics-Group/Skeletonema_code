#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#   Copyright (C) 2017 Mats Töpel. mats.topel@marine.gu.se
#
#   Citation: If you use this version of the program, please cite;
#
#   "Mats Töpel (2017) Open Laboratory Notebook.
#   https://github.com/The-Bioinformatics-Group"
#
#   This program is free software: you can redistribute it and/or modify
#   it under the terms of the GNU General Public License as published by
#   the Free Software Foundation, either version 3 of the License, or
#   (at your option) any later version.
#
#   This program is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU General Public License for more details.
#
#   You should have received a copy of the GNU General Public License
#   along with this program.  If not, see <http://www.gnu.org/licenses/>.




###########################################
# Decoding SAM flags 
# https://broadinstitute.github.io/picard/explain-flags.html
#
# Example: cut -f2 out.sam | sort -u
# 77  = read paired (0x1), read unmapped (0x4), mate unmapped (0x8), first in pair (0x40)
# 141 = read paired (0x1), read unmapped (0x4), mate unmapped (0x8), second in pair (0x40) 
#
# Sum of all applicable flags. Flags relevant to Bowtie are:
#
# 1	  The read is one of a pair
# 2	  The alignment is one end of a proper paired-end alignment
# 4   The read has no reported alignments
# 8   The read is one of a pair and has no reported alignments
# 16  The alignment is to the reverse reference strand
# 32  The other mate in the paired-end alignment is aligned to the reverse reference strand
# 64  The read is mate 1 in a pair
# 128 The read is mate 2 in a pair
#
# Thus, an unpaired read that aligns to the reverse reference strand will have flag 16. 
# A paired-end read that aligns and is the first mate in the pair will have flag 83 (= 64 + 16 + 2 + 1).
#############################################

import subprocess
import sys
import os 


# Takes a fasta file with references and creates a Bowtie2 index
def index(reference):
	# Check if index exists instead...
	subprocess.call(["bowtie2-build", reference, files.file_name_base(reference)])

# Takes a pair of fastq files and a fasta file with genome references as input
# Returns a dictioneary with the counts of mapped reads to the individual reference "species"
def bowtie2(fastq1, fastq2, reference, threads, store_reads, interleaved = False, mapped = False):
#	indexed_db = files.file_name_base(reference)
	# Check if indexed database is available
#	if reference + "1.bt2":
#		pass
#	else:
#		index(reference)
#	index(reference)
	# Check if first or second alignment run

	FNULL = open(os.devnull, 'w')

	if interleaved == False:
		sam = subprocess.Popen(["bowtie2",\
					       "-p", threads,\
					       "-x", reference,\
					       "-1", fastq1,\
					       "-2", fastq2], stderr=subprocess.PIPE, stdout=FNULL)
	bowtie_stderr = sam.communicate()[1]
	for line in bowtie_stderr.decode("utf-8").split("\n"):
		if "aligned concordantly exactly 1 time" in line:
			concord_1 = line.split()[0]
		elif "aligned concordantly >1 times" in line:
			concord_2 = line.split()[0]
		elif "aligned discordantly 1 time" in line:
			discord = line.split()[0]
		elif "aligned exactly 1 time" in line:
			exact = line.split()[0]
		elif "aligned >1 times" in line:
			multimap = line.split()[0]
			
	print(os.path.basename(reference), "\t", concord_1, "\t", concord_2, "\t", discord, "\t", exact, "\t", multimap)
