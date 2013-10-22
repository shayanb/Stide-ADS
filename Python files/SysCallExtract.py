#!/usr/bin/env python


####### STIDE Technique #######
###### Shayan Eskandari #######
###### MIT Copyleft License ######

import fileinput
import os


file = "1grams-seq_Process-"	#name of the raw trace files without the last number
path = "/Users/sbeta/Desktop/PRoject/ISSTA12-mal-data/anubis-good" #path to the raw trace files
W=5		#window size
K=1	#shift size

def parsefile(file):	#parse the files to extract the sequence files
	with open(file) as f:
		for line in f:
			Syscall=line.split("(")
			print Syscall[0]
			if Syscall[0].isdigit():
				seq = open(file + "-seq.txt", "a")
				seq.write(Syscall[0])
				seq.write(",")


def window(seq):	# to extract windows of size W with the shift size of K from the sequence files (-seq)
	with open(seq) as s:
		for line in s:
			sequence=line.split(",")
			end=len(sequence)-W
			for i in xrange(0,end,K):
				for j in xrange(i,W+i):
					print "K: ", K, "        end: ", end , "         seq: ", sequence[j] 
					norm = open("NormDB.txt", "a")
					norm.write(sequence[j])
					norm.write(",")
				norm.write("\n")




os.chdir(path)
for i in xrange(1,36):		
	parsefile(file + str(i)) 		# To extract sequences from the raw files, the i would be the number in the file name
	window(file + str(i) + "-seq.txt")		# to extract windows of size W with the shift size of K from the sequence files (-seq)

