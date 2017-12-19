#!/usr/bin/env python

import subprocess

REF="References"


# Takes a fasta file with references and creates a Bowtie2 index
def index(reference):
	# Check if index exists instead...
	subprocess.call(["bowtie2-build", reference, REF])

# Takes a pair of fastq files and a fasta file with genome references as input
def bowtie2(fastq1, fastq2, reference):
#	index(reference)
	subprocess.call(["bowtie2", "-x", REF, "-1", fastq1, "-2", fastq2, "-S", "out.sam"])




	
