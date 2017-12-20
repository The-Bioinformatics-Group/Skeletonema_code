#!/usr/bin/env python

import subprocess

REF = "References"
SAM_HEADERS = ["@HD", "@SQ", "@RG", "@PG", "@CO"]

class Fastq_file(object):
	def __init__(self, name):
		self.name = name
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
def bowtie2(fastq1, fastq2, reference):
	index(reference)
	sam = subprocess.check_output(["bowtie2", "-x", REF, "-1", fastq1, "-2", fastq2])

	# Count the mapped reads...
	mapped = {}
	unmapped_reads = Fastq_file("Unmapped.fastq")		# Devel.
	for line in sam.split("\n"):
		# Skip SAM header lines
		try:
			if line[0:3] in SAM_HEADERS:
				continue
			else:
				ref_name = line.split()[2]
				if ref_name not in mapped:
					mapped[ref_name] = 1
				# ...and store unmapped reads
				elif ref_name == "*":
					mapped[ref_name] += 1
					read = Fastq_read(line.split()[0], line.split()[9], line.split()[10])
					unmapped_reads.add_seq(str(read))
				else:
					mapped[ref_name] += 1
		except IndexError:
			continue
	
	print mapped

	
