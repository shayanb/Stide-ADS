#!/usr/bin/env python

import fileinput
import os


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
#				seq.write(" ")
				seq.write("0")
				seq.write("\n")

			else:
				seq = open(OUTPUT, "a")
				seq.write(line.rstrip('\n'))
				seq.write("1")
				seq.write("\n")
				print "NO"





compare(norm,malware)