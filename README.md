# Introduction
This repository contains (some of) the code generated in the Skeletonema marinoi genome project.

# whatisit

## Input data
* The first part of the header in the fasta file with reference sequences should be the taxonomic affinity displaied in the resulting plots.

* Requires: bowtie2 version >=2.3.1

# Generate the directory structure
```
for i in {101..194}; do mkdir P14203_${i}; ln -s $(ls /proj/data23/Skeletonema_marinoi/Genome/M.Topel_19_01/P14203/P14203_${i}/02-FASTQ/191018_A00187_0208_BHNG2MDSXX/*_R1_001.fastq.gz) P14203_${i}/; ln -s $(ls /proj/data23/Skeletonema_marinoi/Genome/M.Topel_19_01/P14203/P14203_${i}/02-FASTQ/191018_A00187_0208_BHNG2MDSXX/*_R2_001.fastq.gz) P14203_${i}/; done
```
