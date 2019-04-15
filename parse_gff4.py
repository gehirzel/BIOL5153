#! /usr/bin/env python3
# specify the input files
import argparse
from Bio import SeqIO
import csv

parser = argparse.ArgumentParser(description = "finds GC content of features from fsa files")
parser.add_argument("gff", help="name of .gff file.")
parser.add_argument("fsa", help="name of .fsa file.")

args = parser.parse_args()

#open the fsa file & extract sequence
fsa_name = args.fsa + ".fsa"
handle = open(fsa_name)
for seq_record in SeqIO.parse(handle, "fasta"):
	fsa_seq = seq_record.seq

#read the gff file line by line
gff_file = args.gff + '.gff'
gff = open(gff_file, "r")
gff_read = csv.reader(gff, delimiter="\t")	
for line in gff_read:
	if not line:
		continue
	else:
		start = int(fields[3]) - 1
		end = int(fields[4])
	
	#print sequence for this feature
		feature_seq = fsa_seq[start:end]
		numC = feature_seq.count('C')
		numG = feature_seq.count('G')
		print("Sequence for this " + str(fields[2]) + " is " + feature_seq  + ". There are " + str(numG)  + " Gs and " +  str(numC) + " Cs in this sequence.")
gff.close()
handle.close()

