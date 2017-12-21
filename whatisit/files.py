#!/usr/bin/env python

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


#def sam_file_name(fastq_file_name):
#	if "fastq" in fastq_file_name:
#		return fastq_file_name.rstrip(".fastq")
#	if "fq" in fastq_file_name:
#		return fastq_file_name.rstrip(".fq")

# Takes a filename and returns it as a string without file extention
def file_name_base(file_name):
	return file_name.rsplit(".", 1)[0]
