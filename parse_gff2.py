#! /usr/bin/env python3
# specify the input files
import argparse
parser = argparse.ArgumentParser(description = "finds GC content of features from fsa files")
parser.add_argument("gff", help="name of .gff file.")
parser.add_argument("fsa", help="name of .fsa file.")

args = parser.parse_args()

#open the fsa file
fsa_name =  args.fsa + ".fsa"
fsa = open(fsa_name)
fsa_file = fsa.read()

#trim the header
#have to change this line so this parser can work with other files besides watermelon...not sure how
fsa_seq = fsa_file[196:]

#read the ff file, line by line

gff_file = args.gff + '.gff'
gff = open(gff_file, "r")
for line in gff:
	#skip blank lines
	line = line.rstrip('\n')
	fields = line. split("\t")
	start = int(fields[3]) - 1
	end = int(fields[4])
	
	#print sequence for this feature
	feature_seq = fsa_seq[start:end]
	numC = feature_seq.count('C')
	numG = feature_seq.count('G')
	print("Sequence for this " + str(fields[2]) + " is " + feature_seq  + ". There are " + str(numG)  + " Gs and " +  str(numC) + " Cs in this sequence.")
gff.close()
fsa.close()
#read gff
#open fsa
#read fsa
#for feature in gff:
#
