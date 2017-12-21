#!/usr/bin/env python

#def sam_file_name(fastq_file_name):
#	if "fastq" in fastq_file_name:
#		return fastq_file_name.rstrip(".fastq")
#	if "fq" in fastq_file_name:
#		return fastq_file_name.rstrip(".fq")

# Takes a filename and returns it as a string without file extention
def file_name_base(file_name):
	return file_name.rsplit(".", 1)[0]
