#! /usr/bin/env python3
# specify he input files
gff_file = "watermelon.gff"


#open the fsa file
fsa = open("watermelon.fsa")
fsa_file = fsa.read()
#trim the header
fsa_seq = fsa_file[196:]

#read the ff file, line by line
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
