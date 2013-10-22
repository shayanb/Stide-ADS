#!/usr/bin/env python

####### STIDE Technique #######
###### Shayan Eskandari #######
###### MIT Copyleft License ######


import fileinput
import os

# hard coded file path. changed it to whatever implementation you need, this did what I needed
# note: sort.txt is just a combined version of all the anubis-good sequences (Norm-DB.txt) sorted with sort command

norm="/Users/sbeta/Desktop/PRoject/ISSTA12-mal-data/anubis-good/sort.txt"
malware="/Users/sbeta/Desktop/PRoject/ISSTA12-mal-data/malware/1grams-seq_Malware-5W-seq.txt"
OUTPUT = "malware-5W-Flagg.csv"

def compare(norm,malware):
	seq = open(OUTPUT, "a")
	seq.write("s1,s2,s3,s4,s5,flag")
	seq.write("\n")
	with open(malware) as malfile:
		for line in malfile:
			if line in open(norm).read():
				print line
				seq = open(OUTPUT, "a")
				seq.write(line.rstrip('\n'))
				seq.write("0")
				seq.write("\n")

			else:
				seq = open(OUTPUT, "a")
				seq.write(line.rstrip('\n'))
				seq.write("1")
				seq.write("\n")
				print "NO"





compare(norm,malware)