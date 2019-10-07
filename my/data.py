#!/usr/bin/env python


def download_ncbi_bact_genomes():
	# https://www.biostars.org/p/61081/

	# 1. Get the list of assemblies:
	wget ftp://ftp.ncbi.nlm.nih.gov/genomes/genbank/bacteria/assembly_summary.txt

	# 2. Parse the addresses of complete genomes from it (right now n = 4,804):
	awk -F '\t' '{if($12=="Complete Genome") print $20}' assembly_summary.txt > assembly_summary_complete_genomes.txt

	# 3. Fetch data
	# ORG: for next in $(cat assembly_summary_complete_genomes.txt); do wget -P GbBac "$next"/*genomic.fna.gz; done
	for next in $(cat assembly_summary_complete_genomes.txt); do wget -nc "$next"/*[0-9]_genomic.fna.gz; done
	
	# 4. Remove rna and cds data to only use the genomic sequences
	rm *_rna_* *_cds_*

	# 5. Extract data
	*.gz

	# 6. Concatenate data
	cat *.fna > all_complete_Gb_bac.fasta

	### Virus ###

	# 1. Get the list of assemblies:
	wget ftp://ftp.ncbi.nlm.nih.gov/genomes/genbank/viral/assembly_summary.txt

	# 2. Parse the addresses of complete genomes from it (right now n = 4,804):
	awk -F '\t' '{if($12=="Complete Genome") print $20}' assembly_summary.txt > assembly_summary_complete_genomes.txt



def create_databases():

	# 1. for i in $(ls *.fna); do bowtie2-build $i $i; done
