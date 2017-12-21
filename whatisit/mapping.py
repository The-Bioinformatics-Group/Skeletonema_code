#!/usr/bin/env python

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
import json
import files

REF = "References"
SAM_HEADERS = ["@HD", "@SQ", "@RG", "@PG", "@CO"]

class Fastq_file(object):
	def __init__(self, name):
		self.name = name + ".unmapped" + ".fastq"
		self.OUTHANDLE = open(self.name, "w")

	# Takes a Fastq_read object as argument
	def add_seq(self, read):
		self.OUTHANDLE.write(read)
		
class Fastq_read(Fastq_file):
	def __init__(self, header, seq, qual):
		self.header = header
		self.seq = seq
		self.qual = qual

	def __str__(self):
		self.read = self.header + "\n" + self.seq + "\n" + "+" + "\n" + self.qual + "\n"
		return self.read

# Takes a fasta file with references and creates a Bowtie2 index
def index(reference):
	# Check if index exists instead...
	subprocess.call(["bowtie2-build", reference, REF])

# Takes a pair of fastq files and a fasta file with genome references as input
# Returns a dictioneary with the counts of mapped reads to the individual reference "species"
def bowtie2(fastq1, fastq2, reference, sam_file_name):
	indexed_db = files.file_name_base(reference)
	index(reference)
	sam = subprocess.check_output(["bowtie2", "-x", REF, "-1", fastq1, "-2", fastq2])

	# Count the mapped reads...
	mapped = {}
	unmapped_reads = Fastq_file(sam_file_name)		# Devel.
	for line in sam.split("\n"):
		# Skip SAM header lines
		try:
			if line[0:3] in SAM_HEADERS:
				continue
			else:
				ref_name = line.split()[2]
				if ref_name not in mapped:
					mapped[ref_name] = 1
				# ...and store unmapped reads in a file
				elif ref_name == "*":
					mapped[ref_name] += 1
					read = Fastq_read(line.split()[0], line.split()[9], line.split()[10])
					unmapped_reads.add_seq(str(read))
				else:
					mapped[ref_name] += 1
		except IndexError:
			continue
	
	print json.dumps(mapped)
	print mapped

	
